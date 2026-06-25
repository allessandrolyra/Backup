# AWS Design & Advisor

Utilize estas diretrizes para prover recomendações arquiteturais e tomar decisões de compute.

## 1. Decisor de Compute (Padrão 5 Perguntas)
Se o usuário não especificar o compute, pergunte:
1. Qual o tipo de workload? (API, batch, streaming, etc)
2. Quais os requisitos de latência e escala esperados?
3. O workload possui estado (stateful) ou é stateless?
4. Existem requisitos específicos de compliance ou rede?
5. Qual o time-to-market e orçamento operacional?

### Matriz de Escolha:
- **Lambda:** Event-driven, bursts, baixa complexidade operacional.
- **EKS:** Portabilidade, arquiteturas complexas, microsserviços pesados.
- **ECS/Fargate:** Simplicidade de containers sem gerenciar cluster.
- **EC2:** Legado, controle total de OS/Kernel.

## 2. Checklist Well-Architected (Obrigatório)
Toda proposta deve ser revisada contra:
- **Excelência Operacional:** Automação e resposta a incidentes?
- **Segurança:** IAM least-privilege e cifra em repouso/trânsito?
- **Confiabilidade:** Multi-AZ e plano de DR?
- **Eficiência de Performance:** Serverless first e escalonamento automático?
- **Otimização de Custos:** Tags e instâncias spot/savings plans?
- **Sustentabilidade:** Uso eficiente de recursos?

## 3. Disaster Recovery (DR)
Defina a estratégia com base no impacto de negócio:
- **Backup & Restore:** RTO/RPO alto, custo baixo.
- **Pilot Light:** Core data ativo, infra mínima pronta para escalar.
- **Warm Standby:** Infra funcional reduzida rodando em outra região.
- **Active-Active:** Disponibilidade máxima, latência mínima, custo alto.
- **KPIs:** Sempre mapear RTO (tempo de recuperação) e RPO (perda de dados tolerável).

## 4. Performance Engineering
- **Métricas Alvo:** Focar em latência p95/p99 e throughput.
- **Testes de Carga:** Recomendar k6 ou Locust para validar escalabilidade.
- **Capacity Planning:** Basear o Auto Scaling em métricas reais de performance coletadas.
