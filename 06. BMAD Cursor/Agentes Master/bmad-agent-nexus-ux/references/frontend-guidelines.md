# Frontend Engineering Guidelines

Este documento é o reference técnico para todas as capacidades do Nexus.

## Scaffolding Padrão

Detecte o padrão do projeto existente. Se não houver, use como default:

### React/Next.js (TypeScript)
```
components/
  NomeComponente/
    NomeComponente.tsx        # Componente principal
    NomeComponente.test.tsx   # Testes
    NomeComponente.module.css # Estilos (se CSS Modules)
    index.ts                  # Re-export
    types.ts                  # Tipos/interfaces (se complexo)
```

### Vue/Nuxt
```
components/
  NomeComponente/
    NomeComponente.vue        # SFC
    NomeComponente.spec.ts    # Testes
    index.ts                  # Re-export
```

### Angular
```
components/
  nome-componente/
    nome-componente.component.ts
    nome-componente.component.html
    nome-componente.component.scss
    nome-componente.component.spec.ts
```

**Regra:** Se o projeto já tem um padrão de scaffolding, siga-o.

## Arquitetura Frontend (Stack-Agnostic)

- Separar responsabilidades: UI (components) / Lógica (hooks/composables/services) / Serviços (API/clients)
- Evitar componentes gigantes; preferir composição
- Estado: local primeiro → server state cache (React Query/SWR/Pinia/NGRX) → global só se necessário
- Preferir server-side rendering quando possível; client-side apenas para interatividade
- Minimizar JS no client; reduzir hidratação desnecessária
- Escolher SSR vs SSG vs ISR conforme a natureza do dado e SEO

## Performance (Core Web Vitals)

### Métricas Alvo
- **LCP** <= 2.5s
- **INP** <= 200ms
- **CLS** < 0.1

### Processo de Otimização
1. **Diagnóstico provável** (causas root)
2. **Quick wins** (ações imediatas — implementar direto)
3. **Mudanças estruturais** (longo prazo — com plano)
4. **Medição** (lab + RUM) e como validar LCP/INP/CLS

## Acessibilidade (WCAG 2.2 AA — Checklist Obrigatório)

- HTML semântico primeiro; ARIA só quando necessário e corretamente
- [ ] Teclado (Tab/Shift+Tab; Enter/Esc quando aplicável)
- [ ] Foco visível e ordem correta
- [ ] Nome acessível (labels; aria-label quando necessário)
- [ ] Formulários: erros claros + instrução de correção
- [ ] Contraste mínimo; não depender só de cor
- [ ] Foco não pode ficar obscured por overlays/modais
- [ ] Conteúdo previsível e compreensível (POUR)

## Testes (Práticos e Resilientes)

- Priorizar testes que imitam uso real (evitar detalhes internos)
- **E2E**: smoke dos fluxos críticos
- **Integração**: componentes + fluxos
- **Unit**: lógica pura/utilitários
- Após implementar, rodar testes se terminal disponível

## Observabilidade

- Logs estruturados, Sentry (ou similar), RUM, feature flags
- Sempre sugerir: Evento, Funil, KPI (conversão, abandono, tempo de tarefa, taxa de erro)

## Regras de Execução

- **Sempre leia antes de escrever.** Nunca crie componente sem verificar se já existe similar
- **Não invente imports.** Leia package.json/dependências e estrutura real
- **Mantenha consistência.** Siga padrões de nomeação, estrutura e estilo do projeto
- **Valide após implementar.** Rode lint/typecheck quando disponível
- **Ações destrutivas pedem confirmação.** Delete e overwrites significativos devem ser confirmados

## Definition of Done

Uma solução só está pronta se:
- [ ] Resolve o problema do usuário e define métrica de sucesso
- [ ] Considera estados: loading, empty, error, sucesso, retry (quando aplicável)
- [ ] Atende checklist mínimo de acessibilidade (WCAG 2.2 AA)
- [ ] Não degrada Core Web Vitals
- [ ] Pode ser monitorada (erros + eventos + RUM)
- [ ] Tem testes mínimos proporcionais ao risco
- [ ] **[EXECUTOR]** Código criado/editado nos arquivos reais
- [ ] **[EXECUTOR]** Lint/typecheck passou (quando disponível)
- [ ] **[EXECUTOR]** Lista de arquivos criados/modificados reportada
