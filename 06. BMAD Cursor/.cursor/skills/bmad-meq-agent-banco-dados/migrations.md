---
name: migrations
description: Planeja migrations e evolução do schema
menu-code: MG
---

# Migrations

Planeje migrations e evolução do schema sem quebrar dados existentes.

## Processo

1. **Entenda a mudança** — O que precisa mudar no schema?

2. **Tipos de migração:**
   - **Aditiva** — Nova coluna/tabela (nullable ou default) — baixo risco
   - **Destrutiva** — Remover coluna/tabela — requer cuidado
   - **Transformativa** — Alterar tipo, renomear — requer script

3. **Estratégia:**
   - Expandir → Migrar dados → Contratar (expand-contract)
   - Evitar downtime quando possível
   - Backup antes de alterações destrutivas

4. **Ordem de execução:**
   - Migrations sequenciais por versão
   - Rollback planejado se possível

5. **Output** — Gere scripts de migration ou instruções. Sugira salvar (SM).

## Regras

- Nunca perder dados
- Testar em staging antes de produção
- Documentar cada migration
