---
name: save-memory
description: Salva decisões e artefatos no Project Ledger
menu-code: SM
---

**Language:** Use `{communication_language}` for all output.

# Salvar no Project Ledger

Salve o progresso do projeto na memória persistente.

## Processo

1. **Carregue** `references/project-ledger.md` para a estrutura obrigatória
2. **Leia o Ledger atual** em `{project-root}/_bmad/memory/bmad-agent-astra-sre-azure-ledger/index.md`
3. **Se não existe**, crie seguindo a estrutura completa (seções A-H)
4. **Se existe**, identifique o que mudou desde a última sessão:
   - Novas decisões técnicas
   - Artefatos gerados
   - Mudanças de requisitos
   - Riscos identificados
5. **Mostre o diff** — Antes → Depois para cada seção alterada
6. **Peça confirmação** antes de salvar
7. **Salve** o Ledger atualizado

## Regras
- Nunca sobrescrever decisões anteriores — adicionar como nova entrada com data
- Manter formato consistente (Data | Decisão | Motivo | Trade-off)
- Riscos e pendências sempre no topo da seção H (prioridade)
