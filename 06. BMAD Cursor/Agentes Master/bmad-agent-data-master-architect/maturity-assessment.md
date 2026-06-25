---
name: maturity-assessment
description: Maturity Assessment — avaliação de maturidade e roadmap de evolução
menu-code: MA
---

**Language:** Use `{communication_language}` for all output.

# Maturity Assessment

Avalie a maturidade da plataforma de dados e gere um roadmap de evolução.

## Modelo de Maturidade — 5 Níveis

| Nível | Nome | Características |
|---|---|---|
| 1 | **Ad-hoc** | Processos manuais, sem padrão, dependência de pessoas |
| 2 | **Padronizado** | Processos documentados, padrões definidos, ainda manual |
| 3 | **Governado** | Catálogo, qualidade, ownership, políticas formais |
| 4 | **Automatizado** | CI/CD, testes automáticos, observabilidade, self-service |
| 5 | **AI-Driven Platform** | IA nativa, auto-otimização, data products, plataforma como produto |

## Dimensões de Avaliação

### 1. Dados
| Critério | Nível 1 | Nível 3 | Nível 5 |
|---|---|---|---|
| Modelagem | Planilhas, ad-hoc | Star Schema padronizado | Data Products, contratos |
| Ingestão | Manual, scripts | Pipelines orquestrados | Real-time, self-service |
| Qualidade | Sem controles | Testes básicos | Data Contracts, anomaly detection |

### 2. Governança
| Critério | Nível 1 | Nível 3 | Nível 5 |
|---|---|---|---|
| Catálogo | Inexistente | Purview/Unity Catalog | Business glossary ativo |
| Lineage | Desconhecido | Automatizado | Impact analysis em tempo real |
| Ownership | Ninguém responsável | Data owners definidos | Data mesh com domínios |

### 3. Segurança
| Critério | Nível 1 | Nível 3 | Nível 5 |
|---|---|---|---|
| Acesso | Compartilhado | RBAC por grupo | ABAC, just-in-time, zero trust |
| Encryption | Sem encryption | At rest | At rest + in transit + column-level |
| Auditoria | Sem logs | Logs básicos | SIEM integrado, automação |

### 4. Observabilidade
| Critério | Nível 1 | Nível 3 | Nível 5 |
|---|---|---|---|
| Monitoramento | Nenhum | Alertas básicos | SLIs/SLOs, error budgets |
| Logs | Console manual | Centralizado | Structured logging, tracing |
| Incident response | Reativo | Playbooks | Auto-remediation |

### 5. DataOps
| Critério | Nível 1 | Nível 3 | Nível 5 |
|---|---|---|---|
| Versionamento | Nenhum | Git para código | Git para código + dados + config |
| CI/CD | Manual | Pipelines básicos | Full automation, DORA metrics |
| Testes | Nenhum | Unit tests | Unit + integration + data + contract |

### 6. IA
| Critério | Nível 1 | Nível 3 | Nível 5 |
|---|---|---|---|
| Uso de IA | Nenhum | Experimentação | RAG, agents, copilots em produção |
| MLOps | Ad-hoc | MLflow tracking | Full MLOps, model monitoring |
| Data for AI | Dados desorganizados | Vector store básico | Knowledge graphs, agentic pipelines |

## Processo

1. **Aplicar assessment** — Avaliar cada dimensão com o usuário
2. **Pontuar** — Nível 1-5 por dimensão
3. **Identificar gaps** — Diferença entre atual e desejado
4. **Priorizar** — Quick wins vs investimentos estratégicos
5. **Gerar roadmap** — Timeline com milestones por dimensão

## Progressão

- **Passo 1 → 2:** Após avaliar cada dimensão com o usuário, confirmar pontuações antes de prosseguir
- **Passo 2 → 3:** Após identificar gaps, confirmar prioridades com o usuário
- **Passo 3 → 4:** Após priorizar, prosseguir para gerar roadmap
- **Passo 4 → 5:** Após apresentar roadmap, perguntar se deseja detalhar quick wins específicos

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Scorecard de maturidade (radar chart textual)
- Gaps identificados por dimensão
- Roadmap priorizado com timeline
- Quick wins (impacto alto, esforço baixo)
