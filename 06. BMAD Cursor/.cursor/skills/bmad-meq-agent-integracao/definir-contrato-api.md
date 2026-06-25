---
name: definir-contrato-api
description: Define contrato de API
menu-code: DC
---

# Definir Contrato de API

Guie o usuário na definição do contrato de API — endpoints, payloads e versionamento.

## Processo

1. **Entenda o contexto** — API interna ou externa? REST ou GraphQL?

2. **Endpoints:**
   - Recursos e operações (CRUD ou ações específicas)
   - Métodos HTTP (GET, POST, PUT, PATCH, DELETE)
   - Paths consistentes (ex: /v1/users, /v1/users/:id)

3. **Payloads:**
   - Request body (JSON schema ou exemplo)
   - Response body
   - Status codes (200, 201, 400, 404, 500)
   - Headers relevantes

4. **Versionamento:**
   - URL (/v1/) ou header (Accept-Version)
   - Backward compatibility — como evoluir sem quebrar

5. **Documentação** — Sugira OpenAPI/Swagger quando o contrato estiver claro. Contrato documentado = fonte para testes de API (Quinn).

6. **Memória** — Se decisões importantes, sugira salvar (SM).

## Regras

- Contratos claros e estáveis
- Versionamento desde o início
- Documentação como contrato executável
