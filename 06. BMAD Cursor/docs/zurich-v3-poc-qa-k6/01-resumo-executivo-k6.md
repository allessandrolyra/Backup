# Zurich - PoC QA Performance com K6

## Objetivo
Entregar uma infraestrutura pequena e iterativa para testes de performance com `K6`, integrada ao ecossistema atual da Zurich, permitindo execucao manual e automatizada e deixando a operacao pronta para autonomia futura do cliente.

## Posicionamento da PoC
Esta PoC nao substitui o `Selenium Grid`. Ela cria uma segunda trilha de `QA`, focada em `performance`, enquanto o `Selenium` continua cobrindo testes funcionais e E2E.

## O que a PoC valida
- integracao do `K6` com a esteira existente no `Azure DevOps`
- execucao manual por disparo controlado
- execucao automatizada pela pipeline
- acesso seguro a aplicacoes e APIs da Zurich
- armazenamento de evidencias e resultados
- monitoracao basica e leitura operacional

## Desenho de alto nivel
1. O time de QA cria e versiona scripts `K6`.
2. A execucao pode ser iniciada manualmente ou pela pipeline do `Azure DevOps`.
3. Um `Self-hosted Agent` preparado para performance aciona a execucao.
4. A `VM K6 Executor` roda os cenarios de carga contra a aplicacao piloto.
5. Logs, relatorios e artefatos sao enviados para `Storage Account`.
6. Telemetria e status operacional sao acompanhados em `Azure Monitor` e `Log Analytics`.
7. A Zurich passa a ter uma base pronta para evoluir thresholds, quality gate e capacidade.

## Servicos principais da solucao
- `Azure DevOps`: orquestra pipeline, agenda execucoes e publica artefatos.
- `Self-hosted Agent Pool`: garante ambiente controlado, rede privada e dependencias fixas.
- `VM K6 Executor`: executa os testes de performance.
- `Azure Key Vault`: guarda segredos, tokens e configuracoes sensiveis.
- `Storage Account`: armazena relatorios, logs e saidas da execucao.
- `Azure Monitor`: acompanha eventos, saude e metricas operacionais.
- `Log Analytics Workspace`: centraliza consultas e troubleshooting das execucoes.
- `VNet / NSG / Private Access`: protege a comunicacao com o ambiente alvo.

## Beneficio para a Zurich
O cliente recebe uma base de `performance testing` integrada ao fluxo atual, sem depender da Foursys para cada nova rodada. A PoC entrega a fundacao tecnica, os padroes e a integracao para que o proprio time Zurich execute e evolua seus testes depois.

## Premissas iniciais da PoC
- `1 VM` de execucao de `K6` e suficiente para a prova inicial
- foco em poucas APIs ou jornadas criticas
- execucao em ambiente controlado, preferencialmente nao produtivo
- thresholds e volumetria serao refinados com a aplicacao piloto

## Decisoes arquiteturais
- Nao acoplar `K6` ao `Selenium Grid`, porque os objetivos e a infraestrutura operacional sao diferentes.
- Reaproveitar o mesmo padrao de `Self-hosted Agents`, seguranca e observabilidade ja proposto para QA funcional.
- Comecar com `VM` simples na PoC e evoluir para multiplos executores ou escala horizontal apenas se os volumes justificarem.
- Posicionar `K6` como acelerador do `quality gate` de performance, mas sem tornar isso obrigatorio no primeiro ciclo.

## Evolucao natural apos a PoC
- adicionar mais cenarios de carga e estresse
- ampliar o numero de executores `K6`
- transformar thresholds em `quality gate`
- separar dashboards executivos e operacionais
- consolidar uma esteira completa de `QA funcional + QA performance`
