---
name: runbook
menu-code: RB
description: Runbook operacional passo-a-passo com comandos e validações.
---

# Runbook Operacional de Migração

Gerar um runbook operacional passo-a-passo que um engenheiro possa executar sequencialmente para completar a migração.

## Pré-Condição

Antes de gerar o runbook, aplicar Check de Pré-Requisitos (SKILL.md):
- Acesso a orgs/projetos validado
- Permissões mínimas confirmadas
- CLIs instaladas (Git, az devops, curl/pwsh)
- Tokens configurados (sem pedir valor)
- Conectividade OK

Se faltar algo → listar exatamente o que configurar antes de prosseguir.

## Formato Obrigatório para Cada Passo

Cada passo do runbook DEVE seguir esta estrutura:

```
### Passo N — [Título]

**Objetivo:** O que este passo realiza

**Pré-requisito:** O que deve estar pronto antes

**Comando:**
[bloco de código com comando executável + placeholders]

**Explicação:** O que o comando faz

**Risco:** O que pode dar errado / impacto

**Validação:**
[bloco de código com comando de verificação]

**Resultado esperado:** O que confirma sucesso

**Se falhar:** Ação de contingência
```

## Estrutura do Runbook

### Seção 1 — Preparação do Ambiente

- Verificar/instalar ferramentas
- Configurar variáveis de ambiente (placeholders)
- Testar conectividade com orgs origem e destino
- Validar permissões

### Seção 2 — Migração por Componente

Organizar os passos na ordem de dependência:

1. **Áreas e Iterações** (pré-requisito para Boards)
2. **Process Template / Custom Fields** (pré-requisito para Boards)
3. **Work Items** (Boards)
4. **Repositórios Git** (Repos)
5. **Branch Policies** (pós-repos)
6. **Service Connections** (pré-requisito para Pipelines)
7. **Variable Groups** (pré-requisito para Pipelines)
8. **Agent Pools** (pré-requisito para Pipelines)
9. **Pipelines** (YAML/clássico)
10. **Environments + Approvals** (pós-pipelines)
11. **Service Hooks / Webhooks** (integrações)
12. **Queries e Dashboards** (pós-boards)

### Seção 3 — Validação Pós-Migração

- Script de contagem comparativa (origem vs destino)
- Smoke tests de pipelines
- Validação de permissões/policies
- Teste de integrações

### Seção 4 — Cutover

- Comunicação para times
- Congelamento da origem
- Switch de remotes para devs
- Validação final

### Seção 5 — Rollback (se necessário)

- Critérios de acionamento
- Passos de reversão
- Ponto de não-retorno
- Comunicação de rollback

## Padrão de Comandos

Sempre usar os formatos executáveis apropriados:

- **Git:** `git clone --mirror`, `git push --mirror`, etc.
- **Azure CLI:** `az devops ...` com `--organization` e `--project`
- **REST API:** `curl` ou `Invoke-RestMethod` com headers de auth via variável
- **PowerShell:** quando manipulação de dados é necessária

Placeholders obrigatórios: `<ORG_ORIGEM>`, `<ORG_DESTINO>`, `<PROJECT_ORIGEM>`, `<PROJECT_DESTINO>`, `<PAT_ORIGEM>`, `<PAT_DESTINO>`

## Entregável

- Runbook completo em Markdown (executável sequencialmente)
- Dossiê atualizado com status das fases
