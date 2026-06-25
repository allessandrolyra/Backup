# Checklist de Discovery - PoC K6 Performance

## Objetivo
Listar tudo o que precisa ser confirmado com a Zurich antes de iniciar a configuracao da PoC de K6, para evitar bloqueios e retrabalho.

---

## 1. Aplicacao piloto e ambiente-alvo

- [ ] Qual aplicacao ou API sera usada como alvo dos testes de performance?
- [ ] Existe ambiente de homologacao ou staging disponivel para receber carga?
- [ ] A aplicacao piloto e acessivel via rede privada ou publica?
- [ ] Existe restricao de horario ou janela para execucao de carga?

## 2. Acessos de rede e autenticacao

- [ ] Quais portas, protocolos e endpoints serao utilizados?
- [ ] A comunicacao passa por VPN, VNET peering ou acesso direto?
- [ ] Existe firewall ou WAF no caminho que precisa de liberacao?
- [ ] A API exige autenticacao? Se sim, qual tipo (token, OAuth, API key, certificado)?
- [ ] Ha segredos ou credenciais que precisam ser provisionados no Key Vault?

## 3. APIs e endpoints do piloto

- [ ] Quais endpoints serao testados inicialmente?
- [ ] Existem endpoints criticos que nao devem receber carga (ex: pagamento, integracao externa)?
- [ ] A documentacao da API (Swagger, Postman collection) esta disponivel?
- [ ] Qual volumetria real de usuarios/chamadas a API recebe hoje?

## 4. Thresholds e expectativas

- [ ] Qual tempo de resposta e considerado aceitavel (p95, p99)?
- [ ] Qual taxa de erro e toleravel sob carga?
- [ ] Quantos usuarios virtuais simultaneos o piloto deve simular?
- [ ] Existe baseline de performance anterior para comparacao?

## 5. Infraestrutura e permissoes Azure

- [ ] A Foursys tera acesso ao Resource Group ou Subscription para provisionamento?
- [ ] Existe padrao de naming convention, tags ou RBAC a ser seguido?
- [ ] A VM do K6 sera provisionada pela Foursys ou pela Zurich?
- [ ] O Self-hosted Agent Pool sera criado pela Foursys ou aproveitado do existente?
- [ ] Existe restricao de regiao Azure ou imagem base de VM?

## 6. Esteira e pipeline

- [ ] A pipeline de performance sera um pipeline separado ou um stage no pipeline existente?
- [ ] Quem tera permissao para disparar execucoes manuais?
- [ ] Onde os resultados devem ser publicados (pipeline artifacts, storage, dashboard)?
- [ ] Ha integracao desejada com o SonarQube para quality gate de performance?

## 7. Governanca e autonomia

- [ ] Quem sera o ponto focal tecnico na Zurich para o discovery?
- [ ] Existe padrao corporativo de scripts ou nomenclatura de testes?
- [ ] A Zurich quer modelo de repositorio padrao para scripts K6?
- [ ] Quem operara o ambiente apos a entrega da PoC?

## 8. Visualizacao e resultados

- [ ] Onde a Zurich prefere ver os resultados: pipeline, portal Azure, dashboards ou todos?
- [ ] Existe ferramenta de BI ou observabilidade ja em uso para consolidar metricas?
- [ ] E necessario exportar resultados em formato especifico (CSV, JSON, HTML)?

---

## Proximo passo
Agendar sessao de discovery com ponto focal tecnico da Zurich para validar cada item antes do inicio da configuracao.
