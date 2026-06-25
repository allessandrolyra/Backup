# Revisão do Modelo de Dados — Diana

**Revisor:** Diana (Especialista Banco de Dados)  
**Data:** 2025-03-19  
**Referência:** `architecture-estacionamento.md`

---

## 1. Análise do Modelo Proposto (Wagner)

### Pontos positivos
- Normalização adequada (3NF)
- Relações claras: config (singleton), mensalistas, entradas
- FK mensalista_id em entradas (nullable para rotativos)
- Uso de uuid PK
- timestamptz para datas

### Ajustes recomendados

| Item | Problema | Solução |
|------|----------|---------|
| **Entrada duplicada** | FR15 exige: placa não pode ter 2 entradas ativas | Índice único parcial: `UNIQUE(placa) WHERE saida_em IS NULL` |
| **Índices** | Queries frequentes sem índice | Adicionar índices (ver seção 2) |
| **Precisão decimal** | valor_hora, valor_pago | `numeric(10,2)` |
| **Config** | Nome inconsistente | `fracao_minima_minutos` (já correto) |
| **Constraint tipo** | enum ou check | `CHECK (tipo IN ('rotativo', 'mensalista'))` |

---

## 2. Schema Aprovado com Ajustes

### Índices recomendados

| Tabela | Índice | Uso |
|--------|--------|-----|
| entradas | (placa) WHERE saida_em IS NULL | Busca saída por placa, impede duplicata |
| entradas | (entrada_em) | Dashboard, listagem |
| entradas | (saida_em) | Contagem ocupadas (WHERE saida_em IS NULL) |
| mensalistas | (placa) UNIQUE | Validação na entrada |
| mensalistas | (validade_ate, ativo) | Listar mensalistas ativos |

---

## 3. Veredicto

**Modelo aprovado** com os ajustes acima. Migrations prontas para implementação.

---

*Revisão Diana — Integridade primeiro. Schema evolui.*
