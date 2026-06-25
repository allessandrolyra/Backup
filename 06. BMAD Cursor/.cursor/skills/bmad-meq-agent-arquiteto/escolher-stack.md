---
name: escolher-stack
description: Escolhe stack tecnológico
menu-code: ES
---

# Escolher Stack

Ajude o usuário a escolher a stack tecnológica para web, Android e iOS.

## Processo

1. **Contexto** — O que o produto precisa? (da memória ou conversa)

2. **Por plataforma:**

   **Web:**
   - Frontend: React, Vue, Angular, Svelte, Next.js, etc.
   - Backend: Node, Python, Go, Java, .NET, etc.
   - Banco: PostgreSQL, MongoDB, MySQL, etc.

   **Android:**
   - Nativo (Kotlin): melhor performance, mais esforço
   - Cross-platform: React Native, Flutter — compartilha com iOS

   **iOS:**
   - Nativo (Swift): melhor performance, mais esforço
   - Cross-platform: React Native, Flutter — compartilha com Android

3. **Trade-offs:**
   - Nativo vs cross-platform — tempo de dev vs performance/UX
   - Monolito vs microserviços — complexidade vs escala
   - SQL vs NoSQL — modelo de dados

4. **Recomendação** — Sugira stack alinhado ao contexto: escala, time, prazo, orçamento.

5. **Documente** — Registre decisões. Sugira salvar (SM).

## Regras

- Prefira stack que o time conhece
- Cross-platform (Flutter/RN) pode acelerar se web + mobile
- Backend único pode servir web e apps via API
- Considere custos de infra e licenças
