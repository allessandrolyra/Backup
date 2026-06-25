---
name: modelar-dados
description: Guia modelagem de dados
menu-code: MD
---

# Modelar Dados

Guie o usuário na modelagem de dados — entidades, relações e normalização.

## Processo

1. **Entenda o domínio** — O que o produto precisa armazenar? (da Paula ou conversa)

2. **Identifique entidades:**
   - Quais são as entidades principais?
   - Quais atributos cada uma tem?
   - Quais as relações entre elas? (1:1, 1:N, N:N)

3. **Normalização:**
   - Até qual forma normal? (geralmente 3NF para dados transacionais)
   - Há redundância aceitável por performance? (desnormalização consciente)

4. **SQL vs NoSQL:**
   - Dados relacionais → SQL (PostgreSQL, MySQL, etc.)
   - Dados documentais/JSON → NoSQL (MongoDB, etc.)
   - Dados em cache → Redis, etc.
   - Consulte a arquitetura (Wagner) e requisitos (Paula) para alinhamento

5. **Documente** — Resuma decisões. Sugira definir schema (DS) quando houver clareza.

6. **Memória** — Se decisões importantes, sugira salvar (SM).

## Regras

- Integridade primeiro
- Evitar over-engineering — schema evolui
- Alinhado à arquitetura do projeto
