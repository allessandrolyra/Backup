---
name: resiliencia
description: Planeja resiliência em integrações
menu-code: RS
---

# Resiliência

Planeje resiliência para integrações — retry, timeout, circuit breaker.

## Processo

1. **Entenda a integração** — Qual sistema? Síncrono ou assíncrono?

2. **Estratégias:**
   - **Timeout** — Evitar espera infinita. Definir limite por operação.
   - **Retry** — Tentar novamente em falhas transientes. Backoff exponencial.
   - **Circuit Breaker** — Parar de chamar quando o serviço está falhando. Evitar cascata.
   - **Fallback** — Resposta alternativa quando o serviço está indisponível.

3. **Quando retry:**
   - 5xx, timeout, connection error → retry
   - 4xx (exceto 429) → não retry (erro do cliente)
   - 429 → retry com backoff (rate limit)

4. **Circuit Breaker:**
   - Estados: closed, open, half-open
   - Threshold de falhas para abrir
   - Timeout para tentar novamente (half-open)

5. **Documente** — Registre configurações. Sugira salvar (SM).

## Regras

- Retry com backoff para não sobrecarregar
- Circuit breaker para proteger o sistema
- Logs de falhas para diagnóstico
