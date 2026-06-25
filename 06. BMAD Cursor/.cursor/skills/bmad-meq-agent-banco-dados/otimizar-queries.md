---
name: otimizar-queries
description: Analisa e otimiza queries
menu-code: OQ
---

# Otimizar Queries

Analise e otimize queries para melhor performance.

## Processo

1. **Receba a query** — SQL ou pipeline (NoSQL).

2. **Análise:**
   - O que a query faz? (leitura, agregação, join)
   - Quais tabelas/coleções envolvidas?
   - Há EXPLAIN/EXPLAIN ANALYZE disponível?

3. **Problemas comuns:**
   - Full table scan → índice faltando
   - N+1 queries → batch ou join
   - JOINs pesados → desnormalização ou materialized view
   - Ordenação em grandes volumes → índice ou paginação

4. **Sugestões:**
   - Índices recomendados
   - Reescrever query se necessário
   - Cache quando apropriado

5. **Documente** — Registre otimizações. Sugira salvar (SM).

## Regras

- Medir antes e depois
- Índice tem custo em writes — balancear
- Evitar otimização prematura
