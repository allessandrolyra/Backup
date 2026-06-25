---
name: integracoes
menu-code: IN
description: Análise e plano para integrações (ServiceNow, Jira, hooks, webhooks).
---

# Integrações — Análise e Plano de Migração

Analisar, mapear e planejar a migração de todas as integrações conectadas ao Azure DevOps.

## 1. Inventário de Integrações

Mapear todas as integrações ativas na organização/projeto origem:

### Service Connections

- Tipo (Azure RM, Docker Registry, GitHub, Generic, Kubernetes, etc.)
- Nome e ID
- Escopo (projeto ou org)
- Pipelines que consomem
- Permissões configuradas ("shared" vs "restricted")

### Service Hooks

- Eventos assinados (work item updated, build completed, PR created, etc.)
- Consumer (tipo de destino: webhook, Slack, Teams, ServiceNow, etc.)
- URL do endpoint
- Filtros configurados (projeto, área, pipeline específica)
- Status (enabled/disabled)

### Webhooks Customizados

- URL destino
- Eventos monitorados
- Payload format
- Auth method (basic, token, header)

### Integrações de Terceiros

- **ServiceNow:** connector type, instance URL, mapeamento de work items ↔ incidents/changes
- **Jira:** sync direction, field mapping, projeto Jira vinculado
- **Slack/Teams:** canais, notificações configuradas
- **SonarQube/SonarCloud:** service connections, quality gates
- **Container Registries:** ACR, Docker Hub, outros
- **Package Feeds:** NuGet, npm, Maven (Azure Artifacts)

## 2. Análise de Impacto

Para cada integração, classificar:

| Classificação | Critério | Ação |
|--------------|----------|------|
| **Migra direto** | Configuração simples, sem segredos complexos | Recriar no destino |
| **Requer reconfiguração** | Tokens/endpoints mudam, mas lógica é a mesma | Recriar + reconfigurar credenciais |
| **Requer redesenho** | Integração depende de IDs/URLs hardcoded da origem | Redesenhar com novos endpoints |
| **Deprecar** | Integração obsoleta ou não mais necessária | Documentar e não migrar |

## 3. Plano de Migração por Tipo

### Service Connections

1. Listar todas do projeto origem (`az devops service-endpoint list`)
2. Classificar por tipo
3. Recriar no destino (NUNCA copiar secrets — reconfigurar)
4. Configurar permissões (NUNCA "grant access to all pipelines")
5. Testar conectividade de cada connection
6. Atualizar pipelines para referenciar novas connections

### Service Hooks

1. Exportar configuração dos hooks ativos
2. Verificar se endpoints destino estão acessíveis
3. Recriar hooks no projeto destino
4. Ajustar filtros para novo projeto/área
5. Testar disparo com evento simulado
6. Validar payload recebido no consumer

### Integrações ServiceNow

1. Documentar connector atual (tipo, instance, credenciais referenciadas)
2. Verificar se conector é project-scoped ou org-scoped
3. Reconfigurar conector no destino com a mesma instance ServiceNow
4. Revalidar mapeamento de campos (work item ↔ incident/change)
5. Testar ciclo completo: criar item no ADO → refletir no SNOW (e vice-versa)

### Integrações Jira

1. Documentar sync configuration atual
2. Verificar direção de sync (ADO→Jira, Jira→ADO, bidirecional)
3. Reconfigurar no destino
4. Revalidar field mapping
5. Testar sync com item de teste

## 4. Dependências Externas

Verificar e documentar:

- **IP Allowlists:** endpoints que filtram por IP (atualizar se org destino tem IPs diferentes)
- **Firewall Rules:** portas e protocolos necessários
- **Certificates:** certificados SSL/TLS que possam expirar ou mudar
- **DNS:** registros que apontem para a org origem
- **OAuth Apps:** registros de app que referenciam org origem (redirect URIs)

## 5. Validação

Para cada integração migrada:

- [ ] Conexão estabelecida com sucesso
- [ ] Evento de teste disparado e recebido
- [ ] Payload correto no destino
- [ ] Permissões least privilege aplicadas
- [ ] Documentação atualizada com novos endpoints/IDs

## Entregável

- Inventário completo de integrações (tabela)
- Classificação de impacto por integração
- Plano de migração por tipo
- Checklist de validação
- Lista de dependências externas
- Dossiê atualizado
