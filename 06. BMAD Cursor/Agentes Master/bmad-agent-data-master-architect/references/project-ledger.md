# Project Ledger Structure

Estrutura obrigatória do Project Ledger para Atlas Data Master Architect.

## Template do index.md

```markdown
# Project Ledger — {nome-do-projeto}

**Última atualização:** {data}
**Arquiteto:** Atlas (Data Master Architect)

## A. Contexto do Projeto

| Campo | Valor |
|---|---|
| Nome | {nome} |
| Objetivo | {objetivo} |
| Cloud Provider(s) | {clouds} |
| Plataforma Analítica | {plataforma} |
| Bancos de Dados | {bancos} |
| Camada de BI | {bi} |
| Stack de Ingestão | {ingestao} |
| Ambientes | {ambientes} |
| Governança | {governanca} |
| IaC / CI-CD | {iac-cicd} |

## B. Decisões Arquiteturais (ADR Log)

| # | Data | Decisão | Alternativas Avaliadas | Trade-off Principal | Status |
|---|---|---|---|---|---|
| ADR-001 | {data} | {decisão} | {alternativas} | {trade-off} | Aceito |

## C. Artefatos Gerados

| Data | Artefato | Capability | Descrição |
|---|---|---|---|
| {data} | {nome-artefato} | {capability-code} | {breve-descrição} |

## D. Estado Atual da Plataforma

| Dimensão | Nível Atual (1-5) | Nível Alvo | Próximo Passo |
|---|---|---|---|
| Dados | - | - | - |
| Governança | - | - | - |
| Segurança | - | - | - |
| Observabilidade | - | - | - |
| DataOps | - | - | - |
| IA | - | - | - |

## E. Troubleshooting Log

| Data | Problema | Classificação | Causa Raiz | Solução | Prevenção |
|---|---|---|---|---|---|

## F. Otimizações e FinOps

| Data | Otimização | Componente | Impacto Custo | Impacto Performance |
|---|---|---|---|---|

## G. Padrões e Convenções

- Naming: {convention}
- Tagging: {tags-obrigatorias}
- Branching: {strategy}
- Preferências do usuário: {preferencias}

## H. Riscos e Pendências

| Prioridade | Risco/Pendência | Impacto | Mitigação | Status |
|---|---|---|---|---|
```

## Regras de Atualização

1. **Nunca sobrescrever** — Sempre adicionar novas entradas com data
2. **Seção H no topo** — Riscos e pendências são sempre a primeira coisa a revisar
3. **ADRs são permanentes** — Nunca excluir, marcar como "Substituído por ADR-N" se revisado
4. **Condensar periodicamente** — Mover itens antigos de C/E/F para chronology.md
