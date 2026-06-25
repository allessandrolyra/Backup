---
name: encaminhar
description: Encaminha para um agente específico da squad
menu-code: EN
---

# Encaminhar para Agente

Encaminhe o usuário para o agente correto da Squad MEQ.

## Processo

1. **Identifique a necessidade** — O usuário quer falar com qual tipo de especialista?
   - Product (requisitos, prioridades, escopo)
   - Arquiteto (estrutura, tecnologias, padrões)
   - Full-Stack (implementação web/mobile)
   - Banco de Dados (modelagem, queries, performance)
   - Integração (APIs, sistemas externos)
   - QA (testes, qualidade)
   - DevOps (CI/CD, deploy, infra)

2. **Consulte** `references/squad-knowledge.md` para o nome exato do skill de cada agente.

3. **Encaminhe** — Diga ao usuário: "Para isso, acione o agente [Nome]. Use: [frase de ativação ou nome do skill]."

4. **Contexto** — Se houver contexto relevante da conversa atual, resuma para o usuário levar ao próximo agente.

## Mapa de Encaminhamento

| Necessidade | Agente | Skill |
|-------------|--------|-------|
| Requisitos, escopo, prioridades | Paula (Product Developer) | bmad-meq-agent-product-developer |
| Arquitetura, stack, padrões | Wagner (Arquiteto) | bmad-meq-agent-arquiteto |
| Implementação, código | Felipe (Full-Stack) | bmad-meq-agent-fullstack |
| Modelagem, schemas, queries | Diana (Banco de Dados) | bmad-meq-agent-banco-dados |
| APIs, integrações, contratos | Igor (Integração) | bmad-meq-agent-integracao |
| Testes, qualidade, cobertura | Quinn (QA) | bmad-meq-agent-qa |
| CI/CD, deploy, pipelines | Davi (DevOps) | bmad-meq-agent-devops |
