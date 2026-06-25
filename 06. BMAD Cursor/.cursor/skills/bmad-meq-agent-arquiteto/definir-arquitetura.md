---
name: definir-arquitetura
description: Guia decisões arquiteturais
menu-code: DA
---

# Definir Arquitetura

Guie o usuário nas decisões arquiteturais através de perguntas estruturadas.

## Processo

1. **Entenda o contexto** — O que o Product Developer definiu? Web, Android, iOS ou multiplataforma?

2. **Perguntas essenciais:**
   - Qual a escala esperada? (usuários, dados, transações)
   - Há requisitos de integração? (APIs externas, sistemas legados)
   - Qual a estratégia de deploy? (cloud, on-premise, híbrido)
   - Há restrições de plataforma? (Android/iOS nativo vs cross-platform)

3. **Componentes principais:**
   - Backend (API, serviços, banco)
   - Frontend web (SPA, SSR, framework)
   - Apps mobile (nativo, React Native, Flutter)
   - Infraestrutura (hosting, CI/CD)

4. **NFRs (Non-Functional Requirements):**
   - **Performance** — Latência aceitável? Throughput esperado?
   - **Disponibilidade** — SLA? Tolerância a falhas?
   - **Segurança** — Autenticação, autorização, dados sensíveis?
   - **Escalabilidade** — Crescimento esperado? Horizontal vs vertical?

5. **Padrões** — Sugira padrões adequados: monolito modular, microserviços, serverless, etc. Conecte cada escolha ao contexto do produto.

6. **Documente** — Resuma decisões. Sugira criar documento completo (CA) quando houver clareza.

7. **Memória** — Se decisões importantes foram tomadas, sugira salvar (SM).

## Regras

- Jornadas do usuário guiam decisões
- Tecnologia chata primeiro — estabilidade sobre novidade
- Adiar decisões até ter dados suficientes
- Sem over-engineering para MVP
