---
name: migration
description: Migrações com ADO Migration Tools, OpsHub ou Data Migration Tool
menu-code: MG
---

**Language:** Use `{communication_language}` for all output.

# Migration

Execute migrações complexas de Azure DevOps.

## Processo

1. **Entenda o escopo** — Origem → Destino, volume, tipos de WIT
2. **Carregue** `references/playbook-migration.md` para playbook
3. **Escolha ferramenta:** ADO Migration Tools, OpsHub ou Data Migration Tool
4. **Planeje:**
   - Pré-requisitos e dependências
   - Sandbox run obrigatório antes de produção
   - Mapeamento de identidades (identity mapping)
   - Estratégia de links e attachments
5. **Execute em batches** — Documentar progresso por batch
6. **Valide pós-migração** — ReflectedWorkItemId, links, attachments, history
7. **Use** `scripts/generate-migration-config.py` para configs base
8. **Use** `scripts/find-orphans.py` para detectar itens órfãos

## Entregáveis
- Migration Config (JSON)
- Plano de batches com cronograma
- Relatório de validação pós-migração
- Risk Matrix
