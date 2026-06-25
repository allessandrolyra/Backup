# Desenho Inicial da Solucao - Selenium Grid no Azure

## Objetivo
Disponibilizar uma cadeia `end-to-end` para automacao de testes da Zurich, cobrindo configuracao do ambiente, desenvolvimento e execucao das automacoes, integracao com `Azure DevOps`, armazenamento de evidencias, observabilidade e sustentacao operacional.

## Visao Executiva
A proposta considera uma plataforma de automacao hospedada no `Azure`, com execucao de testes `Selenium` em infraestrutura baseada em `VM dedicada` e `VM Scale Sets`, integrada a pipelines do `Azure DevOps`. O fluxo principal parte do time de QA, passa pela esteira de CI/CD, executa os testes no `Selenium Grid` e publica evidencias e dashboards para acompanhamento operacional.

Os servicos de suporte da plataforma incluem `Azure Container Registry` para imagens, `Key Vault` para segredos, `Azure Monitor` e `Log Analytics` para telemetria, `Storage Account` para evidencias e uma camada de alertas para sustentacao da operacao.

## Componentes Principais
- `Time QA / Desenvolvimento`: cria e mantém os scripts de automacao.
- `Azure DevOps Pipeline`: orquestra build, validacoes e disparo das execucoes.
- `Agent Pool / Runner`: camada logica que executa a pipeline e dispara os testes E2E.
- `VM ou VM Scale Set para Self-hosted Agents`: camada fisica onde os runners dedicados ficam hospedados.
- `Build + Quality Gate`: etapa de validacao antes da execucao automatizada.
- `VM dedicada para Selenium Grid Hub`: recebe e distribui as sessoes `Remote WebDriver`.
- `VM Scale Set para Browser Nodes`: executa os testes em `Chrome`, `Edge` e `Firefox` com escalabilidade horizontal.
- `Aplicacao Alvo`: ambiente de homologacao ou SaaS acessado pelos testes.
- `Publicacao de Evidencias`: consolida logs, screenshots e reports.
- `Dashboards e Alertas`: suportam sustentacao e tratamento de falhas.

## Componentes de Suporte Azure
- `Azure Container Registry (ACR)`
- `Azure Key Vault`
- `Azure Monitor`
- `Log Analytics Workspace`
- `Storage Account`
- `Alert Rules / Action Groups`
- `Ingress ou Internal Load Balancer`
- `VNET`, `Subnets`, `NSG`, `RBAC`, `Private Endpoints` e `DNS Privado`

## Decisao Arquitetural - Self-hosted Agent ou Agent Pool Dedicado
Recomenda-se o uso de `Self-hosted Azure DevOps Agent` ou de um `Agent Pool dedicado` para esta solucao, porque ele fecha melhor a camada de `runner/pipeline` entre o `Azure DevOps` e o ambiente de execucao dos testes.

Na pratica, esse agente e o componente que executa a pipeline, acessa os repositorios, prepara o ambiente, autentica nos servicos Azure, aciona o `Selenium Grid`, publica evidencias e interage com componentes internos da plataforma. No desenho de infraestrutura, essa camada deve aparecer explicitamente como `VM` ou `VM Scale Set`, que hospeda os `self-hosted agents` do pool dedicado.

### Por que isso e importante neste contexto
- `Conectividade controlada`: o agente pode ficar dentro da rede corporativa ou em rede integrada ao Azure, facilitando o acesso ao `Grid Hub`, `VM Scale Sets`, `Key Vault`, `Storage` e aplicacoes internas.
- `Mais seguranca`: reduz a necessidade de expor endpoints publicamente apenas para atender a execucao da pipeline.
- `Padrao operacional`: permite instalar dependencias especificas de execucao, como `JDK`, `Maven`, `Node`, `browsers`, `CLI do Azure` e bibliotecas exigidas pelo framework de automacao.
- `Previsibilidade`: evita variacoes de ambiente comuns em agentes compartilhados e melhora a repetibilidade das execucoes.
- `Governanca`: facilita separar pipelines de automacao, performance e sustentacao em pools diferentes, com controle de permissao e capacidade.
- `Escalabilidade`: permite crescer a capacidade de execucao conforme o volume de suites e o paralelismo esperado.

### Diferenca pratica
- `Microsoft-hosted agent`: e efemero e generico, bom para pipelines simples, mas menos aderente quando a execucao depende de rede privada, configuracoes especificas ou integracoes internas.
- `Self-hosted agent / Agent Pool dedicado`: e mais indicado quando a pipeline precisa acessar componentes privados, manter configuracao controlada e operar como parte da plataforma de testes.

### Recomendacao para a proposta
Para a Zurich, a recomendacao inicial e prever um `Agent Pool dedicado` para a esteira de automacao, com possibilidade de evolucao para multiplos agentes conforme a necessidade de paralelismo, segregacao de carga e sustentacao operacional.

## Decisao Arquitetural - Runtime Sem AKS
Como o cliente nao pode utilizar `AKS`, a recomendacao e substituir o runtime do `Selenium Grid` por uma arquitetura em `IaaS`, composta por:

- `1 VM dedicada para o Selenium Grid Hub`
- `1 VM Scale Set para Browser Nodes`
- `1 VM ou VM Scale Set para Self-hosted Agents`

Essa abordagem preserva o restante da arquitetura, incluindo `Azure DevOps`, `Key Vault`, `ACR`, `Monitor`, `Storage`, `Alertas` e a `rede privada`, com menor ruptura no desenho e melhor aderencia a uma restricao corporativa de plataforma.

### Por que essa alternativa e a melhor sem AKS
- `Escalabilidade real`: o `VM Scale Set` substitui a capacidade elastica que o cliente teria com cluster.
- `Aderencia a IaaS`: mantem a solucao em um modelo que costuma ser mais aceito quando Kubernetes nao e permitido.
- `Menor impacto no desenho atual`: os componentes de seguranca, observabilidade e esteira continuam validos.
- `Leitura comercial simples`: fica facil explicar a plataforma como `Hub em VM + Browser Nodes escalando em VMSS`.

### Trade-offs da alternativa com VMs escalaveis
- `Mais operacao de sistema operacional`: patching, hardening e manutencao de imagem base ficam mais relevantes.
- `Menos elasticidade nativa`: a escala existe, mas depende mais de regras do `VM Scale Set` e padronizacao operacional.
- `Mais cuidado com imagens e browsers`: drivers, versoes e configuracoes precisam ser controlados de forma mais disciplinada.
- `Alta disponibilidade do Hub`: precisa ser tratada como uma decisao especifica se o cliente exigir resiliencia maior.

## Fluxo Resumido
1. O time de QA versiona ou atualiza os scripts de automacao.
2. O `Azure DevOps` executa a pipeline em um `Agent Pool / Runner`.
3. A esteira realiza build e quality gate.
4. O runner dispara os testes no `Selenium Grid`, com `Hub` em `VM dedicada` e `Browser Nodes` em `VM Scale Set`.
5. Os `Browser Nodes` executam as jornadas contra a aplicacao alvo.
6. A pipeline publica evidencias, logs e relatórios.
7. A operacao acompanha dashboards, alertas e eventos de falha.

## Premissas Iniciais
- `Selenium` permanece como ferramenta homologada para automacao funcional.
- A esteira corporativa sera baseada em `Azure DevOps`.
- O ambiente Azure sera mantido em `IaaS`, sem dependencia de `AKS`.
- O acesso entre execucao e aplicacao alvo deve ocorrer de forma controlada.
- Evidencias e telemetria precisam ficar disponiveis para auditoria e suporte.

## Recomendacao de MVP
Como entrega inicial para proposta e validacao tecnica, recomenda-se um `MVP` com:
- pipeline integrada ao `Azure DevOps`
- `Selenium Grid Hub` em `VM dedicada`
- `Browser Nodes` em `VM Scale Set`
- execucao paralela com navegadores homologados
- armazenamento de evidencias
- monitoracao basica e alertas operacionais

## Evolucoes Sugeridas
- ampliar paralelismo por tipo de navegador ou suite
- endurecimento de seguranca com mais componentes privados
- dashboards executivos e operacionais separados
- esteira dedicada para performance com `JMeter`
