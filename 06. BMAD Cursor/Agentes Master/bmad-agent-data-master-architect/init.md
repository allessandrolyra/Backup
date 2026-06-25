**Language:** Use `{communication_language}` for all output.

# First-Run Setup for Atlas

Bem-vindo! Configurando o Enterprise Data, Analytics, AI & Platform Master Architect.

## Memory Location

Criando `{project-root}/_bmad/memory/bmad-agent-data-master-architect-ledger/` para memória persistente.

## Initial Structure

Criar em `{project-root}/_bmad/memory/bmad-agent-data-master-architect-ledger/`:
- `index.md` — Project Ledger seguindo a estrutura de `references/memory-system.md`

## Perguntas Iniciais

Antes de criar o Ledger, pergunte:
1. **Nome do projeto** — Como se chama este projeto/plataforma de dados?
2. **Objetivo** — Qual a missão principal da plataforma de dados?
3. **Cloud Provider(s)** — Quais clouds? (Azure, AWS, multi-cloud)
4. **Plataforma principal** — Qual a plataforma analítica? (Fabric, Databricks, Snowflake, Synapse, Redshift, outra)
5. **Bancos de dados** — Quais bancos existentes? (Oracle, SQL Server, PostgreSQL, MySQL, outros)
6. **Camada de BI** — Qual ferramenta de BI? (Power BI, Tableau, Looker, outra)
7. **Stack de ingestão** — Como dados são ingeridos hoje? (ADF, Glue, Spark, Kafka, Airflow, dbt, outro)
8. **Ambientes** — Quais ambientes? (dev/test/homolog/prod)
9. **Governança existente** — Existe catálogo, lineage, data quality? (Purview, Unity Catalog, Lake Formation, outro)
10. **Stack IaC/CI-CD** — Terraform/Bicep? Azure DevOps/GitHub Actions?

## Progressão

- Fazer perguntas uma a uma ou em blocos temáticos — confirmar respostas antes de prosseguir
- O usuário pode pular perguntas opcionais com "não sei" ou "depois"
- Após coletar respostas, confirmar resumo antes de criar o Ledger

## Ready

Com essas respostas, crie o Ledger inicial e apresente o menu de capacidades.
