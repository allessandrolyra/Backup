---
name: migracao-dados
description: Migração de dados — cloud migration, modernização, re-architecture
menu-code: MD
---

**Language:** Use `{communication_language}` for all output.

# Migração de Dados

Planeje e execute migrações de plataformas de dados para cloud, modernização de ambientes legados e re-arquitetura de soluções analíticas.

## Escopo

- **Estratégias:** Lift-and-Shift, Re-platform, Re-architecture, Replace, Hybrid
- **Origens:** Oracle DW, SQL Server DW, Teradata, Netezza, on-premises Hadoop, SSIS/SSAS/SSRS
- **Destinos:** Microsoft Fabric, Databricks, Snowflake, Synapse, Redshift, BigQuery
- **Ferramentas:** Azure Database Migration Service, AWS DMS, Databricks migration tools, dbt
- **Componentes:** Schema migration, data migration, ETL/ELT migration, report migration, security migration

## Processo

Ao receber um pedido de migração:

### FASE 1 — Assessment

1. **Inventário** — Catalogar todos os objetos (tabelas, views, procedures, jobs, reports)
2. **Dependências** — Mapear dependências entre objetos e sistemas
3. **Volumes** — Tamanho de dados, crescimento, picos
4. **Complexidade** — Classificar objetos por complexidade de migração
5. **Escolher estratégia:**

| Estratégia | Quando Usar | Trade-off |
|---|---|---|
| Lift-and-Shift | Prazo curto, compatibilidade alta | Rápido, não moderniza |
| Re-platform | Aproveitar managed services, mudanças mínimas | Balanço entre velocidade e modernização |
| Re-architecture | Redesenho completo, lakehouse moderno | Melhor resultado, mais tempo e risco |
| Hybrid | Coexistência durante transição | Flexível, complexidade operacional |

### FASE 2 — Planejamento

1. **Waves** — Dividir migração em ondas ordenadas por dependência e risco
2. **Mapeamento** — Origem → Destino para cada objeto
3. **Conversão** — SQL dialect, procedures, functions, types
4. **Testing strategy** — Data validation, reconciliation, performance benchmarks
5. **Rollback plan** — Para cada wave

### FASE 3 — Execução

1. **Schema migration** — DDL convertido e validado
2. **Data migration** — Full load + incremental CDC
3. **ETL/ELT migration** — Pipelines reescritos ou convertidos
4. **Report migration** — Dashboards e reports recriados
5. **Security migration** — Roles, permissions, RLS

### FASE 4 — Validação e Cutover

1. **Data reconciliation** — Contagem de registros, checksums, amostragem
2. **Performance testing** — Benchmarks comparativos (antes vs depois)
3. **UAT** — Validação por usuários de negócio
4. **Cutover plan** — Sequência, horário, comunicação, rollback
5. **Decommission** — Desligamento da origem após período de coexistência

## Progressão

- **FASE 1 → 2:** Após confirmar inventário e estratégia de migração com o usuário, prosseguir para planejamento
- **FASE 2 → 3:** Após o usuário aprovar plano de waves e mapeamento, prosseguir para execução
- **FASE 3 → 4:** Após entregar scripts de migração, prosseguir para validação e cutover
- **A qualquer momento:** O usuário pode solicitar apenas uma fase específica — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Assessment com inventário e complexidade
- Plano de waves com timeline
- Scripts de migração e conversão
- Plano de validação e rollback
