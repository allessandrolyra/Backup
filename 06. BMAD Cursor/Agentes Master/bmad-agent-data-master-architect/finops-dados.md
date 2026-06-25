---
name: finops-dados
description: FinOps — custos de compute/storage/rede, KPIs, otimização, autoscaling
menu-code: FO
---

**Language:** Use `{communication_language}` for all output.

# FinOps para Dados

Avalie, otimize e governe custos de plataformas de dados, analytics e IA.

## Escopo

- **Custos:** Compute, storage, rede, consultas, refresh, ingestão, egress
- **KPIs:** Custo por TB, custo por consulta, custo por pipeline, custo por usuário
- **Otimizações:** Compression, clustering, particionamento, autoscaling, auto-stop, rightsizing
- **Ferramentas:** Azure Cost Management, AWS Cost Explorer, Databricks Account Console, Snowflake Resource Monitors

## Processo

Ao receber um pedido de FinOps:

### NÍVEL 1 — Assessment de Custos

1. **Inventário de recursos** — Listar todos os recursos com custo
2. **Classificação por driver:**

| Driver | Exemplos |
|---|---|
| Compute | Spark clusters, Synapse DWUs, Snowflake credits, Fabric CUs |
| Storage | S3, ADLS, Delta tables, snapshots, backups |
| Rede | Egress, cross-region, VPN, Private Endpoints |
| Queries | Serverless queries (Athena, Synapse serverless), on-demand |
| Refresh | Power BI refresh, materialized views, incremental refresh |

3. **Tagging** — Verificar e recomendar tags obrigatórias (cost-center, environment, team, project)
4. **Baseline** — Estabelecer custo mensal atual por componente

### NÍVEL 2 — Otimizações

| Otimização | Impacto | Complexidade |
|---|---|---|
| Compression (Parquet, Delta) | 50-80% menos storage | Baixa |
| Particionamento | Menos dados escaneados | Média |
| Clustering/Z-Ordering | Queries mais rápidas, menos compute | Média |
| Autoscaling | Compute sob demanda | Média |
| Auto-stop/pause | Zero custo quando ocioso | Baixa |
| Rightsizing | Dimensionar para uso real | Média |
| Reserved capacity | 30-60% menos que on-demand | Commitment |
| Incremental refresh | Processar apenas delta | Média |
| Query optimization | Menos recursos por query | Alta |
| Data lifecycle | Archive/delete dados antigos | Média |

### NÍVEL 3 — Automação

1. **Budgets e alertas** — Alertas automáticos por threshold
2. **Auto-stop policies** — Parar recursos ociosos automaticamente
3. **Rightsizing automation** — Recomendações periódicas baseadas em uso
4. **Cost anomaly detection** — Alertas de gastos anormais

### NÍVEL 4 — Governança de Custos

1. **Chargeback/Showback** — Atribuição de custos por time/projeto
2. **Governance policies** — Limites de cluster, quotas, aprovações
3. **Reviews** — Revisão mensal de custos com stakeholders
4. **Forecast** — Projeção de custos com crescimento

## Progressão

- **NÍVEL 1 → 2:** Após confirmar inventário e baseline de custos com o usuário, prosseguir para otimizações
- **NÍVEL 2 → 3:** Após o usuário aprovar otimizações prioritárias, prosseguir para automação
- **NÍVEL 3 → 4:** Após entregar automação de budgets, perguntar se deseja configurar governança de custos
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Assessment de custos com breakdown
- Top otimizações com impacto estimado
- Configuração de budgets e alertas
- KPIs de FinOps recomendados
