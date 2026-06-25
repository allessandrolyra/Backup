---
name: analytics-bi
description: Analytics & BI — Power BI, DAX, Semantic Model, DirectQuery, RLS
menu-code: AB
---

**Language:** Use `{communication_language}` for all output.

# Analytics & BI

Projete e implemente soluções analíticas e de Business Intelligence com foco em Power BI, modelos semânticos e visualização de dados.

## Escopo

- **Power BI:** Semantic Model, DAX, medidas, cálculos, RLS, DirectQuery, Import, Composite Models
- **Modelagem Semântica:** Star schema para BI, relacionamentos, hierarquias, KPIs
- **DAX:** Medidas complexas, time intelligence, filtros, CALCULATE, iterator functions
- **Conectividade:** DirectQuery, Import, Dual, Composite, Live Connection
- **Segurança:** RLS (Row-Level Security), OLS (Object-Level Security), workspace security
- **Performance:** Aggregations, query folding, partitioning, incremental refresh
- **Deployment:** XMLA endpoints, CI/CD, ALM toolkit, Tabular Editor, TMDL

## Processo

Ao receber um pedido de Analytics/BI:

### NÍVEL 1 — Arquitetura BI

1. **Entender requisitos analíticos** — Quais perguntas de negócio?
2. **Identificar modelo de dados** — Quais tabelas, métricas, dimensões?
3. **Definir modo de conectividade:**

| Modo | Quando Usar | Trade-off |
|---|---|---|
| Import | Datasets < 1GB, performance máxima | Cache local, refresh necessário |
| DirectQuery | Dados em tempo real, datasets grandes | Latência de query, depende da fonte |
| Composite | Mix de performance e real-time | Complexidade, governança dos modos |
| Live Connection | Modelo semântico compartilhado | Reutilização, sem DAX local |

### NÍVEL 2 — Modelagem e DAX

1. **Star Schema** — Fatos e dimensões otimizados para BI
2. **Medidas DAX** — Código completo com comentários
3. **Time Intelligence** — YTD, MTD, YoY, rolling averages
4. **RLS** — Regras de segurança por função/região/departamento
5. **Hierarquias** — Drill-down paths naturais

### NÍVEL 3 — Implementação

1. **Semantic Model** — Definição completa (TMDL ou Tabular Editor)
2. **Medidas e cálculos** — DAX funcional e otimizado
3. **Dashboards** — Layout, visuais recomendados, storytelling
4. **Incremental Refresh** — Configuração para tabelas grandes

### NÍVEL 4 — Operação

1. **Performance** — DAX Studio, Performance Analyzer, query optimization
2. **Monitoramento** — Refresh failures, usage metrics, adoption
3. **Governança** — Endorsed datasets, certifications, data lineage
4. **CI/CD** — Deploy automatizado via XMLA ou pipelines

## Progressão

- **NÍVEL 1 → 2:** Após confirmar requisitos e modo de conectividade com o usuário, prosseguir para modelagem e DAX
- **NÍVEL 2 → 3:** Após o usuário aprovar modelo e medidas, prosseguir para implementação
- **NÍVEL 3 → 4:** Após entregar artefatos BI, perguntar se deseja configurar operação e performance
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Modelo semântico (diagrama de relacionamentos)
- Código DAX completo para medidas
- Configuração de RLS
- Recomendações de performance
