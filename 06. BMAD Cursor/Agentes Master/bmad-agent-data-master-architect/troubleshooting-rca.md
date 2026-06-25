---
name: troubleshooting-rca
description: Troubleshooting & RCA — diagnóstico, root cause, correção, prevenção
menu-code: TR
---

**Language:** Use `{communication_language}` for all output.

# Troubleshooting & Root Cause Analysis

Diagnostique e resolva problemas complexos em plataformas de dados: erros, lentidão, falhas de pipeline, problemas de performance e incidentes.

## Escopo

- **Plataformas:** Databricks, Snowflake, Fabric, Synapse, ADF, Glue, Power BI, Airflow, dbt
- **Categorias:** Rede, identidade/IAM, storage, banco de dados, SQL, Spark, pipelines, catálogo, BI
- **Tipos:** Erros de execução, lentidão, timeout, OOM, data skew, connectivity, permissão, configuração

## Processo — 5 Fases

### FASE 1 — Coleta

Identificar e solicitar ao usuário:

| Informação | Por que é necessária |
|---|---|
| Mensagem de erro exata | Classificação do problema |
| Logs / stack trace | Causa técnica |
| Horário de ocorrência | Correlação com eventos |
| Workload afetado | Escopo do impacto |
| Ambiente (dev/prod) | Severidade e urgência |
| Mudanças recentes | Possível causa |
| Frequência | Intermitente vs constante |

### FASE 2 — Classificação

Determinar a categoria do problema:

| Categoria | Sinais Típicos |
|---|---|
| **Rede** | Timeout, connection refused, DNS resolution, private endpoint |
| **Identidade/IAM** | 401/403, permission denied, token expired, RBAC |
| **Storage** | Access denied, throttling, capacity, file not found |
| **Banco de dados** | Deadlock, blocking, slow query, tempdb, log full |
| **SQL** | Wrong results, performance, plan regression, statistics |
| **Spark** | OOM, data skew, shuffle, executor lost, stage failure |
| **Pipeline (ADF/Glue/Airflow)** | Activity failure, timeout, dependency, concurrency |
| **Power BI** | Refresh failure, DAX error, gateway, capacity |
| **Databricks** | Cluster startup, Unity Catalog, Delta, driver OOM |
| **Snowflake** | Warehouse suspend, credit spike, query profile |
| **Catálogo/Governança** | Scan failure, lineage break, classification error |

### FASE 3 — Root Cause Analysis (RCA)

Separar camadas de causa:

| Camada | Definição | Exemplo |
|---|---|---|
| **Sintoma** | O que o usuário observa | "O dashboard não atualiza" |
| **Causa Imediata** | O que falhou tecnicamente | "O refresh do dataset falhou com timeout" |
| **Causa Técnica** | Por que falhou | "Query no source demora 45min por falta de índice" |
| **Causa Sistêmica** | Por que isso podia acontecer | "Sem monitoramento de query duration no source" |

Técnicas de RCA:
- **5 Whys** — Perguntar "por quê?" iterativamente
- **Fishbone (Ishikawa)** — Categorizar causas por tipo
- **Timeline analysis** — Correlacionar eventos com horário
- **Change analysis** — O que mudou antes do problema?

### FASE 4 — Correção

Entregar em 3 níveis:

1. **Mitigação imediata** — Resolver o sintoma agora (workaround, restart, rollback)
2. **Correção definitiva** — Resolver a causa técnica (fix, patch, config change)
3. **Correção sistêmica** — Resolver a causa raiz (monitoramento, automação, design change)

Incluir para cada correção:
- Comandos/código exatos
- Validação (como confirmar que funcionou)
- Rollback (como reverter se piorar)

### FASE 5 — Prevenção

1. **Alertas** — Configurar alertas para detectar antes que impacte
2. **Monitoramento** — Adicionar métricas e dashboards
3. **Automação** — Runbooks, auto-remediation
4. **Controles** — Políticas, guardrails, gates
5. **Documentação** — Registrar no knowledge base / Ledger

## Progressão

- **FASE 1 → 2:** Após coletar informações do erro com o usuário, prosseguir para classificação
- **FASE 2 → 3:** Após classificar a categoria, prosseguir para RCA detalhado
- **FASE 3 → 4:** Após confirmar a causa raiz com o usuário, prosseguir para correção
- **FASE 4 → 5:** Após aplicar correção, perguntar se deseja configurar prevenção
- **Urgência:** Se o usuário indicar urgência, entregar mitigação imediata (FASE 4) antes de completar RCA (FASE 3)

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Formato específico para troubleshooting:
1. **Classificação:** Categoria e severidade
2. **RCA:** Sintoma → Causa Imediata → Causa Técnica → Causa Sistêmica
3. **Mitigação:** Ação imediata com comandos
4. **Correção:** Fix definitivo com código
5. **Prevenção:** Alertas e controles
6. **Próximos Passos (1-2-3)**
