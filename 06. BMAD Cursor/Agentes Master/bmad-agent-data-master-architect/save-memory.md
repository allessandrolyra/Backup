---
name: save-memory
description: Salva decisões e artefatos no Project Ledger
menu-code: SM
---

**Language:** Use `{communication_language}` for all output.

# Salvar no Project Ledger

Salve o progresso do projeto na memória persistente.

## Processo

1. **Carregue** `references/memory-system.md` para a estrutura obrigatória
2. **Leia o Ledger atual** em `{project-root}/_bmad/memory/bmad-agent-data-master-architect-ledger/index.md`
3. **Se não existe**, crie seguindo a estrutura completa
4. **Se existe**, identifique o que mudou desde a última sessão:
   - Novas decisões arquiteturais
   - Artefatos gerados (pipelines, queries, IaC, DAX)
   - Mudanças de requisitos
   - Riscos identificados
   - Resultados de troubleshooting
   - Otimizações aplicadas
5. **Mostre o diff** — Antes → Depois para cada seção alterada
6. **Peça confirmação** antes de salvar
7. **Salve** o Ledger atualizado

## Regras
- Nunca sobrescrever decisões anteriores — adicionar como nova entrada com data
- Manter formato consistente (Data | Decisão | Motivo | Trade-off)
- Riscos e pendências sempre no topo da seção de riscos (prioridade)
- Registrar ADRs (Architecture Decision Records) quando houver decisão entre alternativas
