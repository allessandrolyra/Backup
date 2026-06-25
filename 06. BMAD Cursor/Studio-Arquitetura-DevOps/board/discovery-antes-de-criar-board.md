# Discovery — Perguntas antes de criar o Azure Board

> Responder estas perguntas **antes** de abrir o Azure DevOps evita retrabalho,
> garante que a estrutura atenda de verdade e facilita o alinhamento com o Eder.

---

## BLOCO 1 — Organização e Acesso (o que depende da empresa)

Estas perguntas definem **onde** o board vai existir. Errar aqui significa migrar depois.

| # | Pergunta | Por que importa | Sua Resposta |
|---|---|---|---|
| 1.1 | Já existe uma **Organization** no Azure DevOps da Foursys/BU2? | Se não existe, precisa criar. Se existe, precisa saber o nome. | |
| 1.2 | Já existe um **Project** onde o time pode criar o board? | Pode ser projeto novo ou Area Path dentro de projeto existente. Cada opção tem prós/contras. | |
| 1.3 | Quem é o **admin** da org/projeto? É o Eder? | Saber quem pode dar permissões, criar Area Paths, configurar o board. | |
| 1.4 | Qual o **Process Template** usado? (Agile, Scrum, CMMI, Basic) | Define os tipos de work item disponíveis. Mudar depois é muito trabalhoso. | |
| 1.5 | Quantas pessoas precisam de acesso? Quais **níveis**? | Basic (cria/edita itens) vs. Stakeholder (só visualiza). Impacta licenciamento. | |
| 1.6 | Existe alguma **política de governança** da empresa sobre como usar Azure DevOps? | Algumas empresas têm padrões de nomenclatura, fields obrigatórios, etc. | |

### Cuidado aqui
- **Process Template é quase irreversível.** Se escolher Scrum e depois quiser Agile, precisa criar projeto novo e migrar tudo.
- **Projeto compartilhado vs. dedicado**: projeto compartilhado é mais simples de pedir, mas o board pode ficar poluído com itens de outros times.

---

## BLOCO 2 — O Time (quem somos)

| # | Pergunta | Por que importa | Sua Resposta |
|---|---|---|---|
| 2.1 | Quantas pessoas compõem o time? | Dimensiona WIP limits, capacidade de sprint. | |
| 2.2 | Quais os **papéis**? (Arquiteto, DevOps, SRE, Líder, etc.) | Pode definir se precisa de sub-times ou uma equipe só. | |
| 2.3 | Todos trabalham **juntos** ou existem **sub-grupos** com backlogs separados? | Se forem sub-grupos, talvez precise de mais de um board ou Area Path. | |
| 2.4 | Quem vai ser o **dono do board**? (quem prioriza, refina, mantém organizado) | Sem dono, o board vira cemitério em 2 sprints. | |
| 2.5 | O time já tem alguma **rotina** (daily, planning, retro)? | Se já tem cerimônias, o board precisa servir a elas. | |

### Cuidado aqui
- **Board sem dono morre.** Alguém precisa ser responsável por manter o backlog limpo e priorizado.
- **Não misture times no mesmo board** se eles têm backlogs e prioridades independentes.

---

## BLOCO 3 — O Trabalho (o que fazemos)

| # | Pergunta | Por que importa | Sua Resposta |
|---|---|---|---|
| 3.1 | Quais **tipos de trabalho** o time faz? | Define categorias, tags, e talvez campos customizados. | |
| 3.2 | O trabalho vem de onde? (demanda interna, squads, clientes, incidentes) | Define como os itens entram no backlog. | |
| 3.3 | Existe trabalho **planejado** (projetos) e **não-planejado** (suporte, incidentes)? | Se sim, pode precisar de swim lanes separadas no board. | |
| 3.4 | Como vocês medem se um trabalho está **pronto**? | Define a coluna "Done" — precisa de aprovação? Deploy? Documentação? | |
| 3.5 | Existe **dependência** de outros times ou aprovações externas? | Pode precisar de coluna "Blocked/Waiting" ou campo de dependência. | |
| 3.6 | Qual o tamanho típico de um item de trabalho? (horas, dias, semanas) | Se muito grande, precisa quebrar melhor. Se muito pequeno, talvez Tasks bastam. | |

### Cuidado aqui
- **Não crie colunas demais.** Comece com 4-6. Adicionar é fácil, remover depois com itens lá dentro é chato.
- **Trabalho não-planejado** (suporte, incidentes) pode sabotar o sprint se não tiver tratamento separado.

---

## BLOCO 4 — O Fluxo (como trabalhamos)

| # | Pergunta | Por que importa | Sua Resposta |
|---|---|---|---|
| 4.1 | Quais **etapas** um trabalho percorre do início ao fim? | Define as colunas do board. | |
| 4.2 | Tem etapa de **review/validação** antes de dar como pronto? | Se sim, precisa de coluna específica. | |
| 4.3 | Vão usar **Sprints** (Scrum) ou **fluxo contínuo** (Kanban)? | Muda a configuração do board e as cerimônias. | |
| 4.4 | Precisa de **aprovação formal** de alguém (líder, cliente) em alguma etapa? | Pode ser modelado como coluna ou como campo. | |
| 4.5 | Querem **WIP limits** (limite de itens por coluna)? | Evita sobrecarga, mas precisa de disciplina para funcionar. | |

### Cuidado aqui
- **Scrum vs. Kanban**: Scrum é bom se o time tem cadência e consegue planejar sprints. Kanban é melhor se o trabalho é mais reativo (suporte, incidentes). Pode misturar (Scrumban).
- **WIP limits só funcionam se o time respeitar.** Comece sem e adicione depois que o fluxo estiver claro.

---

## BLOCO 5 — Visibilidade (o que queremos enxergar)

| # | Pergunta | Por que importa | Sua Resposta |
|---|---|---|---|
| 5.1 | Quem **precisa ver** o board? (só o time? gestão? clientes?) | Define permissões e o que mostrar no dashboard. | |
| 5.2 | O que o **gestor** quer ver de cara? | Pode ser "quem faz o quê", "o que está atrasado", "quantos itens entregues". | |
| 5.3 | Precisa de **relatórios** ou só a visão do board basta? | Relatórios exigem campos preenchidos consistentemente. | |
| 5.4 | Querem rastrear **tempo gasto** por item? | Se sim, precisa de campo de horas e disciplina de preenchimento. | |
| 5.5 | O board precisa se integrar com algum **outro sistema**? (Repos, Pipelines, Wiki) | Define se precisa linkar work items a PRs, builds, etc. | |

### Cuidado aqui
- **Quanto mais campos obrigatórios, mais atrito para o time.** Comece com o mínimo e adicione conforme a necessidade real aparecer.
- **Dashboard sem dados bons é pior que nenhum dashboard.** Primeiro garanta que o time preenche o board, depois monte dashboards.

---

## BLOCO 6 — Riscos e Armadilhas Comuns

| Armadilha | Como evitar |
|---|---|
| Criar board e ninguém usar | Definir dono, usar na daily, começar simples |
| Colunas demais, burocracia | Máximo 6 colunas no início |
| Campos demais, ninguém preenche | Só obrigatório o que realmente vai ser usado |
| Board vira cemitério de itens velhos | Revisar backlog toda semana, fechar o que não vale mais |
| Misturar trabalho de times diferentes | Cada time com seu Area Path |
| Escolher Process Template errado | Confirmar com a governança antes de criar o projeto |
| Não ter admin para ajustar | Garantir que alguém do time tenha permissão de configuração |

---

## Resumo — Mínimo que precisa antes de abrir o Azure DevOps

1. **Onde**: Org, Projeto, Area Path (alinhar com Eder)
2. **Quem**: Lista de membros + nível de acesso
3. **O quê**: Tipos de trabalho que o time faz
4. **Como**: 4-6 colunas que representam o fluxo real
5. **Para quem**: Quem precisa de visibilidade e o que quer ver
6. **Dono**: Quem mantém o board vivo
