---
name: arquitetura-dados
description: Arquitetura de dados — DW, Lakehouse, modelagem dimensional
menu-code: AD
---

**Language:** Use `{communication_language}` for all output.

# Arquitetura de Dados

Projete arquiteturas de dados corporativas: Data Warehouse, Lakehouse, modelagem dimensional e plataformas analíticas modernas.

## Escopo

- **Data Warehouse:** Kimball, Star Schema, Snowflake Schema, SCD (Type 1/2/3), Data Marts, camada semântica
- **Lakehouse:** Arquitetura Medallion (Bronze/Silver/Gold), Delta Lake, Iceberg, unified analytics
- **Modelagem:** Dimensional (fatos e dimensões), relacional (3NF), Data Vault 2.0, One Big Table
- **Plataformas:** Microsoft Fabric, Databricks, Snowflake, Synapse, Redshift

## Processo

Ao receber um pedido de arquitetura de dados:

### NÍVEL 1 — Arquitetura

1. **Entender o contexto** — Qual o caso de uso? (BI, ML, operational analytics, real-time)
2. **Identificar fontes** — De onde vêm os dados? (OLTP, APIs, files, streaming)
3. **Definir volumes** — Qual o volume esperado? (GB, TB, PB)
4. **Definir latência** — Batch, micro-batch, near real-time, real-time?
5. **Escolher abordagem:**

| Abordagem | Quando Usar | Trade-off |
|---|---|---|
| Data Warehouse (Kimball) | BI clássico, dados estruturados, SLA rígido | Performance excelente, flexibilidade limitada |
| Lakehouse (Medallion) | Dados variados, ML + BI, cost-effective | Flexível, governança requer mais cuidado |
| Data Vault 2.0 | Auditoria, múltiplas fontes, enterprise DW | Resiliente a mudanças, mais complexo |
| Hybrid (DW + Lakehouse) | Enterprise com múltiplos casos de uso | Melhor dos dois mundos, mais componentes |

### NÍVEL 2 — Modelagem

1. **Identificar processos de negócio** (grão, fatos, dimensões)
2. **Definir Bus Matrix** (conformed dimensions)
3. **Modelar Star Schema** com:
   - Tabelas fato (métricas, grão definido)
   - Tabelas dimensão (atributos descritivos, SKs)
   - SCD strategy por dimensão
4. **Definir camadas:**
   - **Bronze/Raw:** Dados brutos, schema-on-read
   - **Silver/Cleansed:** Dados limpos, tipados, deduplicados
   - **Gold/Curated:** Modelos dimensionais, agregações, data marts

### NÍVEL 3 — Implementação

1. **Código DDL** (SQL) para tabelas, schemas, partições
2. **Pipelines de carga** (ELT/ETL) com transformações
3. **Testes de qualidade** (dbt tests, Great Expectations)
4. **Documentação** do modelo (dbt docs, data dictionary)

### NÍVEL 4 — Operação

1. **Monitoramento** de freshness, volume, qualidade
2. **Performance** — particionamento, clustering, indexação
3. **Governança** — catálogo, lineage, ownership

## Progressão

- **NÍVEL 1 → 2:** Após confirmar a abordagem arquitetural com o usuário, prosseguir para modelagem
- **NÍVEL 2 → 3:** Após o usuário aprovar o modelo dimensional, prosseguir para implementação
- **NÍVEL 3 → 4:** Após entregar código DDL e pipeline, perguntar se deseja configurar operação
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Diagrama da arquitetura (mermaid ou ASCII)
- DDL das tabelas principais
- Pipeline de exemplo
- Trade-offs entre alternativas
- Recomendação fundamentada
