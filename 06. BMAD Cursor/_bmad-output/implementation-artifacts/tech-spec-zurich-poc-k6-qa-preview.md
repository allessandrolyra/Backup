---
status: in-progress
execution_mode: one-shot
baseline_commit: NO_VCS
created_at: 2026-03-30
---

# Zurich PoC K6 QA Preview

## Objetivo
Criar uma nova versao separada da PoC para detalhar a arquitetura de `QA Performance` com `K6`, sem alterar os arquivos anteriores da linha de `Selenium Grid`.

## Premissas da PoC
- A PoC continua pequena, iterativa e orientada a infraestrutura e integracao
- A Zurich ja possui `Azure DevOps` e `SonarQube`
- A PoC deve permitir execucao `manual` e `automatizada`
- O foco e entregar a base para que a Zurich rode seus proprios testes depois
- A trilha de `K6` complementa a trilha de `Selenium Grid`, mas nao substitui a automacao funcional

## Entregaveis
- `docs/zurich-v3-poc-qa-k6/01-resumo-executivo-k6.md`
- `docs/zurich-v3-poc-qa-k6/02-servicos-arquitetura-k6.md`
- `docs/zurich-v3-poc-qa-k6/zurich-poc-k6-executivo.drawio`
- `docs/zurich-v3-poc-qa-k6/zurich-poc-k6-infra-icons.drawio`
