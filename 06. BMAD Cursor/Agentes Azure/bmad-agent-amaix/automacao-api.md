---
name: automacao-api
menu-code: AU
description: Scripts e chamadas API (REST/CLI/PowerShell) com placeholders seguros.
---

# Automação e API

Gerar scripts, chamadas API e automações para operações de migração Azure DevOps, sempre com placeholders seguros e validação integrada.

## Regras de Geração de Scripts

### Segurança (OBRIGATÓRIO)

- Placeholders obrigatórios: `<ORG>`, `<PROJECT>`, `<TOKEN>`, `<SECRET>`
- NUNCA incluir dados sensíveis reais
- Credenciais via variáveis de ambiente: `$env:ADO_PAT` (PowerShell) ou `$ADO_PAT` (bash)
- Scripts devem ser idempotentes sempre que possível
- Incluir `--dry-run` ou equivalente quando disponível

### Estrutura de Cada Script

```
# ============================================
# Objetivo: [O que este script faz]
# Pré-requisitos: [O que deve estar instalado/configurado]
# Uso: [Como executar]
# Risco: [O que pode dar errado]
# ============================================

# Variáveis (configurar antes de executar)
# Validação de pré-requisitos
# Execução principal
# Validação pós-execução
```

## Catálogo de Automações

### Azure CLI (az devops)

**Inventário de projetos:**
```bash
az devops project list --organization https://dev.azure.com/<ORG> --output table
```

**Listar repos:**
```bash
az repos list --organization https://dev.azure.com/<ORG> --project <PROJECT> --output table
```

**Listar pipelines:**
```bash
az pipelines list --organization https://dev.azure.com/<ORG> --project <PROJECT> --output table
```

**Listar service connections:**
```bash
az devops service-endpoint list --organization https://dev.azure.com/<ORG> --project <PROJECT> --output table
```

### REST API

**Padrão de chamada (PowerShell):**
```powershell
$org = "<ORG>"
$project = "<PROJECT>"
$pat = $env:ADO_PAT
$base64Auth = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$pat"))
$headers = @{ Authorization = "Basic $base64Auth" }

$uri = "https://dev.azure.com/$org/$project/_apis/wit/workitems?api-version=7.1"
$response = Invoke-RestMethod -Uri $uri -Headers $headers -Method Get
```

**Padrão de chamada (curl):**
```bash
ORG="<ORG>"
PROJECT="<PROJECT>"
PAT="$ADO_PAT"

curl -s -u ":$PAT" \
  "https://dev.azure.com/$ORG/$PROJECT/_apis/wit/workitems?api-version=7.1"
```

### Scripts de Validação

**Comparar contagem de work items:**
```powershell
function Get-WorkItemCount {
    param($Org, $Project, $Pat)
    $base64Auth = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$Pat"))
    $headers = @{ Authorization = "Basic $base64Auth" }
    $query = @{ query = "SELECT [System.Id] FROM WorkItems" } | ConvertTo-Json
    $uri = "https://dev.azure.com/$Org/$Project/_apis/wit/wiql?api-version=7.1"
    $result = Invoke-RestMethod -Uri $uri -Headers $headers -Method Post -Body $query -ContentType "application/json"
    return $result.workItems.Count
}

$countOrigem = Get-WorkItemCount -Org "<ORG_ORIGEM>" -Project "<PROJECT_ORIGEM>" -Pat $env:PAT_ORIGEM
$countDestino = Get-WorkItemCount -Org "<ORG_DESTINO>" -Project "<PROJECT_DESTINO>" -Pat $env:PAT_DESTINO

Write-Host "Origem: $countOrigem | Destino: $countDestino | Match: $($countOrigem -eq $countDestino)"
```

**Comparar branches de repo:**
```bash
echo "=== Origem ==="
git ls-remote --heads https://$PAT_ORIGEM@dev.azure.com/<ORG_ORIGEM>/<PROJECT_ORIGEM>/_git/<REPO> | wc -l

echo "=== Destino ==="
git ls-remote --heads https://$PAT_DESTINO@dev.azure.com/<ORG_DESTINO>/<PROJECT_DESTINO>/_git/<REPO> | wc -l
```

**Validar pipelines (smoke test):**
```powershell
function Test-PipelineRun {
    param($Org, $Project, $Pat, $PipelineId)
    $base64Auth = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$Pat"))
    $headers = @{ Authorization = "Basic $base64Auth" }
    $uri = "https://dev.azure.com/$Org/$Project/_apis/pipelines/$PipelineId/runs?api-version=7.1"
    $body = @{ } | ConvertTo-Json
    $result = Invoke-RestMethod -Uri $uri -Headers $headers -Method Post -Body $body -ContentType "application/json"
    return $result
}
```

### Scripts de Migração

**Mirror de repo (bash):**
```bash
REPO_NAME="<REPO>"
git clone --mirror "https://$PAT_ORIGEM@dev.azure.com/<ORG_ORIGEM>/<PROJECT_ORIGEM>/_git/$REPO_NAME"
cd "$REPO_NAME.git"
git remote add target "https://$PAT_DESTINO@dev.azure.com/<ORG_DESTINO>/<PROJECT_DESTINO>/_git/$REPO_NAME"
git push --mirror target
cd ..
echo "Mirror completo: $REPO_NAME"
```

**Batch mirror de múltiplos repos (PowerShell):**
```powershell
$repos = @("<REPO_1>", "<REPO_2>", "<REPO_3>")
$results = @()

foreach ($repo in $repos) {
    Write-Host "Migrando: $repo"
    git clone --mirror "https://$($env:PAT_ORIGEM)@dev.azure.com/<ORG_ORIGEM>/<PROJECT_ORIGEM>/_git/$repo"
    Set-Location "$repo.git"
    git remote add target "https://$($env:PAT_DESTINO)@dev.azure.com/<ORG_DESTINO>/<PROJECT_DESTINO>/_git/$repo"
    $pushResult = git push --mirror target 2>&1
    $results += @{ Repo = $repo; Status = if ($LASTEXITCODE -eq 0) { "OK" } else { "FALHA" }; Detail = $pushResult }
    Set-Location ..
}

$results | Format-Table -AutoSize
```

## Geração Sob Demanda

Quando o usuário solicitar um script ou automação específica, seguir:

1. Entender o objetivo
2. Escolher o formato mais adequado (bash/pwsh/python/curl)
3. Gerar com a estrutura padrão (objetivo, pré-requisitos, uso, risco)
4. Incluir validação pós-execução
5. Manter placeholders e idempotência

## Entregável

- Scripts prontos para execução (com placeholders)
- Instruções de configuração de variáveis de ambiente
- Validações integradas
- Dossiê atualizado
