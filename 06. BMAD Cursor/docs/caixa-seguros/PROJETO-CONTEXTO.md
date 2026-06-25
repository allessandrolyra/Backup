# Caixa Seguros - Contexto do Projeto

> **Ultima atualizacao:** 06/05/2026
> **Status:** Discovery concluido - Dimensionamento em andamento

---

## Cliente

- **Nome:** Caixa Seguros
- **Segmento:** Seguros
- **Contato principal:** A definir

---

## Ordens de Servico Ativas

### OS-001: Mapeamento de Arquitetura Corporativa e Rastreabilidade ALM

- **Diretorio:** `os-archimate-alm/`
- **Status:** Entendimento inicial concluido, pendente reuniao com cliente
- **Metodologia:** TOGAF Standard, 10th Edition
- **Modelagem:** ArchiMate 3.2
- **Ferramentas:** Archi (Git-based), Azure DevOps, Neo4j
- **Tipo de trabalho:** 100% off-site (remoto)
- **Pagamento:** Por entrega aceita

#### Resumo da OS

O cliente quer criar um "Gemeo Digital" da arquitetura corporativa - um mapa completo e interativo que mostre como todos os sistemas, processos de negocio e tecnologias se conectam. O foco e em objetos logicos (nao infraestrutura fisica/CMDB) com rastreabilidade total ate o ciclo de desenvolvimento (ALM) no Azure DevOps.

#### Os 4 Pilares

1. **Modelagem** - Arquitetura em 3 camadas ArchiMate (Negocio, Aplicacao, Tecnologia)
2. **Versionamento** - Git-based via Archi Collaboration Plugin
3. **Rastreabilidade ALM** - Vinculo Work Items + Repos do Azure DevOps ao modelo
4. **Analise de Impacto** - Neo4j para consultas de dependencia e impacto

#### Entregaveis

| # | Entregavel | Status |
|---|-----------|--------|
| E1 | Repositorio Git com modelo ArchiMate completo | Pendente |
| E2 | Scripts de Ingestao Cypher + Pipeline Azure DevOps | Pendente |
| E3 | Matriz de Rastreabilidade Dinamica | Pendente |
| E4 | Manual de Taxonomia | Pendente |

#### Cronograma Revisado (pos-Discovery 06/05/2026)

**Premissas de volume:**
- 40 aplicacoes, 1.300 APIs, 70 integracoes batch (sem mensageria)
- 20-30 departamentos, ~500 pessoas, capabilities only (sem BPMN)
- Documentacao parcial existente (Archi, Visio, CMDB SharePoint)
- Neo4j a provisionar (container Azure)
- Pipelines ADO: responsabilidade Caixa Consorcio (Foursys entrega scripts/specs)

| Fase | Atividade | Horas Arq. | Horas Sr. | Duracao | Entregavel |
|------|-----------|-----------|----------|---------|------------|
| F0 | Setup Ambiente (Archi repo, Git, Neo4j container, taxonomia) | 24 | 16 | 1 sem | Ambiente operacional + Manual Taxonomia (draft) |
| F1 | Camada de Negocio — Capabilities Map (20-30 deptos) | 40 | 24 | 2 sem | Modelo ArchiMate: Business Layer |
| F2 | Camada de Aplicacao — 40 apps + 1.300 APIs + 70 batch | 80 | 60 | 3-4 sem | Modelo ArchiMate: Application Layer + interfaces |
| F3 | Camada de Tecnologia — Runtime Azure (servicos logicos) | 40 | 32 | 2 sem | Modelo ArchiMate: Technology Layer |
| F4 | Vinculacao Azure DevOps — Work Items, Repos, IDs ArchiMate | 24 | 40 | 2 sem | Rastreabilidade ALM configurada |
| F5 | Neo4j Ingestao + Queries de Impacto | 32 | 40 | 2 sem | Scripts Cypher + spec de pipeline (exec: Caixa) |
| F6 | Consolidacao + Manual de Taxonomia final | 16 | 16 | 1 sem | E1 + E4 finalizados |
| F7 | Transferencia de Conhecimento | 16 | 8 | 1 sem | Workshop + documentacao |
| | **TOTAL** | **272** | **236** | **14-16 sem** | |

**Total geral estimado: 508 horas** (272h Arquiteto + 236h Desenvolvedor Senior)

> **Nota:** A fase F2 e a mais critica — 1.300 APIs exigem classificacao, agrupamento e validacao.
> Recomenda-se apoio de automacao (scripts de importacao do CMDB/SharePoint e Archi existente).

#### Cronograma Anterior (referencia pre-discovery)

| Fase | Atividade | Duracao | Status |
|------|-----------|---------|--------|
| F0 | Setup Ambiente (Archi, Git, Neo4j) | 1-2 sem | Pendente |
| F1 | Camada de Negocio | 2-3 sem | Pendente |
| F2 | Camada de Aplicacao | 3-4 sem | Pendente |
| F3 | Camada de Tecnologia | 2-3 sem | Pendente |
| F4 | Vinculacao Azure DevOps | 2-3 sem | Pendente |
| F5 | Pipeline Neo4j + Queries | 2-3 sem | Pendente |
| F6 | Consolidacao + Manual | 1-2 sem | Pendente |
| F7 | Transferencia Conhecimento | 1 sem | Pendente |

**Prazo total anterior:** 12 a 16 semanas

#### Prazos Contratuais

- Resposta a cotacao: 5 dias uteis apos recebimento
- Inicio do servico: 10 dias apos OS aceita e assinada

#### Respostas do Discovery (06/05/2026)

| # | Pergunta | Resposta |
|---|----------|----------|
| 1 | Quantos sistemas/aplicacoes no portfolio? | **~40 aplicacoes** |
| 2 | Quantas integracoes (APIs, batch, mensageria)? | **~1.300 APIs**, **~70 integracoes por arquivo (batch)**. Nao existe mensageria. |
| 3 | Existe documentacao de arquitetura atual? | Sim — documentacao basica no **Archi**, desenhos de solucao no **Visio**, mapeamentos parciais |
| 4 | Quantos repositorios no Azure Repos? Work Items ativos? | Work items antigos **fora do escopo**. Repos nao quantificados. |
| 5 | Quantas organizacoes ADO? Projetos? | **1 organizacao**, **~20 projetos**. Em processo de migracao. |
| 6 | Quantas areas de negocio/departamentos? | Ideal descer ate nivel de coordenacao. **~500 pessoas** (terceiros + funcionarios). Estimativa: **20 a 30 departamentos**. |
| 7 | Macroprocessos/processos de negocio? BPMN? | **Nao e necessario** mapeamento de processos negociais. Somente **capabilities do negocio**. |
| 8 | Existe CMDB? Qual ferramenta? | Sim — **CMDB no SharePoint** |
| 9 | Nivel de nos logicos esperado? | **Servicos de runtime**, principalmente os do **Azure** (ex.: AKS, Service Bus, SQL MI) |
| 10 | Limite inferior de detalhe de infra? | Nao fazer CMDB. Ex.: mapear "roda em AKS" sim, "qual node pool" nao. Nao vincular app a servidor fisico. |
| 11 | Neo4j ja existe? | **Nao existe**. Sera provisionado no **Azure como container**. |
| 12 | Azure DevOps: estrutura de Work Item Types? | Diversos projetos em 1 org. Campos, work items e fluxos **customizados** dentro da ferramenta. |
| 13 | Acesso para criar pipelines no ADO? | **Nao**. Construcao de pipelines e responsabilidade da **Caixa Consorcio**. |

#### Informacoes Ainda Pendentes

- [ ] Quem sao os pontos focais por area/departamento?
- [ ] Quem mantera o modelo apos entrega?
- [ ] Lista/inventario das 40 aplicacoes (nomes, responsaveis)
- [ ] Acesso ao CMDB do SharePoint (leitura)
- [ ] Acesso ao Archi e Visio existentes (importacao)

#### Riscos Atualizados

1. **Volume de integracoes muito alto** — 1.300 APIs + 70 batch e um inventario massivo; risco de subestimar esforco de mapeamento
2. **Indisponibilidade de pontos focais** — 20-30 departamentos exigem coordenacao com multiplos interlocutores
3. **Qualidade da documentacao existente** — Archi e Visio existem mas nivel de completude e desconhecido
4. **Pipelines fora do nosso controle** — Caixa Consorcio constroi as pipelines; dependencia de terceiro para integracao Neo4j
5. **ADO em migracao** — Estrutura de projetos/org ainda instavel, com customizacoes em work items
6. **Neo4j precisa ser provisionado** — Dependencia de setup de infra (container no Azure) antes da fase de ingestao
7. **CMDB no SharePoint** — Qualidade e formato dos dados pode exigir ETL significativo

---

## Documentos Gerados

| Data | Documento | Caminho | Descricao |
|------|-----------|---------|-----------|
| 08/04/2026 | Entendimento OS ArchiMate | `os-archimate-alm/entendimento-os-archimate-alm.docx` | Documento completo de entendimento com escopo, perguntas, riscos e cronograma |

---

## Historico de Interacoes

| Data | Tipo | Resumo |
|------|------|--------|
| 08/04/2026 | Analise interna | Recebimento e analise da OS. Criacao do documento de entendimento. Estruturacao do diretorio do projeto. |
| 06/05/2026 | Discovery (respostas cliente) | Respostas de dimensionamento recebidas: 40 apps, 1300 APIs, 70 batch, 20-30 deptos, capabilities only, Neo4j a provisionar, pipelines com Caixa. |

---

## Proximos Passos

1. ~~Agendar reuniao de esclarecimento com o cliente~~ ✅
2. ~~Obter respostas das perguntas criticas de dimensionamento~~ ✅
3. **IMEDIATO** — Elaborar estimativa de horas por perfil (usando tabela contratual)
4. Montar cronograma detalhado de entregas
5. Formalizar e enviar proposta/cotacao (**URGENTE — cliente cobrando hoje 06/05**)
