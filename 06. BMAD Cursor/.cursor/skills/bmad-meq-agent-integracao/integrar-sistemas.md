---
name: integrar-sistemas
description: Guia integração entre sistemas
menu-code: IS
---

# Integrar Sistemas

Guie o usuário na integração entre sistemas — síncrono, assíncrono ou webhooks.

## Processo

1. **Entenda os sistemas** — Quem consome? Quem fornece? Qual o fluxo?

2. **Padrões de integração:**
   - **Síncrono (REST)** — Request/response. Simples, bloqueante. Bom para operações rápidas.
   - **Assíncrono (mensageria)** — Queue, pub/sub. Desacoplado, resiliente. Bom para processamento em background.
   - **Webhooks** — Push do provedor para o consumidor. Evita polling. Requer retry e idempotência.

3. **Trade-offs:**
   - Síncrono: mais simples, mas acoplamento e timeout
   - Assíncrono: desacoplamento, mas complexidade e eventual consistency
   - Webhook: push eficiente, mas consumidor precisa estar disponível

4. **Para cada integração:**
   - Contrato (DC)
   - Autenticação (AA)
   - Resiliência (RS)

5. **Documente** — Resuma decisões. Sugira salvar (SM).

## Regras

- Escolher padrão adequado ao caso
- Contratos claros entre sistemas
- Considerar idempotência em webhooks e retries
