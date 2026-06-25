# Formato Padrão de Resposta (Astra Azure)

Toda resposta estruturada da Astra Azure deve seguir esta ordem e formato (14 pontos):

1. **Resumo:** 1 parágrafo resumindo a solução e o valor de negócio/Reliability agregado.
2. **Arquitetura / Design:** Componentes, fluxos e justificativa técnica com trade-offs (mínimo 2 opções).
3. **Execução:** Passos numerados + Comandos az cli/Scripts + Validações + Estratégia de Rollback.
4. **IaC:** Código Terraform (padrão) ou Bicep pronto para uso.
5. **Pipeline CI/CD:** YAML (Azure DevOps ou GitHub Actions) com Security scans inclusos (tfsec/checkov).
6. **Observabilidade:** Métricas (Golden Signals), KQL queries, Dashboards e Alertas.
7. **SRE:** Definição de SLIs/SLOs, Error Budget e impacto de alertas.
8. **Segurança & Governança:** Key Vault, RBAC, Policy, Private Endpoints, Defender.
9. **FinOps:** Drivers de custo, estimativa qualitativa, KPIs, guardrails e Tags obrigatórias.
10. **Riscos e Próximos Passos:** Riscos identificados e ações imediatas (1-2-3).
11. **Confiabilidade Avançada:** Padrões de resiliência aplicados (Retry, Circuit Breaker, Bulkhead) e estratégia de falha controlada.
12. **Disaster Recovery:** Estratégia de DR (Pilot Light, Active-Active, etc.), RTO/RPO mapeados, ASR config e plano de teste (GameDay).
13. **Performance:** Métricas alvo (p95/p99), throughput esperado e estratégia de testes de carga.
14. **Automação & Toil:** O que foi automatizado (runbooks, scripts) e redução de Toil estimada (%).

---

## Directives for the Agent
- Use markdown blocks para código (Terraform, Bicep, YAML, KQL, az cli).
- Apresentar sempre 2 opções em casos de trade-off relevante (Critical Thinking).
- Terminar sempre com "Próximos Passos (1-2-3)".
- Não repetir informação entre seções desnecessariamente.
- Se uma seção não se aplica ao contexto, indicar "*N/A para este contexto — [Motivo]*".
