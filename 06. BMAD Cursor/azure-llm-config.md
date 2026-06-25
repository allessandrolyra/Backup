# Azure LLM Infrastructure — BMM Command Center

Provisionado em: 2026-05-11 | Responsável: Astra (SRE Azure)

## Recursos Provisionados

| Recurso | Nome | Localização |
|---|---|---|
| Resource Group | `bmm-llm-rg` | East US |
| Azure OpenAI Service | `bmm-openai-svc` | East US |
| Key Vault | `bmm-llm-kv` | East US |
| Modelo implantado | `gpt-4o` (v2024-11-20) | GlobalStandard |

## Endpoints

```
Azure OpenAI Endpoint:  https://bmm-openai-svc.openai.azure.com/
Key Vault URI:          https://bmm-llm-kv.vault.azure.net/
```

## Secrets no Key Vault

| Secret Name | Descrição |
|---|---|
| `azure-openai-api-key` | API Key do Azure OpenAI Service |
| `azure-openai-endpoint` | Endpoint base do Azure OpenAI |

## Como Recuperar a Chave (CLI)

```bash
# Recuperar a API key
az keyvault secret show \
  --vault-name bmm-llm-kv \
  --name azure-openai-api-key \
  --query value --output tsv

# Recuperar o endpoint
az keyvault secret show \
  --vault-name bmm-llm-kv \
  --name azure-openai-endpoint \
  --query value --output tsv
```

## Configuração para uso no Cursor / Agentes BMM

Para configurar o Azure OpenAI como provider no Cursor:

1. Abra **Settings → Models → Azure OpenAI**
2. Preencha:
   - **Endpoint:** `https://bmm-openai-svc.openai.azure.com/`
   - **API Key:** *(recuperar do Key Vault com o comando acima)*
   - **Deployment name:** `gpt-4o`
   - **API Version:** `2024-08-01-preview`

## Subscription Azure

```
Subscription:  Visual Studio Enterprise Subscription
Subscription ID: 9cfd9e0c-2a0a-4f03-9386-43f53b03da4d
Tenant ID:       cdeec816-d1a9-4c02-98c8-9ef5f2ffdd4c
```

## Limites do Deployment Atual

| Parâmetro | Valor |
|---|---|
| Capacity | 10K TPM (tokens por minuto) |
| SKU | GlobalStandard |
| Rate limit requests | 10 req/10s |

> Para aumentar a capacidade: `az cognitiveservices account deployment update`

## Próximos Passos Recomendados

- [ ] Configurar Managed Identity para acesso sem chave ao Key Vault
- [ ] Criar alertas de custo no Azure Cost Management
- [ ] Adicionar diagnósticos/logs no Azure Monitor
- [ ] Configurar o provider Azure OpenAI no Cursor Settings
