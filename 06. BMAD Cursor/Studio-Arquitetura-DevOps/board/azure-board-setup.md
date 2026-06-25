# Azure Board — Studio Arquitetura e DevOps

> **Status**: URGENTE — Definido na Daily de 14/05/2026
> **Objetivo**: Ganho de visibilidade — enxergar o que cada um está fazendo e facilitar leitura/gestão do trabalho.
> **Alinhamento pendente**: Eder (estrutura, campos, etapas, organização)
> **Acesso pendente**: Solicitar acessos na BU2

---

## 1. Contexto (Daily 14/05)

- Não existe board do time hoje — trabalhar sem board não é viável.
- Necessidade de um board **próprio do time Studio Arquitetura e DevOps**.
- Foco em **visibilidade**: quem está fazendo o quê, em que estágio, com que prioridade.
- Ações imediatas:
  1. Criar o board e estruturar colunas/fluxo
  2. Solicitar acessos necessários (BU2)
  3. Alinhar com Eder a estrutura sugerida (campos/etapas/organização)

---

## 2. Configuração do Projeto

| Campo | Valor | Observação |
|---|---|---|
| **Nome do Time** | Studio Arquitetura e DevOps | |
| **Organização Azure DevOps** | _Confirmar com Eder_ | BU2 |
| **Projeto** | _Confirmar com Eder_ | Criar novo ou usar existente? |
| **Process Template** | Agile | Sugestão — alinhar com Eder |
| **Área Path** | `\Studio-Arquitetura-DevOps` | Isola os itens do time |
| **Iteration Path** | `\Studio-Arquitetura-DevOps\Sprint {n}` | Cadência a definir |

---

## 3. Proposta de Colunas do Board (para alinhar com Eder)

O fluxo abaixo reflete a realidade de um time de Arquitetura + DevOps, onde o trabalho nem sempre é "código" — inclui análises, POCs, documentos técnicos e suporte a squads.

### Fluxo Kanban

```
 ┌──────────┐   ┌─────────────┐   ┌─────────┐   ┌───────────┐   ┌───────────┐   ┌──────┐
 │  Backlog  │──▶│ Em Análise  │──▶│  Ready  │──▶│ Em Andamento│──▶│ Validação │──▶│ Done │
 └──────────┘   └─────────────┘   └─────────┘   └───────────┘   └───────────┘   └──────┘
```

| Coluna | WIP Limit | O que fica aqui |
|---|---|---|
| **Backlog** | — | Tudo que entra: demandas, ideias, pedidos de squads |
| **Em Análise** | 4 | Time está refinando, investigando viabilidade, quebrando em tarefas |
| **Ready** | 6 | Analisado, estimado, pronto para pegar |
| **Em Andamento** | 5 | Alguém está executando agora |
| **Validação** | 3 | Review técnico, teste, aprovação de par ou líder |
| **Done** | — | Entregue e aceito |

> **Nota para Eder**: Os WIP limits são sugestões iniciais. Ajustar conforme tamanho do time.

---

## 4. Campos Sugeridos nos Work Items

Campos que dão visibilidade ao gestor e ao time:

| Campo | Tipo | Por que |
|---|---|---|
| **Assigned To** | Pessoa | Quem está fazendo — visibilidade principal |
| **Priority** | 1-4 | Ordenar o backlog |
| **Tipo de Trabalho** (tag ou campo) | Escolha | Arquitetura / DevOps / Suporte / POC / Documentação |
| **Cliente/Squad** | Tag ou campo | Saber para quem é a demanda |
| **Estimativa (Story Points)** | Número | Capacidade e velocity |
| **Data de Início** | Data | Quando pegou |
| **Target Date** | Data | Quando precisa estar pronto |
| **Bloqueado?** | Flag | Sinalizar impedimentos rápido |

---

## 5. Tipos de Work Item

### Hierarquia recomendada

```
Epic           →  Iniciativa grande (ex: "Padronização de Pipelines CI/CD")
 └── Feature   →  Entrega intermediária (ex: "Template de pipeline .NET")
      └── User Story / Task  →  Unidade de trabalho (ex: "Criar stage de build no template")
```

### Tipos de trabalho do time (usar como tags ou categorias)

| Categoria | Exemplos |
|---|---|
| **Arquitetura** | Solution design, ADR, revisão de arquitetura, padrão técnico |
| **DevOps** | Pipeline, IaC, automação, template, configuração de ambiente |
| **Suporte a Squads** | Apoio técnico a outros times, troubleshooting |
| **POC / Pesquisa** | Prova de conceito, spike técnico, avaliação de ferramenta |
| **Documentação** | Runbooks, guias, wiki, onboarding |
| **Infra / SRE** | Provisionamento, monitoramento, incident response |

---

## 6. Sprints

| Campo | Proposta |
|---|---|
| **Cadência** | 2 semanas |
| **Início sugerido** | Próxima segunda após alinhamento com Eder |
| **Cerimônias** | Planning (início), Daily (diária), Review + Retro (fim) |

---

## 7. Dashboards — O que montar de cara

Para atender o objetivo de **visibilidade**, estes widgets resolvem 80% da necessidade:

| Widget | Mostra o quê |
|---|---|
| **Board configurado por membro** | Quem está fazendo o quê — visão rápida |
| **Sprint Burndown** | Estamos no ritmo da sprint? |
| **Work Items por Estado** | Onde o trabalho está acumulando? |
| **Itens bloqueados** | Query de itens com tag/flag "bloqueado" |
| **Velocity (após 3+ sprints)** | Quanto o time entrega por ciclo |

---

## 8. Checklist de Ações

### Imediato (esta semana)

- [ ] **Solicitar acesso BU2** — listar quem precisa de acesso e qual nível (Basic, Stakeholder)
- [ ] **Agendar alinhamento com Eder** — apresentar esta proposta de estrutura
- [ ] **Definir**: criar projeto novo ou usar Area Path dentro de projeto existente?
- [ ] **Levantar membros do time** — nomes, roles, e-mails para configurar no Azure DevOps

### Após alinhamento com Eder

- [ ] Criar Area Path e Iteration Paths
- [ ] Configurar colunas do board conforme aprovado
- [ ] Criar os primeiros Epics/Features com base no trabalho atual
- [ ] Migrar trabalho em andamento para o board (cada um cria seus itens)
- [ ] Montar dashboard mínimo (board por membro + burndown)

### Semana seguinte

- [ ] Primeira Planning com o board
- [ ] Ajustar WIP limits e colunas conforme feedback do time
- [ ] Configurar notificações e alertas

---

## 9. Proposta para levar ao Eder

**Resumo em 3 pontos para a conversa:**

1. **O que queremos**: Um board Azure Boards exclusivo do time Studio Arq & DevOps, com visibilidade de quem faz o quê e em que estágio.
2. **O que precisamos**: Acesso BU2 para o time + permissão para configurar Area Path / Board / Dashboard.
3. **Estrutura sugerida**: 6 colunas (Backlog → Done), campos de atribuição/prioridade/tipo, categorias por natureza do trabalho (Arquitetura, DevOps, Suporte, POC, Doc, Infra).

> Se Eder preferir estrutura diferente, este documento serve como base de discussão — tudo é ajustável.
