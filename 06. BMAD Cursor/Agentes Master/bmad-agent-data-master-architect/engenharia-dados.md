---
name: engenharia-dados
description: Engenharia de dados — ETL/ELT, pipelines, Spark, dbt, ADF, Glue, CDC
menu-code: ED
---

**Language:** Use `{communication_language}` for all output.

# Engenharia de Dados

Projete e implemente pipelines de dados, ingestão, transformação e orquestração para plataformas analíticas modernas.

## Escopo

- **Ingestão:** Batch, streaming, CDC, APIs, file-based, database replication
- **Transformação:** SQL-first (dbt), Spark (PySpark/Scala), Pandas, stored procedures
- **Orquestração:** Airflow, ADF, Databricks Workflows, Glue, Fabric Pipelines
- **Streaming:** Kafka, Event Hubs, Kinesis, Flink, Spark Structured Streaming
- **CDC:** Debezium, Oracle GoldenGate, SQL Server CDC, Snowflake Streams, Delta Live Tables

## Processo

Ao receber um pedido de engenharia de dados:

### NÍVEL 1 — Arquitetura do Pipeline

1. **Identificar fontes e destinos** — Origem → Transformação → Destino
2. **Definir padrão:** ETL vs ELT vs streaming
3. **Definir frequência:** Batch (diário/horário), micro-batch, real-time
4. **Definir SLA:** Freshness, completude, latência máxima
5. **Escolher stack:**

| Stack | Quando Usar | Trade-off |
|---|---|---|
| dbt + Airflow | SQL-first, ELT moderno, testabilidade | Excelente para transformação, limitado para ingestão complexa |
| Spark (Databricks/EMR) | Big data, transformações complexas, ML | Poderoso e flexível, curva de aprendizado |
| ADF + Fabric | Ecossistema Microsoft, low-code, ingestão | Integrado, menos flexível para lógica complexa |
| Glue | Ecossistema AWS, serverless, custo variável | Serverless, cold start, debugging mais difícil |

### NÍVEL 2 — Implementação

1. **Pipeline de ingestão** — Código completo (ADF JSON, Airflow DAG, dbt model)
2. **Transformações** — SQL/Spark com lógica de negócio
3. **Qualidade de dados** — Testes inline (dbt tests, assertions, data contracts)
4. **Idempotência** — Garantir re-executabilidade sem duplicação
5. **Error handling** — Dead letter queues, retry policies, alertas

### NÍVEL 3 — Automação

1. **CI/CD** — Pipeline de deploy (dbt build, Spark job deploy, ADF ARM export)
2. **Testes automatizados** — Unit tests, integration tests, data tests
3. **Parametrização** — Ambientes (dev/test/prod), variáveis, secrets

### NÍVEL 4 — Operação

1. **Monitoramento** — Execução, duração, volumes, erros
2. **Alertas** — Falha, atraso, anomalia de volume
3. **Troubleshooting** — Logs, Spark UI, query plans, bottleneck analysis
4. **Otimização** — Particionamento, caching, broadcast joins, file compaction

## Progressão

- **NÍVEL 1 → 2:** Após confirmar a arquitetura do pipeline e stack com o usuário, prosseguir para implementação
- **NÍVEL 2 → 3:** Após entregar o pipeline funcional, perguntar se deseja configurar CI/CD e testes
- **NÍVEL 3 → 4:** Após automação configurada, perguntar se deseja configurar operação e monitoramento
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Diagrama do pipeline (mermaid ou ASCII)
- Código completo e funcional
- Testes de qualidade
- Configuração de monitoramento
