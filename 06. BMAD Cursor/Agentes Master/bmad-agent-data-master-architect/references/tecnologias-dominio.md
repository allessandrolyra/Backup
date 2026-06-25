# Tecnologias de Domínio Obrigatório

Referência rápida das tecnologias que Atlas domina e deve considerar em toda recomendação.

## Microsoft
| Tecnologia | Uso Principal |
|---|---|
| Microsoft Fabric | Plataforma analítica unificada (OneLake, Warehouse, Lakehouse, Notebooks, Pipelines) |
| OneLake | Data Lake unificado do Fabric |
| Power BI | BI, dashboards, Semantic Model, DAX, RLS, DirectQuery, Composite Models |
| Azure Data Factory | Orquestração e ingestão (ETL/ELT) |
| Synapse Analytics | Data Warehouse serverless e Spark pools |
| Azure SQL | Banco relacional gerenciado |
| Azure OpenAI | LLMs, embeddings, GPT, DALL-E |
| Azure AI Foundry | Plataforma de IA (ex-AI Studio) |
| Purview | Governança — Data Catalog, Lineage, Classification, Data Quality |
| Azure Monitor | Observabilidade — métricas, logs, alertas, KQL |

## AWS
| Tecnologia | Uso Principal |
|---|---|
| AWS Glue | ETL serverless, Spark, catálogo |
| Redshift | Data Warehouse |
| Athena | Query engine serverless sobre S3 |
| Lake Formation | Governança de Data Lake |
| EMR | Spark/Hadoop gerenciado |
| S3 | Object storage |
| CloudWatch | Monitoramento e logs |
| IAM | Identity and Access Management |

## Databricks
| Tecnologia | Uso Principal |
|---|---|
| Unity Catalog | Governança unificada — catálogo, lineage, access control |
| Delta Lake | Storage layer ACID sobre data lake |
| Delta Live Tables | Pipelines declarativos com qualidade |
| Workflows | Orquestração de jobs |
| Mosaic AI | Plataforma de IA/ML |
| MLflow | Tracking, registry, deployment de ML |

## Snowflake
| Tecnologia | Uso Principal |
|---|---|
| Snowpark | Desenvolvimento em Python/Java/Scala |
| Cortex | IA/ML nativo (LLMs, functions) |
| Dynamic Tables | Materialização incremental declarativa |
| Tasks | Agendamento de jobs |
| Streams | CDC nativo |
| Native Apps | Apps distribuíveis no marketplace |

## Open Source
| Tecnologia | Uso Principal |
|---|---|
| Apache Spark | Processamento distribuído (batch e streaming) |
| Airflow | Orquestração de workflows |
| dbt | Transformação SQL-first com testes e docs |
| Kafka | Streaming de eventos |
| Flink | Stream processing |
| Iceberg | Table format open (alternativa a Delta) |
| Trino | Query engine federado |
| Hive | Metastore e query engine |
| OpenTelemetry | Observabilidade (traces, metrics, logs) |
| Prometheus | Monitoramento e alertas |
| Grafana | Dashboards e visualização |

## Bancos de Dados
| Tecnologia | Uso Principal |
|---|---|
| Oracle | Enterprise RDBMS, RAC, Data Guard, Exadata |
| SQL Server | RDBMS Microsoft, Always On, SSIS/SSAS/SSRS |
| PostgreSQL | Open source RDBMS avançado |
| MySQL | Open source RDBMS |
| MariaDB | Fork MySQL otimizado |

## Frameworks de IA
| Framework | Uso Principal |
|---|---|
| LangChain | Orquestração de LLMs, chains, tools |
| LangGraph | Agentic workflows com estado |
| Semantic Kernel | SDK Microsoft para IA (plugins, planners) |
| AutoGen | Multi-agent conversations |

## Fontes Prioritárias (Ordem Obrigatória)
1. Azure Architecture Center
2. AWS Well-Architected Framework
3. Documentação Oficial Microsoft
4. Documentação Oficial AWS
5. Documentação Oficial Databricks
6. Documentação Oficial Snowflake
7. Documentação Oficial dbt
8. Documentação Oficial Apache Foundation
