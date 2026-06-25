# Checklist Pre-Submissao Coupa — BAT DevSecOps

**Prazo:** 08/06/2026
**Plataforma:** Coupa (BAT procurement)
**Responsavel:** Alessandro Lyra

---

## Proposta Tecnica

### Estrutura e Formato
- [ ] Executive Summary adicionado (Secao 0) com problema, solucao, valor, investimento e timeline
- [ ] Emojis removidos de todos os headers
- [ ] Diagramas Mermaid substituidos por imagens PNG ou tabelas descritivas
- [ ] Callouts `> [!NOTE]` e `> [!IMPORTANT]` substituidos por blockquotes padrao
- [ ] Tabela de 15 itens agrupada por fase para facilitar leitura
- [ ] Secao de Equipe expandida (perfis, experiencia, certificacoes)
- [ ] Secao "Proximos Passos" com CTA e contatos adicionada ao final
- [ ] Numero de referencia e controle de versao no cabecalho
- [ ] Documento exportado para PDF e validado visualmente

### Conteudo Tecnico — Decisoes Resolvidas
- [ ] Container Apps definido como plataforma de compute (AKS como evolucao documentada)
- [ ] Playwright definido como framework E2E (Cypress como fallback)
- [ ] Blue-Green definido como estrategia de deploy PRD (Canary como evolucao)
- [ ] Observabilidade hibrida: OTel SDK + Azure Monitor + Grafana
- [ ] Cada "ou" resolvido com recomendacao primaria e justificativa

### Governanca e Compliance
- [ ] Risk Matrix (5x5) com minimo 5 riscos incluida
- [ ] RACI Matrix (Foursys / BAT LATAM / COE Global) incluida
- [ ] SLAs de RFC definidos com buffer de contingencia
- [ ] Categorizacao de mudancas (Standard / Normal / Emergency) documentada
- [ ] Rollback strategy para PRD com SLA < 10 minutos documentado

### Arquitetura e Infraestrutura
- [ ] Networking incluido: VNet, subnets, Private Endpoints, NSGs, DNS privado
- [ ] Zone-redundant definido para AKS/Container Apps, PostgreSQL e Redis
- [ ] API Gateway (APIM) incluido na arquitetura
- [ ] Circuit Breaker (Resilience4j) mencionado para Salesforce/SAP
- [ ] Azure Service Bus para integracoes assincronas
- [ ] Managed Identity para Key Vault, ACR e Service Connections
- [ ] RTO/RPO definidos por tier de criticidade
- [ ] SLOs concretos definidos (ex: 99.9% uptime, p99 < 500ms)
- [ ] SLA composto calculado e documentado

### Pipeline e Qualidade
- [ ] Quality Gate Matrix completa (merge / UAT / REG / PRD)
- [ ] Integration tests adicionados a piramide (Testcontainers)
- [ ] Database migration strategy incluida (Flyway/Liquibase)
- [ ] Artifact promotion (build once, deploy everywhere) documentado
- [ ] Smoke tests pos-deploy incluidos no pipeline
- [ ] SCA para dependencias Java especificado (OWASP Dependency Check)
- [ ] Ferramenta de secrets detection definida (Gitleaks)
- [ ] DAST com ferramenta e ambiente definidos (OWASP ZAP em UAT)
- [ ] Performance tests declarados como "fora de escopo" ou incluidos na Frente B

### Integracao
- [ ] Tipos de API Salesforce especificados (REST/Bulk/Streaming)
- [ ] Tipos de API SAP especificados (OData/RFC/IDoc)
- [ ] Autenticacao detalhada (OAuth2, certificados, Key Vault)
- [ ] Estrategia de mocks definida (WireMock + OpenAPI)
- [ ] Comunicacao inter-microservicos documentada
- [ ] Discovery de integracao incluido na Fase 1

### Premissas e Dependencias
- [ ] Secao de premissas adicionada (acessos BAT, SPOC, ambiente provisionado, licencas)
- [ ] Fase 0 (Pre-requisitos BAT) com checklist incluida
- [ ] Clausula de impedimentos por dependencias externas
- [ ] Dependencias mapeadas explicitamente (COE, infra BAT, licencas)

---

## Proposta Comercial

### Estrutura
- [ ] Executive Summary adicionado
- [ ] Emojis removidos
- [ ] Callouts GitHub substituidos
- [ ] Referencia cruzada com proposta tecnica
- [ ] Exportado para PDF e validado

### Conteudo Comercial
- [ ] Estimativa de horas revisada (220h → ajustada ou exclusoes declaradas)
- [ ] Fase 6 (Handover) expandida para 30-40h
- [ ] Projecao TCO de 6-12 meses incluida
- [ ] Cenarios otimista/realista/pessimista para Frente B
- [ ] Tabela com valores para horario comercial E fora do horario
- [ ] R$ 12.000 de replicacao classificado formalmente ("Frente A — Extensao")
- [ ] Criterios de aceite ("Definicao de Pronto") para Frente A
- [ ] Clausula de impedimentos e re-estimativa
- [ ] Clausula de reajuste apos 90 dias de validade

---

## Validacao Final

- [ ] Ambos os documentos revisados por pelo menos 2 pessoas
- [ ] PDF gerado e testado em diferentes leitores
- [ ] Nomes e dados do cliente conferidos
- [ ] Data e versao atualizadas
- [ ] Upload no Coupa testado (tamanho, formato)
- [ ] Copia de backup salva

---

*Checklist gerado pela Squad MEQ em 02/06/2026.*
