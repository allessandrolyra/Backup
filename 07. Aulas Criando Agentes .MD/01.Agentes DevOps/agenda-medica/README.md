# Agenda Médica Online

Sistema web para agendamento de consultas médicas. Pacientes podem agendar, visualizar e cancelar consultas; administradores gerenciam horários e confirmações.

## Stack

| Camada | Tecnologia |
|--------|------------|
| Frontend | React 18 + TypeScript + Vite |
| Backend/DB | Supabase (PostgreSQL, Auth, RLS) |
| Estilo | Tailwind CSS |
| Deploy | GitHub Pages / Vercel (gratuito) |

## Funcionalidades

- **Paciente**: Cadastro (nome, contato, consentimento LGPD), autenticação, agendar/visualizar/cancelar consultas
- **Admin**: Gerenciar médicos, horários disponíveis, confirmações
- **Notificações**: Email de confirmação (via Supabase Edge Functions)
- **Observabilidade**: Endpoint `/health`, logs básicos

## Setup

### 1. Criar projeto Supabase (gratuito)

1. Acesse [supabase.com](https://supabase.com) e crie uma conta
2. Crie um novo projeto
3. Execute o SQL em `supabase/schema.sql` no SQL Editor
4. Copie a URL e a chave anônima para `.env.local`

### 2. Configurar variáveis

```bash
cp .env.example .env.local
# Edite .env.local com suas credenciais Supabase
```

### 3. Instalar e rodar

```bash
npm install
npm run dev
```

### 4. Criar primeiro admin

No SQL Editor do Supabase, execute:
```sql
UPDATE profiles SET role = 'admin' WHERE email = 'seu-email@exemplo.com';
```

### 5. Deploy (GitHub Pages / Vercel)

**GitHub Pages:**
```bash
npm run build
# Configure o repositório: Settings > Pages > Source: GitHub Actions ou pasta dist/
```

**Vercel (recomendado):**
```bash
npm run build
# Conecte o repo no vercel.com e faça deploy
```

## Estrutura

```
agenda-medica/
├── src/
│   ├── components/     # Componentes React
│   ├── lib/            # Supabase client, utils
│   ├── pages/          # Páginas da aplicação
│   └── types/          # Tipos TypeScript
├── supabase/
│   ├── schema.sql     # Schema do banco
│   └── functions/     # Edge Functions (notificações)
└── public/
```

## Notificações (opcional)

Para enviar emails de confirmação:
1. Crie conta em [Resend](https://resend.com) (free tier)
2. Configure `RESEND_API_KEY` nas secrets da Edge Function `send-confirmation`
3. Deploy: `supabase functions deploy send-confirmation`

## Licença

MIT - Livre para uso e publicação no GitHub.
