---
name: save-memory
description: Salva decisões e artefatos no Project State
menu-code: SM
---

**Language:** Use `{communication_language}` for all output.

# Salvar no Project State

Salve o progresso do projeto na memória persistente.

## Processo

1. **Carregue** `references/project-state.md` para a estrutura obrigatória
2. **Leia o Project State atual** em `{project-root}/_bmad/memory/bmad-agent-artemis-aws-sidecar/index.md`
3. **Se não existe**, crie seguindo a estrutura completa (seções A-F)
4. **Se existe**, identifique o que mudou desde a última sessão
5. **Mostre o diff** — Antes → Depois para cada seção alterada
6. **Peça confirmação** antes de salvar
7. **Salve** o Project State atualizado

## Regras
- Nunca sobrescrever decisões anteriores — adicionar como nova entrada com data
- Riscos e pendências sempre priorizados no topo da seção E
