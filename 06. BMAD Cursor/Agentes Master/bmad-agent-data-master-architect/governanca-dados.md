---
name: governanca-dados
description: Governança — Data Catalog, Lineage, Quality, Ownership, Stewardship
menu-code: GD
---

**Language:** Use `{communication_language}` for all output.

# Governança de Dados

Projete e implante frameworks de governança de dados corporativos: catálogo, lineage, qualidade, ownership e stewardship.

## Escopo

- **Data Catalog:** Purview, Unity Catalog, Lake Formation, Collibra, Alation
- **Data Lineage:** Rastreamento fim-a-fim (fonte → transformação → consumo)
- **Data Quality:** Regras, monitoramento, remediação, data contracts
- **Data Ownership:** Domínios, owners, stewards, RACI
- **Data Classification:** Sensibilidade (PII, PCI, PHI), categorização, tagging
- **Data Access:** Políticas de acesso, masking, tokenization, RLS

## Processo

Ao receber um pedido de governança:

### NÍVEL 1 — Framework

1. **Assessment** — Estado atual da governança (ad-hoc → automatizado)
2. **Domínios de dados** — Definir domínios de negócio (vendas, finanças, RH, etc.)
3. **Papéis e responsabilidades:**

| Papel | Responsabilidade |
|---|---|
| Data Owner | Responsável pelo domínio, aprova políticas |
| Data Steward | Cuida da qualidade e metadata no dia-a-dia |
| Data Engineer | Implementa pipelines e controles técnicos |
| Data Consumer | Usa dados conforme políticas |

4. **Políticas** — Retenção, acesso, qualidade, privacidade

### NÍVEL 2 — Data Catalog

1. **Registrar fontes** — Databases, lakes, APIs, files
2. **Classificação automática** — PII, PCI, sensibilidade
3. **Business glossary** — Termos de negócio padronizados
4. **Ownership assignment** — Domínio → Owner → Steward

### NÍVEL 3 — Data Quality

1. **Regras de qualidade:**

| Dimensão | Exemplo |
|---|---|
| Completude | NOT NULL em campos obrigatórios |
| Unicidade | Primary keys sem duplicação |
| Validade | Formato de email, range de datas |
| Consistência | FK válidas, cross-source matching |
| Freshness | Dados atualizados dentro do SLA |
| Accuracy | Dados refletem a realidade |

2. **Implementação** — dbt tests, Great Expectations, Soda, Purview Data Quality
3. **Monitoramento** — Dashboards de qualidade, alertas, tendências
4. **Data Contracts** — Schema contracts entre produtores e consumidores

### NÍVEL 4 — Operação

1. **Lineage** — Rastreamento automático (Purview, Unity Catalog, dbt docs)
2. **Auditoria** — Logs de acesso, mudanças, compliance
3. **Métricas de governança** — Coverage, quality score, adoption
4. **Data mesh considerations** — Quando escalar para domínios descentralizados

## Progressão

- **NÍVEL 1 → 2:** Após confirmar framework e papéis com o usuário, prosseguir para configuração do catálogo
- **NÍVEL 2 → 3:** Após o usuário aprovar catálogo, prosseguir para regras de data quality
- **NÍVEL 3 → 4:** Após entregar regras e testes de qualidade, perguntar se deseja configurar operação contínua
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Framework de governança com papéis
- Configuração do catálogo de dados
- Regras de qualidade implementáveis
- Métricas de governança
