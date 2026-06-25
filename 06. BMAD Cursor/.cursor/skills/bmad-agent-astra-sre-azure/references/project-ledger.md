# Project Memory Ledger (Astra Azure)

Este ledger é a base da continuidade para projetos Azure. Ele deve ser atualizado sempre que um novo artefato for gerado ou uma decisão técnica for tomada.

## Estrutura do Ledger
O arquivo localizado em `{project-root}/_bmad/memory/bmad-agent-astra-sre-azure-ledger/index.md` deve seguir esta estrutura:

### A) Contexto do Projeto
- Nome, Objetivo, Stakeholders.
- Tenant, Subscription(s), Management Groups, Resource Groups.
- Regiões/AZ, Ambientes (dev/stg/prod).

### B) Decisões (com data)
- Registro histórico de escolhas arquiteturais e técnicas.
- Formato: Data | Decisão | Motivo | Trade-off aceito.

### C) Workloads & Stack
- Workloads: AKS, App Service, SQL, Functions, etc.
- Stack IaC: Terraform ou Bicep.
- Stack CI/CD: Azure DevOps ou GitHub Actions.

### D) Observabilidade & SRE
- Monitor, Log Analytics, App Insights configurados.
- SLOs/SLIs definidos.
- Error Budget policy.

### E) DR & Backup
- RTO/RPO por workload.
- Estratégia de failover (ASR, Geo-replication).
- Último teste de DR.

### F) FinOps
- Tags obrigatórias configuradas.
- Budgets e alertas ativos.
- Reservas/Savings Plans.

### G) Artefatos Gerados
- Lista de arquivos, módulos e links gerados por sessão.

### H) Pendências & Riscos
- Próximas ações priorizadas.
- Riscos mapeados com mitigação.
- Assunções feitas por falta de informação.

---

## Instruções para o Agente
1. **Leitura:** Sempre leia o Ledger ao iniciar a sessão.
2. **Identificação:** Se não existe projeto ativo, pergunte antes de criar um novo.
3. **Atualização:** Após qualquer entrega ou decisão, resuma a atualização do Ledger.
4. **Mudança de Contexto:** Se o usuário mudar um requisito, registre como "Decisão Alterada" com trade-offs.
5. **Formato de Update:** Sempre mostrar o diff (antes → depois) ao atualizar o Ledger.
