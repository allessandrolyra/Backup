# Standard Output Format

## Modo Executor (quando implementa)

1. **O que fiz** (resumo das ações)
2. **Arquivos criados/modificados** (lista)
3. **Decisões tomadas** (trade-offs, se houver)
4. **Validação** (lint/types/testes — resultado)
5. **Próximos passos** (max. 3)

## Modo Consultoria (quando apenas recomenda)

1. Resumo executivo
2. Solução (UX/UI/FE)
3. Decisão técnica (trade-offs)
4. Acessibilidade + Performance
5. Implementação (passo a passo)
6. Riscos e mitigação
7. Próximas perguntas (max. 3)

## Modos de Execução

| Modo | Ativação | Comportamento |
|------|----------|---------------|
| **Rápido** (default) | Pedidos diretos, fixes pontuais | Implementa direto, resumo curto |
| **Detalhado** | "explique", comparações | Implementa + explica decisões e alternativas |
| **Arquitetura** | Mudanças estruturais, escala | Apresenta 2 opções antes de implementar |
| **Somente Consultoria** | "analise", "o que acha" | NÃO implementa, apenas recomenda |

## Modos Especiais

| Modo | Ativação | Entrega |
|------|----------|---------|
| **SCAFFOLD** | "crie um componente/página/feature" | Estrutura completa com código funcional |
| **REFACTOR** | "refatore este código" | Código melhorado + explicação de ganhos |
| **AUDITORIA** | "audite esta página/componente" | Issues (UX/A11y/Perf) com severidade e fix |
| **DESIGN_CRITIQUE** | "critique este design" | Hierarquia, CTA, consistência, carga cognitiva |
| **MIGRATION** | "migre para Server Components" | Plano + execução por etapas |
