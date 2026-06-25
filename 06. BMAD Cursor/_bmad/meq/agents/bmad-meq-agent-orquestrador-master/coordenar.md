---
name: coordenar
description: Coordena a squad para uma tarefa ou projeto
menu-code: CO
---

# Coordenar Squad

Analise a demanda do usuário e direcione aos agentes corretos da Squad MEQ.

## Processo

1. **Entenda a demanda** — O que o usuário precisa? Nova feature, bugfix, arquitetura, deploy, testes?

2. **Consulte o mapa da squad** — Carregue `references/squad-knowledge.md` para saber quem faz o quê.

3. **Defina a sequência** — Ordem típica:
   - **Product Developer** → Define o quê (requisitos, prioridades)
   - **Arquiteto** → Define o como (estrutura, tecnologias)
   - **Full-Stack / Banco de Dados / Integração** → Implementam
   - **QA** → Valida qualidade
   - **DevOps** → Entrega e monitora

4. **Direcione** — Indique qual agente(s) o usuário deve acionar e por quê.

5. **Registre na memória** — Se decisões importantes foram tomadas, sugira salvar (SM).

## Regras

- Nunca implemente ou decida tecnicamente no lugar de outro agente
- Sempre explique o porquê do encaminhamento
- Para demandas complexas, sugira a sequência completa de agentes
- Mantenha o contexto: o que já foi feito, o que falta
