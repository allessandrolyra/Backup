# Estimativa de Dimensionamento — Mapeamento/Assessment
# Caixa Seguros — OS-001: Arquitetura Corporativa ArchiMate + ALM

> **Data:** 06/05/2026
> **Versao:** 1.0
> **Elaborado por:** Alessandro Lyra — Arquiteto de Solucoes

---

## 1. Volumetria Confirmada (Discovery 06/05/2026)

| Dimensao | Volume | Impacto |
|----------|--------|---------|
| Aplicacoes no portfolio | ~40 | Base do mapeamento Application Layer |
| APIs (integracoes REST/SOAP) | ~1.300 | **Principal driver de esforco** — classificacao, agrupamento, vinculacao |
| Integracoes por arquivo (batch/SFTP) | ~70 | Mapeamento de fluxos de dados |
| Mensageria | 0 | Reduz complexidade de Technology Layer |
| Departamentos/areas | 20-30 | Capabilities map, stakeholders |
| Pessoas (terceiros + funcionarios) | ~500 | Contexto organizacional, nao mapeamento individual |
| Organizacoes ADO | 1 | Simplifica vinculacao |
| Projetos ADO | ~20 | Em migracao — risco de instabilidade |
| Documentacao existente | Archi (basico) + Visio + CMDB SharePoint | Acelera coleta, mas qualidade desconhecida |

---

## 2. Premissas de Estimativa

1. **Capabilities only** — sem mapeamento BPMN/processos de negocio (reduz F1 significativamente)
2. **Nos logicos de runtime Azure** — mapear servicos (AKS, SQL MI, Service Bus etc.), nao infra fisica
3. **Sem CMDB fisico** — nao vincular app a servidor/VM especifico
4. **Pipelines ADO sao responsabilidade da Caixa Consorcio** — Foursys entrega scripts e especificacoes
5. **Neo4j sera provisionado como container no Azure** — setup incluso em F0
6. **Documentacao existente pode ser importada** — economia estimada de 15-20% nas fases F1-F3
7. **Trabalho 100% remoto** — sem deslocamento, reunioes por Teams
8. **1 semana = 40h** para calculo de duracao

---

## 3. Estimativa por Fase

### F0 — Setup de Ambiente (1 semana)

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Criar repositorio Git + estrutura Archi Collaboration | Arquiteto | 8 |
| Provisionar Neo4j container no Azure (ACR + ACI ou AKS) | Arquiteto | 8 |
| Definir taxonomia ArchiMate (categorias, naming conventions) | Arquiteto | 8 |
| Importar modelo Archi existente do cliente | Dev Senior | 8 |
| Configurar ambiente dev local + CI basico | Dev Senior | 8 |
| **Subtotal F0** | | **40h** |

### F1 — Camada de Negocio: Capabilities Map (2 semanas)

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Levantamento de capabilities com stakeholders (20-30 deptos) | Arquiteto | 24 |
| Modelagem ArchiMate Business Layer (capabilities, atores, parceiros) | Arquiteto | 16 |
| Validacao com pontos focais | Dev Senior | 16 |
| Documentacao e versionamento | Dev Senior | 8 |
| **Subtotal F1** | | **64h** |

> **Nota:** Sem BPMN, o esforco se concentra em capabilities e organizational structure.
> Estimativa considera ~2 reunioes de 1h por departamento (agrupando areas similares).

### F2 — Camada de Aplicacao: Apps + Integracoes (3-4 semanas)

Esta e a fase de **maior esforco e risco** do projeto.

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Importar dados do CMDB SharePoint (ETL/normalizacao) | Dev Senior | 24 |
| Importar/validar desenhos Visio existentes | Dev Senior | 16 |
| Mapear 40 aplicacoes (componentes, servicos, responsabilidades) | Arquiteto | 40 |
| Classificar e agrupar 1.300 APIs (por dominio/aplicacao) | Arquiteto | 24 |
| Mapear 70 integracoes batch (origem, destino, frequencia, formato) | Arquiteto | 16 |
| Modelagem ArchiMate Application Layer | Dev Senior | 20 |
| Validacao cruzada (modelo vs CMDB vs Visio) | Dev Senior | 16 |
| **Subtotal F2** | | **156h** |

> **Analise de risco:** 1.300 APIs e um volume expressivo.
> - Se existir inventario estruturado (planilha/CMDB com app + endpoint + metodo): estimativa se mantem
> - Se for necessario levantar APIs via entrevistas ou scan de codigo: adicionar **40-60h**
> - Recomendacao: solicitar export do CMDB SharePoint antes de iniciar F2

### F3 — Camada de Tecnologia: Runtime Azure (2 semanas)

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Levantar servicos Azure em uso (AKS, App Service, SQL MI, Storage etc.) | Arquiteto | 24 |
| Modelar nos logicos ArchiMate Technology Layer | Arquiteto | 16 |
| Vincular Technology -> Application (hosting, data flow) | Dev Senior | 24 |
| Validacao com time de infra/cloud | Dev Senior | 8 |
| **Subtotal F3** | | **72h** |

### F4 — Vinculacao Azure DevOps (2 semanas)

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Mapear estrutura ADO (20 projetos, WI types customizados) | Arquiteto | 16 |
| Definir convencao de vinculacao (ID ArchiMate <-> Work Item/Repo) | Arquiteto | 8 |
| Implementar vinculacao nos objetos existentes | Dev Senior | 32 |
| Validar rastreabilidade bidirecional | Dev Senior | 8 |
| **Subtotal F4** | | **64h** |

> **Restricao:** Pipelines sao da Caixa Consorcio.
> Foursys entrega: scripts + documentacao de spec da pipeline (trigger Git -> Neo4j).

### F5 — Neo4j: Ingestao e Queries de Impacto (2 semanas)

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Modelar schema de grafo (nodes, relationships, properties) | Arquiteto | 16 |
| Desenvolver scripts Cypher de ingestao (Archi -> Neo4j) | Dev Senior | 24 |
| Criar queries de analise de impacto (API -> processos afetados) | Arquiteto | 16 |
| Dashboard de Coerencia (desenvolvimentos sombra, arquiteturas orfas) | Dev Senior | 16 |
| Documentar spec de pipeline para Caixa Consorcio executar | Dev Senior | 8 |
| **Subtotal F5** | | **80h** |

### F6 — Consolidacao + Manual de Taxonomia (1 semana)

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Revisao e consolidacao do modelo completo | Arquiteto | 16 |
| Manual de Taxonomia final (naming, categorias, regras de modelagem) | Dev Senior | 8 |
| Export Open Exchange Format XML | Dev Senior | 4 |
| **Subtotal F6** | | **28h** |

### F7 — Transferencia de Conhecimento (1 semana)

| Atividade | Perfil | Horas |
|-----------|--------|-------|
| Workshop presencial/remoto (modelo, Neo4j, governanca) | Arquiteto | 12 |
| Documentacao de operacao e manutencao | Dev Senior | 8 |
| Suporte pos-entrega (1 semana) | Arquiteto | 4 |
| **Subtotal F7** | | **24h** |

---

## 4. Resumo Consolidado

| Fase | Arquiteto (h) | Dev Senior (h) | Total (h) | Duracao |
|------|--------------|----------------|-----------|---------|
| F0 — Setup | 24 | 16 | 40 | 1 sem |
| F1 — Negocio | 40 | 24 | 64 | 2 sem |
| F2 — Aplicacao | 80 | 76 | 156 | 3-4 sem |
| F3 — Tecnologia | 40 | 32 | 72 | 2 sem |
| F4 — ADO | 24 | 40 | 64 | 2 sem |
| F5 — Neo4j | 32 | 48 | 80 | 2 sem |
| F6 — Consolidacao | 16 | 12 | 28 | 1 sem |
| F7 — Transferencia | 16 | 8 | 24 | 1 sem |
| **TOTAL** | **272** | **256** | **528** | **14-16 sem** |

### Por Perfil

| Perfil | Horas | % do total |
|--------|-------|------------|
| Arquiteto de Solucoes | 272h | 52% |
| Desenvolvedor Senior | 256h | 48% |
| **Total** | **528h** | 100% |

---

## 5. Faixa de Estimativa (3-point)

| Cenario | Horas | Premissa |
|---------|-------|----------|
| **Otimista** | 440h | Documentacao existente cobre 80%+ das apps, CMDB bem estruturado, stakeholders disponiveis |
| **Provavel** | 528h | Documentacao parcial, necessita validacao, stakeholders com disponibilidade moderada |
| **Pessimista** | 640h | CMDB desorganizado, APIs sem inventario, necessidade de entrevistas extensas, ADO instavel |

---

## 6. Fatores que Podem Alterar a Estimativa

| Fator | Impacto se positivo | Impacto se negativo |
|-------|---------------------|---------------------|
| Qualidade do CMDB SharePoint | -40h (importacao direta) | +60h (ETL manual) |
| Inventario de APIs estruturado | -30h | +50h (levantamento manual) |
| Modelo Archi existente completo | -50h (reuso) | +0h (ja considerado parcial) |
| Disponibilidade de stakeholders | -20h (reunioes eficientes) | +40h (reagendamentos, atrasos) |
| Estabilidade do ADO em migracao | 0h | +30h (retrabalho de vinculacao) |

---

## 7. Entregaveis por Fase

| Entregavel OS | Fase(s) | Descricao |
|---------------|---------|-----------|
| E1 — Repositorio Git ArchiMate | F0-F6 | Modelo completo 3 camadas + versionamento |
| E2 — Scripts Cypher + Spec Pipeline | F5 | Scripts de ingestao + doc para Caixa construir pipeline |
| E3 — Matriz Rastreabilidade Dinamica | F4-F5 | ArchiMate <-> ADO <-> Neo4j |
| E4 — Manual de Taxonomia | F0 (draft) + F6 (final) | Naming, categorias, regras de modelagem |

---

## 8. Recomendacoes

1. **Solicitar export do CMDB SharePoint antes de F2** — determina se o volume de APIs e tratavel por importacao ou exige levantamento manual
2. **Alinhar com Caixa Consorcio sobre pipeline ADO** — Foursys entrega spec, Caixa executa; precisa de ponto focal tecnico do lado deles
3. **Provisionar Neo4j em F0** — nao deixar para depois; bloqueia F5 se atrasado
4. **Considerar automacao de importacao** — com 1.300 APIs, scripts de ETL (CMDB -> Archi / Archi -> Neo4j) sao essenciais, nao opcionais
5. **Validar o modelo Archi existente** — antes de iniciar F1, importar e avaliar cobertura real
