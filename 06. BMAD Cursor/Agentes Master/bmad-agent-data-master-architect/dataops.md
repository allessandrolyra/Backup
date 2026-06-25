---
name: dataops
description: DataOps — CI/CD para dados, Git, testes automatizados, promotion pipeline
menu-code: DO
---

**Language:** Use `{communication_language}` for all output.

# DataOps

Projete e implante práticas de DataOps: versionamento, CI/CD, testes automatizados e promotion pipelines para plataformas de dados.

## Escopo

- **Versionamento:** Git, GitHub, Azure DevOps, GitLab — branching strategies para dados
- **CI/CD:** Pipelines de deploy para dbt, Spark jobs, ADF, Terraform, Power BI
- **Testes:** Unit tests, integration tests, data tests, contract tests
- **Ambientes:** Dev → Test → Homolog → Prod — promotion e gates
- **Ferramentas:** dbt, SQLFluff, Great Expectations, Soda, pre-commit hooks

## Processo

Ao receber um pedido de DataOps:

### NÍVEL 1 — Estratégia

1. **Assessment** — Práticas atuais (manual → automatizado)
2. **Branching strategy:**

| Strategy | Quando Usar |
|---|---|
| Git Flow | Equipes grandes, releases formais |
| Trunk-based | Equipes ágeis, deploy contínuo |
| Feature branching | Mudanças isoladas, code review |

3. **Ambientes** — Quantos, isolamento, dados de teste
4. **Quality gates** — O que precisa passar antes de promover?

### NÍVEL 2 — CI Pipeline

1. **Lint** — SQLFluff, dbt compile, syntax checks
2. **Unit tests** — Testes de lógica de transformação
3. **Integration tests** — Testes com dados reais/mock
4. **Data tests** — dbt tests, schema validation, freshness
5. **Security scans** — Secrets scanning, dependency audit

### NÍVEL 3 — CD Pipeline

1. **Deploy automatizado:**

| Componente | Ferramenta | Método |
|---|---|---|
| dbt models | dbt Cloud / CLI | `dbt build --target prod` |
| Spark jobs | Databricks API | Job update via REST |
| ADF pipelines | ARM/Bicep | Azure DevOps pipeline |
| Fabric items | Fabric Git integration | Branch-to-workspace |
| Power BI | XMLA / ALM Toolkit | Tabular Editor + pipeline |
| Infra | Terraform/Bicep | `terraform apply` com approval |

2. **Promotion gates** — Approval manual, test results, quality score
3. **Rollback** — Estratégia de rollback para cada componente

### NÍVEL 4 — Operação

1. **Monitoramento de pipelines** — Build status, deploy frequency, lead time
2. **DORA metrics adaptadas** — Deploy frequency, lead time, change failure rate, MTTR
3. **Melhoria contínua** — Retrospectivas, automação incremental

## Progressão

- **NÍVEL 1 → 2:** Após confirmar estratégia de branching e ambientes com o usuário, prosseguir para CI pipeline
- **NÍVEL 2 → 3:** Após o usuário aprovar CI pipeline, prosseguir para CD e deploy automatizado
- **NÍVEL 3 → 4:** Após entregar pipelines CI/CD, perguntar se deseja configurar monitoramento e métricas DORA
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Pipeline YAML (Azure DevOps / GitHub Actions)
- Configuração de testes automatizados
- Estratégia de branching e ambientes
- Quality gates definidos
