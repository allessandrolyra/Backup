---
name: ambientes
description: Define ambientes e variáveis
menu-code: AM
---

# Ambientes

Guie o usuário na definição de ambientes — dev, staging, prod e variáveis.

## Processo

1. **Entenda o contexto** — Web, Android ou iOS? Onde roda cada ambiente?

2. **Ambientes típicos:**
   - **dev** — local ou cloud, dados de teste
   - **staging** — espelho de prod, validação antes do deploy
   - **prod** — produção, dados reais

3. **Variáveis por ambiente:**
   - API_URL, API_KEY
   - Feature flags
   - Log level (dev: debug, prod: warn)
   - Nunca secrets em código — usar variáveis de ambiente

4. **Configuração:**
   - .env.example (template sem valores sensíveis)
   - .env.local (gitignore) para dev
   - Secrets no CI (GitHub Secrets, etc.) para staging/prod

5. **Memória** — Se decisões importantes, sugira salvar (SM).

## Regras

- Um ambiente = um conjunto de variáveis
- Prod nunca herda de dev
- Documentar variáveis obrigatórias em .env.example
