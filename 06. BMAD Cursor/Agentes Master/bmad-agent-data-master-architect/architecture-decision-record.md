---
name: architecture-decision-record
description: ADR — registro de decisões arquiteturais com trade-offs e consequências
menu-code: AR
---

**Language:** Use `{communication_language}` for all output.

# Architecture Decision Record (ADR)

Produza ADRs formais quando houver múltiplas opções técnicas para documentar decisões arquiteturais.

## Quando Produzir ADR

- Escolha entre plataformas (Fabric vs Databricks vs Snowflake)
- Escolha de abordagem (Kimball vs Data Vault, batch vs streaming)
- Escolha de tecnologia (dbt vs Spark, Terraform vs Bicep)
- Migração strategy (lift-and-shift vs re-architecture)
- Trade-off significativo (custo vs performance vs complexidade)

## Formato Obrigatório

### ADR-{número}: {Título da Decisão}

**Status:** Proposto | Aceito | Rejeitado | Substituído por ADR-{n}
**Data:** {data}
**Decisores:** {quem participa da decisão}

### 1. Contexto

Descrever o problema, requisitos, restrições e contexto organizacional que motivam esta decisão.

### 2. Alternativas

Para cada alternativa:
- **Nome da alternativa**
- Descrição técnica
- Arquitetura resumida
- Pré-requisitos

### 3. Critérios de Avaliação

Definir critérios com peso:

| Critério | Peso | Descrição |
|---|---|---|
| Performance | Alto | Latência, throughput, escalabilidade |
| Custo | Alto | TCO (licenças + infra + operação) |
| Governança | Médio | Catálogo, lineage, compliance |
| Complexidade | Médio | Curva de aprendizado, operação |
| Escalabilidade | Alto | Crescimento de dados e usuários |
| Segurança | Alto | Encryption, access control |
| Ecossistema | Baixo | Integração com stack existente |

### 4. Trade-offs

Tabela comparativa:

| Critério | Alternativa A | Alternativa B | Alternativa C |
|---|---|---|---|
| Performance | ... | ... | ... |
| Custo | ... | ... | ... |
| ... | ... | ... | ... |

### 5. Decisão

Declarar a decisão escolhida com justificativa clara.

### 6. Consequências

**Positivas:**
- O que melhora com esta decisão

**Negativas:**
- O que piora ou é limitado

**Neutras:**
- Impactos sem julgamento de valor

### 7. Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| ... | Alta/Média/Baixa | Alto/Médio/Baixo | ... |

### 8. Plano de Revisão

- **Revisão em:** {prazo} ou {trigger event}
- **Métricas de sucesso:** Como medir se a decisão foi correta
- **Critérios de reversão:** Quando reconsiderar

## Processo

1. **Entender o contexto** — Perguntar sobre o problema e restrições
2. **Levantar alternativas** — Mínimo 2, idealmente 3
3. **Definir critérios** — Com o usuário, adaptar pesos ao contexto
4. **Avaliar** — Analisar cada alternativa por critério
5. **Recomendar** — Com justificativa fundamentada
6. **Documentar** — Gerar ADR formal
7. **Registrar no Ledger** — Salvar via `[SM] - Save Memory`

## Progressão

- **Passo 1 → 2:** Após entender o contexto, confirmar com o usuário antes de levantar alternativas
- **Passo 2 → 3:** Após apresentar alternativas, confirmar critérios de avaliação com o usuário
- **Passo 3 → 4:** Após avaliar, apresentar trade-offs e pedir confirmação antes de declarar recomendação
- **Passo 5 → 6:** Após o usuário aceitar decisão, gerar ADR formal completo
- **Passo 7:** Após ADR gerado, perguntar se deseja registrar no Project Ledger via `[SM]`

## Saída

O ADR é o formato de saída principal desta capability. Seguir o formato obrigatório acima integralmente.
