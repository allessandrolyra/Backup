# Arquitetura — Sistema Web de Gerenciamento de Estacionamento

**Autor:** Wagner (Arquiteto)  
**Data:** 2025-03-19  
**Fonte:** PRD `prd-estacionamento.md`  
**Restrição:** Ferramentas 100% gratuitas (free tier)

---

## 1. Visão Geral

Sistema web responsivo com stack gratuita: **Next.js** (frontend + API) + **Supabase** (banco, auth, realtime) + **Vercel** (deploy). Tudo em free tier.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Browser       │────▶│   Vercel        │────▶│   Supabase      │
│   (React/Next)  │     │   (Next.js)     │     │   (PostgreSQL   │
│                 │◀────│   API Routes    │◀────│    Auth         │
└─────────────────┘     └─────────────────┘     │    Realtime)    │
                                                  └─────────────────┘
```

---

## 2. Decisões Técnicas

### 2.1 Stack Escolhida

| Camada | Tecnologia | Justificativa | Free Tier |
|--------|------------|---------------|-----------|
| **Frontend** | Next.js 14 (App Router) | SSR, API routes, responsivo | ✅ |
| **Banco de Dados** | Supabase (PostgreSQL) | PostgreSQL gerenciado, auth, realtime | ✅ 500MB |
| **Autenticação** | Supabase Auth | Integrado, JWT, roles | ✅ 50k MAU |
| **Deploy** | Vercel | Next.js nativo, edge | ✅ 100GB bandwidth |
| **Realtime** | Supabase Realtime | Vagas em tempo real | ✅ Incluído |

### 2.2 Por que Supabase

- **PostgreSQL** — Relacional, adequado para vagas, entradas, mensalistas
- **Auth** — Login, roles (operador/admin) sem custo
- **Realtime** — Atualização de vagas disponíveis/ocupadas sem polling
- **Free tier** — 500MB DB, 50k usuários auth, 2 projetos
- **Sem servidor próprio** — Tudo gerenciado

### 2.3 Alternativas Descartadas

| Alternativa | Motivo |
|-------------|--------|
| SQLite + Vercel | SQLite não persiste em serverless; Supabase oferece mais |
| Firebase | NoSQL menos adequado para relações (entradas, mensalistas) |
| Railway + PostgreSQL | Free tier mais limitado que Supabase |
| MongoDB Atlas | Overkill; PostgreSQL relacional é mais adequado |

---

## 3. Modelo de Dados (Supabase/PostgreSQL)

### 3.1 Diagrama ER (resumido)

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ config           │     │ mensalistas      │     │ entradas          │
├──────────────────┤     ├──────────────────┤     ├──────────────────┤
│ id (PK)          │     │ id (PK)          │     │ id (PK)          │
│ total_vagas      │     │ nome             │     │ placa            │
│ valor_hora       │     │ placa            │     │ tipo             │
│ fracao_minima    │     │ validade_ate     │     │ entrada_em       │
│ updated_at       │     │ ativo            │     │ saida_em         │
└──────────────────┘     └──────────────────┘     │ valor_pago      │
                                                    │ mensalista_id   │
                                                    └──────────────────┘
```

### 3.2 Tabelas

**config** — Configuração global (uma linha)
```sql
- id: uuid PK
- total_vagas: int (80)
- valor_hora: decimal
- fracao_minima_minutos: int
- updated_at: timestamptz
```

**mensalistas**
```sql
- id: uuid PK
- nome: text
- placa: text UNIQUE
- validade_ate: date
- ativo: boolean
- created_at, updated_at: timestamptz
```

**entradas**
```sql
- id: uuid PK
- placa: text
- tipo: enum ('rotativo', 'mensalista')
- entrada_em: timestamptz
- saida_em: timestamptz (nullable)
- valor_pago: decimal (nullable)
- mensalista_id: uuid FK (nullable)
- created_at: timestamptz
```

**users** (Supabase Auth) — Extensão com role
```sql
-- Via Supabase: auth.users
-- Metadata: role = 'operador' | 'admin'
```

### 3.3 RLS (Row Level Security)

- **Operador:** leitura/escrita em `entradas`, leitura em `config`, `mensalistas`
- **Admin:** leitura/escrita em todas as tabelas

---

## 4. Estrutura da Aplicação (Next.js)

```
estacionamento/
├── app/
│   ├── (auth)/
│   │   ├── login/
│   │   └── layout.tsx
│   ├── (operador)/
│   │   ├── dashboard/          # Tela principal: vagas, entrada, saída
│   │   └── layout.tsx
│   ├── (admin)/
│   │   ├── admin/              # Painel admin
│   │   │   ├── mensalistas/
│   │   │   ├── config/
│   │   │   └── dashboard/
│   │   └── layout.tsx
│   ├── api/                    # API routes (se necessário)
│   └── layout.tsx
├── lib/
│   ├── supabase/
│   │   ├── client.ts           # Cliente browser
│   │   ├── server.ts           # Cliente server
│   │   └── middleware.ts
│   ├── services/
│   │   ├── entrada-service.ts
│   │   ├── vaga-service.ts
│   │   ├── mensalista-service.ts
│   │   └── payment-service.ts  # Abstrato para gateway futuro
│   └── utils/
├── components/
├── supabase/
│   ├── migrations/             # SQL migrations
│   └── seed.sql
└── .env.local                  # NEXT_PUBLIC_SUPABASE_URL, SUPABASE_SERVICE_KEY
```

---

## 5. PaymentService (Preparado para Gateway)

```typescript
// lib/services/payment-service.ts

export interface PaymentResult {
  success: boolean;
  transactionId?: string;
  error?: string;
}

export interface PaymentService {
  processPayment(amount: number, metadata: Record<string, unknown>): Promise<PaymentResult>;
}

// MVP: implementação interna (registro manual)
export class InternalPaymentService implements PaymentService {
  async processPayment(amount: number): Promise<PaymentResult> {
    // Apenas registra; operador confirma pagamento manual
    return { success: true };
  }
}

// Futuro: StripePaymentService, MercadoPagoPaymentService, etc.
```

---

## 6. Realtime (Vagas)

Supabase Realtime para atualizar vagas sem refresh:

```typescript
// Subscribe em mudanças de entradas (entrada/saída)
supabase
  .channel('vagas')
  .on('postgres_changes', { event: '*', schema: 'public', table: 'entradas' }, () => {
    // Recalcular disponíveis = total - COUNT(entradas WHERE saida_em IS NULL)
    refreshVagas();
  })
  .subscribe();
```

---

## 7. Autenticação (Supabase Auth)

- **Sign up / Sign in** — Email + senha (Supabase Auth)
- **Roles** — `user_metadata.role`: `operador` ou `admin`
- **Middleware** — Protege rotas `/admin/*` para role admin
- **RLS** — Políticas no Supabase por role

---

## 8. Deploy

| Etapa | Ferramenta | Config |
|-------|------------|--------|
| Repositório | GitHub | Público ou privado |
| Build | Vercel | Auto-deploy em push |
| Variáveis | Vercel | `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY` |
| Banco | Supabase | Projeto free, URL e key no .env |

**URLs:**
- App: `https://estacionamento-xxx.vercel.app`
- Supabase: `https://xxx.supabase.co`

---

## 9. Limites do Free Tier (Resumo)

| Serviço | Limite Free |
|---------|-------------|
| **Supabase** | 500MB DB, 50k MAU auth, 2 projetos |
| **Vercel** | 100GB bandwidth, 100 deployments/mês |
| **Next.js** | Sem limite (framework) |

Para 80 vagas e uso de um estacionamento, o free tier é suficiente.

---

## 10. Revisão Diana

Modelo aprovado. Ver `modelo-dados-diana-review.md` e `supabase-migrations/001_initial_schema.sql`.

## 11. Próximos Passos
2. **Felipe** — Implementar seguindo esta arquitetura
3. **Quinn** — Testes E2E dos fluxos
4. **Davi** — Pipeline CI/CD (GitHub Actions + Vercel)

---

*Arquitetura criada pelo Time MEQ. Stack 100% free: Next.js + Supabase + Vercel.*
