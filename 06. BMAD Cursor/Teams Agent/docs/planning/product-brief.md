# Product Brief — Teams Meeting Secretary Agent

> **Squad MEQ** | Product Developer: Paula  
> **Versão:** 1.0  
> **Data:** 08/06/2026  
> **Status:** Draft — Aguardando validação dos stakeholders

---

## 1. Visão do Produto

### O que é

O **Teams Meeting Secretary Agent** é um agente inteligente que participa de reuniões no Microsoft Teams como uma persona automatizada. Ao final de cada reunião, ele gera dois artefatos:

- **Ata de Reunião Estruturada** — com pauta, decisões tomadas, responsáveis designados e prazos acordados.
- **Resumo Executivo** — síntese dos pontos-chave discutidos, otimizada para leitura rápida por gestores e stakeholders.

### Problema que resolve

Reuniões são o principal mecanismo de alinhamento e decisão em organizações, mas sofrem de um problema crônico: **o que foi decidido se perde**. Atas manuais dependem de alguém dedicado a anotar, são subjetivas, incompletas e frequentemente nem são produzidas. Isso gera retrabalho, decisões esquecidas, falta de rastreabilidade e perda de accountability.

### Proposta de valor

> **"Nunca mais perca uma decisão de reunião."**

O agente elimina o trabalho manual de documentação, garante registro completo e padronizado de todas as reuniões, e entrega resultados instantaneamente no canal onde a equipe já trabalha — o Microsoft Teams.

---

## 2. Personas e Stakeholders

### Personas primárias (usuários diretos)

| Persona | Descrição | Necessidade principal |
|---|---|---|
| **Líder de Projeto / Scrum Master** | Conduz reuniões de status, planning e retrospectiva | Registro automático de decisões e action items com responsáveis e prazos |
| **Gestor / Diretor** | Participa de reuniões estratégicas e de governança | Resumo executivo rápido para acompanhamento sem assistir gravações |
| **Membro de Equipe** | Participa de reuniões técnicas e de alinhamento | Referência confiável sobre o que foi combinado, sem depender de memória |

### Personas secundárias (beneficiários indiretos)

| Persona | Descrição | Benefício |
|---|---|---|
| **Compliance / Auditoria** | Necessita de evidências documentais de decisões corporativas | Registro padronizado, datado e armazenado com rastreabilidade |
| **PMO** | Acompanha múltiplos projetos e decisões transversais | Visão consolidada das decisões de cada reunião sem participar de todas |
| **Novos membros da equipe** | Precisam de contexto sobre decisões passadas | Histórico acessível de atas e resumos para onboarding rápido |

### Stakeholders do projeto

| Stakeholder | Papel | Interesse |
|---|---|---|
| **Sponsor executivo** | Aprova investimento e prioridade | ROI em produtividade e compliance |
| **TI / Administrador do Tenant** | Concede permissões e configura o ambiente | Segurança, governança e impacto no tenant |
| **Segurança da Informação** | Valida conformidade com políticas de dados | Tratamento adequado de transcrições e dados sensíveis |

---

## 3. Problema a Resolver

### Situação atual (As-Is)

As organizações enfrentam um ciclo recorrente de perda de informação em reuniões:

1. **Reuniões sem registro formal** — A maioria das reuniões não gera ata. Quando gera, depende de alguém anotar manualmente, o que é subjetivo e incompleto.

2. **Decisões perdidas** — Sem documentação, decisões tomadas em reunião são esquecidas ou contestadas semanas depois. "Mas a gente tinha combinado diferente..." é uma frase comum.

3. **Falta de follow-up** — Action items e prazos combinados verbalmente se perdem. Não há mecanismo automático de rastreamento do que foi acordado.

4. **Tempo desperdiçado** — Quando alguém se dedica a produzir a ata, gasta de 30 a 60 minutos após cada reunião revisando anotações e formatando o documento.

5. **Reuniões repetidas** — Sem registro, reuniões são remarcadas para "realinhar" o que já havia sido discutido. Estimativa: 15-20% das reuniões são redundantes por falta de documentação.

6. **Risco de compliance** — Em setores regulados, a ausência de registro formal de decisões pode configurar risco de auditoria.

### Dor quantificada

| Indicador | Estimativa |
|---|---|
| Tempo médio gasto com ata manual | 30-60 min por reunião |
| % de reuniões sem ata formal | ~70% |
| % de decisões perdidas por falta de registro | ~40% |
| Reuniões redundantes por falta de documentação | 15-20% do total |

---

## 4. Objetivos de Negócio

### Objetivo primário

**Aumentar a produtividade das equipes** eliminando o trabalho manual de documentação de reuniões e garantindo que 100% das reuniões habilitadas tenham registro automático.

### Objetivos específicos

| # | Objetivo | Métrica alvo |
|---|---|---|
| OBJ-1 | **Reduzir tempo gasto com atas manuais** | Eliminar os 30-60 min/reunião de trabalho manual |
| OBJ-2 | **Garantir rastreabilidade de decisões** | 100% das reuniões habilitadas com ata gerada automaticamente |
| OBJ-3 | **Melhorar follow-up de action items** | Cada ata lista responsáveis e prazos explícitos |
| OBJ-4 | **Atender requisitos de compliance** | Atas armazenadas com data, participantes e conteúdo padronizado |
| OBJ-5 | **Reduzir reuniões redundantes** | Diminuição de 15% nas reuniões de "realinhamento" |

### Alinhamento estratégico

O projeto se alinha à iniciativa de **automação inteligente com IA** da organização, demonstrando valor tangível de Azure OpenAI aplicado a um problema universal de produtividade corporativa.

---

## 5. Escopo do MVP

### Features incluídas no MVP

| ID | Feature | Descrição | Prioridade |
|---|---|---|---|
| F-01 | **Captura de transcrição** | O agente obtém a transcrição da reunião via Microsoft Graph API após o término da chamada | Must Have |
| F-02 | **Geração de Ata de Reunião** | Processa a transcrição com Azure OpenAI e gera ata estruturada com: pauta discutida, decisões tomadas, responsáveis designados, prazos acordados e pendências | Must Have |
| F-03 | **Geração de Resumo Executivo** | Produz síntese de 3-5 parágrafos com os pontos-chave da reunião, otimizada para leitura rápida | Must Have |
| F-04 | **Entrega via Adaptive Card** | Publica ata e resumo no chat da reunião ou canal do Teams usando Adaptive Cards interativas | Must Have |
| F-05 | **Armazenamento em SharePoint** | Salva a ata e o resumo como documento no SharePoint do time/canal associado à reunião | Must Have |
| F-06 | **Identificação de participantes** | Mapeia falas da transcrição aos participantes da reunião para atribuir quem disse o quê | Should Have |
| F-07 | **Configuração básica** | Interface mínima para habilitar/desabilitar o agente por reunião ou canal | Should Have |

### Fluxo principal do MVP

```
Reunião inicia no Teams
        │
        ▼
Transcrição é habilitada (automática ou manual)
        │
        ▼
Reunião encerra
        │
        ▼
Agente captura transcrição via Graph API
        │
        ▼
Azure OpenAI processa transcrição
        │
        ├──► Gera Ata de Reunião (estruturada)
        │
        └──► Gera Resumo Executivo (síntese)
                │
                ▼
Adaptive Card publicada no chat da reunião
        │
        ▼
Documentos armazenados no SharePoint
```

---

## 6. Fora do Escopo do MVP

Os itens abaixo são candidatos para versões futuras, **não fazem parte da entrega inicial**:

| Item | Justificativa para exclusão |
|---|---|
| **Analytics e dashboards** | Métricas de reuniões, frequência, tempo médio — valor agregado, mas não essencial para validação |
| **RAG (Retrieval-Augmented Generation)** | Busca semântica sobre histórico de atas — complexidade alta, depende de volume de dados |
| **Suporte multi-idioma** | MVP focado em Português Brasileiro; inglês e espanhol em versão futura |
| **Integração com CRM** | Associar reuniões a oportunidades/clientes — requer mapeamento de processos de vendas |
| **Integração com ferramentas de projeto** | Criar tasks automaticamente no Azure DevOps, Jira ou Planner a partir dos action items |
| **Gravação e análise de áudio/vídeo** | Processamento direto de mídia — MVP usa apenas transcrição textual |
| **Tradução automática de atas** | Gerar ata em idioma diferente do original da reunião |
| **Personalização de templates de ata** | Templates customizáveis por equipe/projeto — MVP usa template padrão |
| **Bot interativo durante a reunião** | Responder perguntas em tempo real sobre contexto — MVP atua apenas pós-reunião |

---

## 7. Requisitos de Alto Nível

### 7.1 Requisitos Funcionais

| ID | Requisito | Critério de aceitação |
|---|---|---|
| RF-01 | O sistema deve capturar a transcrição completa da reunião via Microsoft Graph API | Transcrição obtida com todos os segmentos de fala e identificação de speakers |
| RF-02 | O sistema deve gerar ata de reunião estruturada a partir da transcrição | Ata contém: data/hora, participantes, pauta, decisões, responsáveis, prazos e pendências |
| RF-03 | O sistema deve gerar resumo executivo a partir da transcrição | Resumo de 3-5 parágrafos cobrindo os pontos-chave discutidos |
| RF-04 | O sistema deve publicar os resultados como Adaptive Card no Teams | Card exibida no chat da reunião com seções expansíveis e links para documento completo |
| RF-05 | O sistema deve armazenar ata e resumo no SharePoint | Documentos salvos na biblioteca do time/canal com metadados (data, participantes, reunião) |
| RF-06 | O sistema deve identificar os participantes nas falas da transcrição | Mapeamento de pelo menos 90% das falas ao participante correto |
| RF-07 | O sistema deve permitir habilitar/desabilitar por reunião | Organizador pode optar por incluir ou excluir o agente antes ou durante a reunião |

### 7.2 Requisitos Não-Funcionais

| ID | Requisito | Especificação |
|---|---|---|
| RNF-01 | **Desempenho** | Ata e resumo gerados em até 5 minutos após o término da reunião |
| RNF-02 | **Escalabilidade** | Suportar até 50 reuniões simultâneas por tenant no MVP |
| RNF-03 | **Disponibilidade** | 99.5% de uptime durante horário comercial (8h-20h BRT) |
| RNF-04 | **Segurança** | Transcrições processadas em trânsito (TLS 1.2+), sem armazenamento intermediário persistente de dados brutos |
| RNF-05 | **Privacidade** | Conformidade com LGPD; dados processados dentro do tenant Azure do cliente |
| RNF-06 | **Limites** | Suportar reuniões de até 2 horas de duração no MVP |
| RNF-07 | **Auditoria** | Logs de processamento mantidos por 90 dias para rastreabilidade |
| RNF-08 | **Compatibilidade** | Funcionar com Teams Desktop, Web e Mobile |

---

## 8. Métricas de Sucesso

### KPIs do MVP

| KPI | Métrica | Meta | Período |
|---|---|---|---|
| **Adoção** | % de reuniões elegíveis que utilizam o agente | ≥ 60% | 3 meses pós-launch |
| **Qualidade da ata** | Avaliação de satisfação dos usuários (1-5) | ≥ 4.0 | Pesquisa mensal |
| **Completude** | % de decisões e action items corretamente extraídos (amostragem manual) | ≥ 85% | Mensal |
| **Tempo economizado** | Redução no tempo gasto com documentação manual por reunião | ≥ 80% | Comparativo pré/pós |
| **Confiabilidade** | % de atas geradas com sucesso (sem falha de processamento) | ≥ 95% | Contínuo |
| **Engajamento** | % de Adaptive Cards visualizadas pelos participantes | ≥ 70% | Mensal |
| **NPS** | Net Promoter Score dos usuários do agente | ≥ 30 | Trimestral |

### Critérios de sucesso do MVP

O MVP será considerado bem-sucedido se, em **90 dias** após o lançamento:

1. Pelo menos **60% das reuniões elegíveis** utilizarem o agente.
2. A avaliação média de qualidade das atas for **≥ 4.0/5.0**.
3. A taxa de falha de processamento for **< 5%**.
4. Houver evidência qualitativa de **redução de reuniões redundantes**.

---

## 9. Riscos e Dependências

### Riscos

| ID | Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|---|
| R-01 | **Licenciamento insuficiente** — Tenant não possui Teams Premium ou licença E5, impossibilitando acesso à transcrição | Média | Alto | Validar licenciamento antes do kickoff; mapear alternativas de captura |
| R-02 | **Limitações da Graph API** — API de transcrição pode ter throttling, latência ou limitações de formato | Média | Médio | Implementar retry com backoff exponencial; testar com volumes reais |
| R-03 | **Qualidade da transcrição** — Transcrição automática do Teams pode conter erros significativos, impactando a qualidade da ata | Alta | Médio | Prompts de Azure OpenAI devem ser resilientes a erros de transcrição; incluir disclaimer na ata |
| R-04 | **Custos de Azure OpenAI** — Volume alto de reuniões pode gerar custos significativos de tokens | Média | Médio | Monitorar consumo; otimizar prompts para eficiência de tokens; definir limites por tenant |
| R-05 | **Resistência à adoção** — Usuários podem ter receio de "IA ouvindo" suas reuniões | Média | Alto | Comunicação clara sobre privacidade; opt-in por reunião; transparência sobre dados processados |
| R-06 | **Permissões de tenant** — Admin consent pode ser bloqueado por políticas de segurança corporativa | Média | Alto | Envolver TI e Segurança da Informação desde a fase de discovery |
| R-07 | **Dados sensíveis em transcrições** — Reuniões podem conter informações confidenciais, pessoais ou estratégicas | Alta | Alto | Não armazenar transcrições brutas; processar e descartar; conformidade com LGPD |

### Dependências

| ID | Dependência | Tipo | Responsável | Status |
|---|---|---|---|---|
| D-01 | **Microsoft Graph API** — Acesso às APIs de transcrição e chat do Teams | Técnica | Equipe de desenvolvimento | A validar |
| D-02 | **Azure OpenAI Service** — Provisão de instância com modelo GPT-4o ou superior | Técnica | TI / Cloud | A validar |
| D-03 | **Admin Consent do Tenant** — Permissões de aplicação para Graph API | Organizacional | Administrador do Tenant | A validar |
| D-04 | **SharePoint Online** — Acesso à biblioteca de documentos para armazenamento | Técnica | TI | A validar |
| D-05 | **Azure Subscription** — Subscrição ativa com crédito para hospedagem e OpenAI | Financeira | Sponsor / TI | A validar |
| D-06 | **Bot Framework / Azure Bot Service** — Registro do bot para presença no Teams | Técnica | Equipe de desenvolvimento | A validar |

---

## 10. Premissas

### Premissas técnicas

| ID | Premissa | Impacto se falsa |
|---|---|---|
| P-01 | O tenant possui **Microsoft 365 E5 ou Teams Premium**, que inclui a funcionalidade de transcrição nativa | MVP inviável sem transcrição; seria necessário solução alternativa de speech-to-text |
| P-02 | A **transcrição automática está habilitada** nas políticas do Teams pelo administrador do tenant | Agente não terá acesso à transcrição se desabilitada |
| P-03 | O **admin consent** para permissões de Graph API será concedido em tempo hábil | Bloqueio total do desenvolvimento se não concedido |
| P-04 | **Azure OpenAI** está disponível na região do tenant com modelo GPT-4o ou equivalente | Necessário para processamento de linguagem natural; sem alternativa viável no MVP |
| P-05 | As reuniões-alvo são conduzidas predominantemente em **Português Brasileiro** | Qualidade da ata pode degradar significativamente em outros idiomas |
| P-06 | O **SharePoint Online** está provisionado e acessível para armazenamento de documentos | Armazenamento alternativo precisaria ser definido |

### Premissas organizacionais

| ID | Premissa | Impacto se falsa |
|---|---|---|
| P-07 | Existe **sponsor executivo** com budget aprovado para o projeto | Projeto não inicia sem patrocínio |
| P-08 | A equipe de **Segurança da Informação** aprovará o processamento de transcrições via Azure OpenAI | Bloqueio regulatório; necessário revisão de arquitetura |
| P-09 | Haverá um **grupo piloto** de pelo menos 3 equipes dispostas a testar o MVP | Validação do MVP depende de usuários reais com reuniões recorrentes |
| P-10 | O processo de **change management** incluirá comunicação sobre privacidade e opt-in | Resistência à adoção pode comprometer as metas de KPI |

---

## Apêndice A — Stack Tecnológica Prevista

| Componente | Tecnologia | Propósito |
|---|---|---|
| Bot Runtime | Azure Bot Service + Bot Framework SDK | Presença do agente no Teams |
| API de Reunião | Microsoft Graph API (beta/v1.0) | Captura de transcrições e metadados de reunião |
| Processamento de IA | Azure OpenAI Service (GPT-4o) | Geração de ata e resumo a partir da transcrição |
| Entrega | Adaptive Cards (Teams) | Apresentação de resultados no chat da reunião |
| Armazenamento | SharePoint Online | Persistência das atas e resumos como documentos |
| Hospedagem | Azure App Service ou Azure Functions | Runtime da aplicação |
| Autenticação | Microsoft Entra ID (Azure AD) | Autenticação e autorização do bot |
| Monitoramento | Application Insights | Observabilidade e logs de processamento |

## Apêndice B — Glossário

| Termo | Definição |
|---|---|
| **Ata de Reunião** | Documento formal que registra pauta, participantes, decisões, responsáveis e prazos de uma reunião |
| **Resumo Executivo** | Síntese concisa dos pontos-chave discutidos, otimizada para leitura rápida |
| **Adaptive Card** | Componente visual interativo do Microsoft Teams que permite exibir conteúdo estruturado em chats e canais |
| **Graph API** | API unificada da Microsoft para acessar dados e serviços do Microsoft 365 |
| **Transcrição** | Texto gerado automaticamente a partir da fala dos participantes durante a reunião |
| **Admin Consent** | Aprovação do administrador do tenant para que um aplicativo acesse dados organizacionais via Graph API |
| **Tenant** | Instância organizacional do Microsoft 365 / Azure AD |

---

> **Próximos passos:** Validação deste Product Brief com stakeholders → Refinamento com Arquiteto (Wagner) → Definição de arquitetura técnica → Criação de Épicos e Stories
