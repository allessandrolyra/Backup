---
name: definir-schema
description: Define schema para tabelas/coleções
menu-code: DS
---

# Definir Schema

Defina o schema (DDL ou estrutura) para as tabelas ou coleções.

## Processo

1. **Entenda a modelagem** — Da memória ou conversa anterior (MD).

2. **Para SQL (PostgreSQL, MySQL, etc.):**
   - CREATE TABLE com colunas, tipos, constraints
   - PRIMARY KEY, FOREIGN KEY
   - Índices necessários
   - Considerar migrations (MG) para evolução

3. **Para NoSQL (MongoDB, etc.):**
   - Estrutura de documentos
   - Índices para queries frequentes
   - Embedding vs referência

4. **Boas práticas:**
   - Nomes consistentes (snake_case)
   - Timestamps (created_at, updated_at) quando apropriado
   - Soft delete quando necessário

5. **Output** — Gere o DDL ou estrutura. Sugira salvar (SM).

## Regras

- Seguir convenções do projeto
- Schema versionado (migrations)
- Índices para queries conhecidas
