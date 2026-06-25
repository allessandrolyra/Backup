# Zurich

## Objetivo

Esta pasta concentra assuntos, projetos, reunioes, arquitetura, propostas e referencias relacionadas ao cliente `Zurich`.

## Estrutura

- `reunioes/` - atas, pautas, roteiros e preparacao
- `projetos/` - iniciativas, pilotos e frentes em andamento
- `arquitetura/` - desenhos, decisoes, hipoteses e documentacao tecnica
- `propostas/` - materiais comerciais e modulares
- `referencias/` - materiais de apoio, links, insumos e anexos

## Contexto Atual

Tema atual em acompanhamento:

- estrategia da Foursys para implantacao de `Selenium Grid` na Zurich
- integracao com a esteira de `CI/CD` no `Azure DevOps`
- estruturacao de testes de `performance` com foco em `k6`
- visao de `dashboards` para acompanhamento dos resultados

## Sistemas Citados

- `Motor TIA` - front-end em `Angular` e backend em `.NET`
- `Sinistros` - sistema legado em `ASP.NET`

## Contexto Tecnologico

- transicao de modelos `IaaS` para `SaaS` na Azure
- stack com `.NET 4.7`, `.NET 4.8` e `.NET Core 10`
- uso de `xUnit` e `nUnit` para testes unitarios
- `Selenium` homologado globalmente pela Zurich

## Prioridades Mapeadas

1. Montagem, configuracao e sustentacao do ambiente `Selenium Grid` integrado ao `Azure DevOps`
2. Estrategia e execucao de testes de performance e carga com foco em `k6`
3. Implementacao dos aceleradores Foursys com IA para automacao Selenium
4. Modelo de sustentacao e manutencao continua da automacao

## Contribuicao Arquitetural Esperada

Como apoio de arquitetura cloud Azure, os principais pontos de contribuicao sao:

- desenho da arquitetura alvo para o `Selenium Grid`
- definicao da integracao com `Azure DevOps` e esteiras de qualidade
- estrategia de observabilidade, logs, evidencias e dashboards
- apoio na estrategia de testes de performance
- avaliacao de operacao, sustentacao, seguranca e custo

## Hipotese Inicial de Solucao

Hipotese inicial discutida:

- `Azure DevOps` como orquestrador da esteira
- `AKS` como plataforma para o `Selenium Grid`
- `ACR` para imagens dos nodes e componentes
- `Key Vault` para segredos e configuracoes sensiveis
- `Azure Monitor` e `Log Analytics` para observabilidade
- `Storage` ou artefatos de pipeline para relatorios, screenshots e evidencias

## Artefatos Criados

- diagrama inicial da solucao: `docs/selenium-grid-azure.drawio`

## Pendencias Para Proximas Conversas

- validar se a arquitetura em `AKS` e aderente ao contexto da Zurich
- entender restricoes de rede, seguranca, proxies e conectividade
- confirmar volume esperado de execucoes paralelas
- mapear navegadores, versoes e ambientes suportados
- definir como sera a sustentacao da plataforma
- entender requisitos de dashboard tecnico e executivo

## Proximos Passos Sugeridos

1. Registrar a ata detalhada em `reunioes/`
2. Criar uma visao de arquitetura inicial em `arquitetura/`
3. Estruturar a proposta modular em `propostas/`
4. Registrar perguntas de descoberta para a proxima reuniao
