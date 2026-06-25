---
name: autenticacao-api
description: Define estratégia de autenticação
menu-code: AA
---

# Autenticação de API

Guie o usuário na definição da estratégia de autenticação para APIs.

## Processo

1. **Entenda o cenário** — API interna, externa, ou ambos? Quem autentica?

2. **Opções:**
   - **API Key** — Simples, para integrações máquina-a-máquina. Header ou query.
   - **JWT** — Stateless, para APIs que validam token. Expiração, claims.
   - **OAuth 2.0** — Para delegação de acesso (ex: login com Google). Client credentials, authorization code.
   - **Basic Auth** — User:pass em base64. Só sobre HTTPS, para casos simples.

3. **Recomendação por contexto:**
   - Internal API (microserviços): JWT ou API key
   - External API (terceiros): OAuth ou API key
   - Mobile/Web client: OAuth + JWT para sessão

4. **Segurança:**
   - HTTPS obrigatório
   - Tokens com expiração
   - Refresh token quando apropriado

5. **Documente** — Registre decisões. Sugira salvar (SM).

## Regras

- Nunca credenciais em código ou logs
- Tokens com vida útil definida
- HTTPS em produção
