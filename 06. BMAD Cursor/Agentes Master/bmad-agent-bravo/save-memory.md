---
name: save-memory
description: Salva estado de migrações, mappings e freeze windows
menu-code: SM
---

**Language:** Use `{communication_language}` for all output.

# Salvar na Memória

Salve o progresso do projeto na memória persistente.

## Processo

1. **Carregue** `references/memory-system.md` para estrutura do sidecar
2. **Leia o sidecar atual** em `{project-root}/_bmad/memory/bmad-agent-bravo-sidecar/index.md`
3. **Se não existe**, crie estrutura completa: index.md, active-migrations.md, de-para-mappings.md, freeze-calendar.md, audit-history.md
4. **Se existe**, identifique mudanças e atualize o arquivo correto:
   - Migrações → active-migrations.md
   - Mapeamentos → de-para-mappings.md
   - Freeze → freeze-calendar.md
   - Auditorias → audit-history.md
5. **Mostre o diff** — Antes → Depois
6. **Peça confirmação** antes de salvar

## Regras
- Nunca sobrescrever histórico — adicionar como nova entrada com data
- Manter links entre index.md e arquivos específicos
