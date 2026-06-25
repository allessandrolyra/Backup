---
name: otimizacao-pos-migracao
menu-code: OT
description: Otimização e hypercare pós-migração com métricas e alertas.
---

# Otimização e Hypercare Pós-Migração

Definir e executar o plano de estabilização, monitoramento e otimização após a conclusão da migração Azure DevOps.

## 1. Plano de Hypercare

### Definição do Período

Calibrar conforme complexidade da migração:

| Complexidade | Período Hypercare | Cobertura |
|-------------|-------------------|-----------|
| BAIXA | 1 semana | Horário comercial |
| MÉDIA | 2 semanas | Horário comercial + plantão |
| ALTA | 3-4 semanas | Horário estendido + plantão |
| ENTERPRISE | 4-8 semanas | 24/7 na primeira semana, depois horário estendido |

### Responsáveis

Definir claramente:

- **Owner do hypercare:** quem coordena
- **Ponto focal por componente:** Boards, Repos, Pipelines, Integrações
- **Escalation path:** para quem escalar se o ponto focal não resolver
- **Contato de rollback:** quem autoriza rollback se necessário

## 2. Métricas de Sucesso

### Métricas Operacionais

- **Pipeline success rate:** % de pipelines executando com sucesso vs origem (antes da migração)
- **Build time comparison:** tempo médio de build destino vs origem
- **Deployment frequency:** frequência de deploys mantida ou melhorada
- **Integration uptime:** integrações (hooks, webhooks, connectors) funcionando sem falha

### Métricas de Adoção

- **Developer adoption:** % de devs usando o novo org/projeto
- **Remote switch completion:** % de devs que atualizaram remotes
- **Work item usage:** times criando/atualizando work items no destino
- **Query/Dashboard usage:** stakeholders usando dashboards no destino

### Métricas de Qualidade

- **Data integrity:** amostragem de work items/repos para confirmar integridade
- **Permission accuracy:** zero incidentes de acesso indevido ou bloqueio indevido
- **Zero data loss:** nenhum artefato reportado como perdido

## 3. Alertas Mínimos

Configurar monitoramento para:

- [ ] Pipeline failure rate > threshold (ex: >10% em 24h)
- [ ] Integration failures (service hooks retornando erro)
- [ ] Authentication errors (PAT expirado, permissões revogadas)
- [ ] Agent pool offline
- [ ] Build queue time > threshold

### Canais de Alerta

- Teams/Slack channel dedicado ao hypercare
- Email para incidentes críticos
- Dashboard de status (Azure DevOps ou externo)

## 4. Logs Críticos para Monitorar

- **Pipeline logs:** falhas, warnings, referências quebradas
- **Audit logs:** mudanças de permissão, acessos incomuns
- **Integration logs:** disparos de hooks, respostas de endpoints
- **Authentication logs:** falhas de auth, tokens expirados
- **Agent logs:** conectividade, capacidade, falhas

## 5. Plano de Resposta a Incidentes

### Classificação

| Severidade | Critério | SLA Resposta | SLA Resolução |
|-----------|----------|-------------|---------------|
| **P1 - Crítico** | Pipeline de produção bloqueada, data loss, security breach | 15 min | 2h |
| **P2 - Alto** | Pipeline não-prod falhando, integração down, permissões erradas | 1h | 8h |
| **P3 - Médio** | Work items com dados incorretos, dashboard quebrado | 4h | 24h |
| **P4 - Baixo** | Cosmético, queries a ajustar, docs a atualizar | 24h | 72h |

### Fluxo de Resposta

1. **Detectar** — alerta automático ou report de usuário
2. **Classificar** — severidade P1-P4
3. **Comunicar** — notificar stakeholders conforme severidade
4. **Diagnosticar** — usar capability [DG] Diagnóstico
5. **Resolver** — aplicar fix ou workaround
6. **Validar** — confirmar resolução com evidência
7. **Documentar** — registrar no Dossiê + lessons learned

## 6. Otimizações Pós-Estabilização

Após o período de hypercare, sugerir:

- **Pipelines:** otimização de tempo de build, paralelização, caching
- **Branch policies:** refinamento baseado no uso real
- **Permissões:** revisão e tightening (remover acessos temporários da migração)
- **Integrações:** health check e cleanup de hooks desnecessários
- **Dashboards:** criação/atualização com métricas do novo ambiente
- **Documentação:** atualização de runbooks, wikis, onboarding com novos URLs/processos
- **Descomissionamento:** plano para desativar org/projeto origem (com aprovação)

## 7. Critérios de Encerramento do Hypercare

O hypercare é encerrado quando:

- [ ] Todas as métricas de sucesso atingidas por N dias consecutivos
- [ ] Zero P1/P2 abertos
- [ ] Todos os devs migraram remotes
- [ ] Integrações estáveis por período definido
- [ ] Stakeholders aprovam encerramento
- [ ] Org/projeto origem com plano de descomissionamento definido

## Entregável

- Plano de hypercare com responsáveis e SLAs
- Dashboard de métricas (ou template)
- Lista de alertas configurados
- Plano de resposta a incidentes
- Checklist de encerramento
- Dossiê atualizado
