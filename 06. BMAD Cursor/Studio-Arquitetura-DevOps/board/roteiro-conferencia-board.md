# Roteiro de Conferência — Montagem do Azure Board

> **Time**: Studio Arquitetura e DevOps
> **Objetivo da reunião**: Alinhar tudo que precisa para criar o board do time no Azure DevOps.
> **Participantes sugeridos**: Alessandro, Eder, membros-chave do time
> **Duração estimada**: 45–60 min

---

## Abertura (5 min)

**Falar:**
- O time não tem board hoje. Isso saiu como urgência na Daily.
- O objetivo é ganhar visibilidade: saber quem faz o quê, em que estágio, com que prioridade.
- Esta reunião serve para alinhar **o que precisamos** antes de criar qualquer coisa.

**Resultado esperado da reunião:**
- Sair com decisões claras sobre onde criar, como estruturar e quem acessa.

---

## Ponto 1 — Onde vai morar o board? (10 min)

**Perguntas para resolver:**

| # | Pergunta | Decisão |
|---|---|---|
| 1 | Qual **organização** do Azure DevOps vamos usar? | _______________ |
| 2 | Criar **projeto novo** ou usar um projeto existente com Area Path? | _______________ |
| 3 | Quem é o **admin** que pode configurar? | _______________ |
| 4 | Qual **Process Template**? (Agile / Scrum / Basic) | _______________ |

**Ponto de atenção para levantar:**
- Process Template é difícil de mudar depois. Precisa decidir certo agora.
- Projeto compartilhado vs. dedicado: compartilhado é mais rápido de conseguir, mas pode misturar itens.

---

## Ponto 2 — Quem somos? (5 min)

**Perguntas para resolver:**

| # | Pergunta | Decisão |
|---|---|---|
| 1 | Quantas pessoas no time? | _______________ |
| 2 | Quais os papéis? (Arquiteto, DevOps, SRE, Líder...) | _______________ |
| 3 | Todos num board só ou existem sub-grupos com backlogs separados? | _______________ |
| 4 | Quem vai ser o **dono do board**? (mantém organizado, prioriza) | _______________ |

**Ponto de atenção para levantar:**
- Board sem dono vira cemitério. Alguém precisa ser responsável.

---

## Ponto 3 — O que o time faz? (10 min)

**Perguntas para resolver:**

| # | Pergunta | Decisão |
|---|---|---|
| 1 | Quais **tipos de trabalho** fazemos? (arquitetura, pipeline, suporte, POC...) | _______________ |
| 2 | De onde vem a demanda? (interna, squads, clientes, incidentes) | _______________ |
| 3 | Tem trabalho **planejado** e **não-planejado** (suporte/incidentes)? | _______________ |
| 4 | Quando um trabalho está **pronto**? (precisa de aprovação? deploy? doc?) | _______________ |
| 5 | Temos **dependência** de outros times? | _______________ |

**Ponto de atenção para levantar:**
- Se tem trabalho reativo (suporte, incidentes), precisa de tratamento separado no board para não sabotar o planejado.

---

## Ponto 4 — Como queremos o fluxo? (10 min)

**Apresentar a proposta de colunas e validar:**

```
Backlog → Em Análise → Ready → Em Andamento → Validação → Done
```

| # | Pergunta | Decisão |
|---|---|---|
| 1 | Essas colunas representam nosso fluxo real? | _______________ |
| 2 | Falta alguma etapa? Sobra alguma? | _______________ |
| 3 | **Scrum** (sprints) ou **Kanban** (fluxo contínuo) ou mistura? | _______________ |
| 4 | Tem **aprovação formal** em alguma etapa? | _______________ |
| 5 | Queremos **WIP limits** (limite por coluna) desde o início? | _______________ |

**Ponto de atenção para levantar:**
- Começar com poucas colunas. Adicionar é fácil, remover com itens dentro é chato.
- Se o time é mais reativo, Kanban pode funcionar melhor que Scrum.

---

## Ponto 5 — Quem precisa ver o quê? (5 min)

| # | Pergunta | Decisão |
|---|---|---|
| 1 | Quem precisa ver o board além do time? (gestão, clientes) | _______________ |
| 2 | O que o **gestor** quer ver de cara? (quem faz o quê? atrasados? volume?) | _______________ |
| 3 | Precisa de **relatórios** ou a visão do board basta por enquanto? | _______________ |
| 4 | Precisa integrar com **Repos, Pipelines, Wiki**? | _______________ |

---

## Ponto 6 — Acessos (5 min)

| # | Pergunta | Decisão |
|---|---|---|
| 1 | Quem precisa de acesso **Basic** (cria e edita itens)? | _______________ |
| 2 | Quem precisa só de **Stakeholder** (visualiza)? | _______________ |
| 3 | Como solicitar os acessos na **BU2**? Quem aprova? | _______________ |
| 4 | Prazo para ter os acessos? | _______________ |

---

## Fechamento (5 min)

**Consolidar:**

| Item | Decisão | Responsável | Prazo |
|---|---|---|---|
| Criar projeto/Area Path | | | |
| Solicitar acessos BU2 | | | |
| Configurar colunas do board | | | |
| Criar primeiros work items | | | |
| Montar dashboard mínimo | | | |

**Próximo passo**: Após esta reunião, a configuração do board pode ser feita no mesmo dia.

---

## Checklist de preparação (antes da reunião)

- [ ] Agendar com Eder e membros-chave
- [ ] Ter a lista de nomes + e-mails do time
- [ ] Saber se já existe org/projeto no Azure DevOps
- [ ] Levar este roteiro impresso ou compartilhado em tela
