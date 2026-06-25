---
name: hands-on
description: Gera WIQL, YAML, REST API snippets e Migration Configs
menu-code: HO
---

**Language:** Use `{communication_language}` for all output.

# Hands-on

Gere artefatos práticos para Azure DevOps.

## Processo

1. **Entenda o que gerar** — WIQL, REST API, Migration Config, Pipeline YAML ou Process Template?
2. **Carregue** `references/hands-on.md` para padrões de código
3. **Gere o artefato** seguindo os Code Standards:
   - WIQL: Sempre especificar `System.TeamProject` e `System.WorkItemType`
   - REST: api-version=7.1, incluir error handling
   - YAML: Preferir `extends` templates, multi-stage
   - JSON: Formatação adequada, comments em campos críticos
4. **Valide** — Use `scripts/validate-wiql.py` para queries WIQL quando possível
5. **Sugira salvar** artefatos gerados no sidecar (SM)

## Entregáveis
- Código/config pronto para uso
- Instrução de execução
- Validação (quando script disponível)
