# Azure Reliability & Resilience

Base de conhecimento para o pilar Reliability do WAF (Azure Well-Architected Framework).

## 1. Princípios de Resiliência
- **SPOF:** Identificar e eliminar pontos únicos de falha.
- **Redundância:** Zone Redundant Storage (ZRS), recursos Zone-redundant.
- **Isolamento:** Subnets, NSGs, Private Links, Availability Zones.
- **Self-healing:** Auto-scaling, Health Probes (LB/App Gateway), restart policies.

## 2. Padrões Avançados de Resiliência
- **Retry com Exponential Backoff:** Para falhas transientes (SDK Azure já suporta).
- **Circuit Breaker:** Proteção contra falhas em cascata em microsserviços.
- **Bulkhead Isolation:** Isolar recursos de workloads diferentes.
- **Queue-based Load Leveling:** Service Bus ou Storage Queues para absorver picos.
- **Graceful Degradation:** Planejar comportamento quando dependências falham.
- **Timeout & Fallback:** Garantir que o sistema degrade graciosamente.

## 3. Chaos Engineering
- **Azure Chaos Studio:** Planejar experimentos de falha (AZ Down, Latency, DNS issue).
- **GameDays:** Planejamento e execução de testes de estresse operacional.
- **Hipóteses:** Cada experimento com hipótese clara, métrica de sucesso e blast radius.
- **Frequência:** Trimestral para workloads críticos.

## 4. Disaster Recovery (DR)
- **Estratégias:** Backup & Restore, Pilot Light, Warm Standby, Active-Active.
- **RTO/RPO:** Sempre mapear metas de tempo e perda de dados por workload.
- **Azure Site Recovery (ASR):** Padrão para replicação Cross-region de VMs.
- **Geo-Replication:** SQL Database, Cosmos DB, Storage Account.
- **Plano de Teste:** DR deve ser testado — não apenas documentado.

## 5. Well-Architected Framework (WAF) — Checklist Reliability
- Todos os recursos críticos são Zone-redundant?
- Health probes configurados e testados?
- Auto-scale configurado com métricas reais (não guess)?
- DR testado nos últimos 90 dias?
- SLAs de serviço Azure considerados no design (composite SLA)?
