# Preparacao - Reuniao Comercial Zurich

## Tema

Preparacao para reuniao sobre a iniciativa de `Selenium Grid`, `Azure DevOps`, testes de `performance` e sustentacao da automacao.

## Objetivo

Entrar na reuniao com clareza sobre:

- como arquitetura Azure pode apoiar a iniciativa
- quais perguntas precisam ser respondidas
- quais riscos devem ser observados
- qual hipotese inicial de solucao pode ser apresentada

## Pontos-Chave

- `Selenium Grid` como plataforma de execucao paralela de testes UI
- integracao com `Azure DevOps`
- `SonarQube` como parte da qualidade de codigo
- testes de performance com foco em `k6`
- dashboards para acompanhamento de execucao e qualidade

## Como O Arquiteto Pode Ajudar

- desenhar a arquitetura alvo no Azure
- avaliar opcao de `AKS` versus alternativas mais simples
- propor observabilidade, seguranca e governanca
- apoiar na definicao de sustentacao e operacao
- ajudar a modularizar a proposta tecnica

## Perguntas Importantes

- qual o objetivo real da POC?
- qual volume de execucoes paralelas e esperado?
- quais browsers e versoes sao obrigatorios?
- existem restricoes de rede, proxy, VPN ou acesso privado?
- ha preferencia por `AKS`, VMs ou outra plataforma?
- quem sustentara a plataforma apos a implantacao?
- quais dashboards e evidencias sao esperados?
- quais jornadas precisam de testes de performance?

## Hipotese Inicial

- `Azure DevOps` orquestra a esteira
- `AKS` hospeda o `Selenium Grid`
- `ACR` armazena imagens
- `Key Vault` protege segredos
- `Azure Monitor` e `Log Analytics` monitoram a solucao
- `Storage` ou artefatos da pipeline guardam evidencias

## Riscos

- subdimensionamento ou superdimensionamento do grid
- flakiness dos testes UI
- pipeline lenta demais
- falta de baseline de performance
- ausencia de modelo claro de sustentacao

## Referencia

- diagrama base: `docs/selenium-grid-azure.drawio`
