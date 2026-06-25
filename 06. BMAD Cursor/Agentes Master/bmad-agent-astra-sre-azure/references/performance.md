# Azure Performance Engineering

Base de conhecimento para performance, testes de carga e capacity planning.

## 1. Métricas Alvo
- **Latência:** Focar em p95 e p99 (não apenas média).
- **Throughput:** Requests por segundo (RPS) esperado por tier.
- **Saturação:** CPU, memória, IOPS, connections — limites por SKU.
- **Error Rate:** % de erros 5xx como indicador de saturação.

## 2. Testes de Carga
- **Ferramentas:** k6 (script JS, lightweight), Locust (Python), Azure Load Testing (managed).
- **Cenários:** Baseline, stress, spike, soak (endurance).
- **Ambiente:** Testar em staging com dados representativos.
- **Automação:** Integrar testes de carga no pipeline CI/CD para regressões.

## 3. Capacity Planning
- **Baseline:** Medir carga real antes de projetar escala.
- **Auto Scaling:** Configurar com base em métricas de performance coletadas (não chutar).
- **Reservas vs On-Demand:** Workloads estáveis em Reserved Instances; bursts em on-demand.
- **Limits & Quotas:** Conhecer limites de subscription, region e por-recurso.

## 4. Otimização por Camada
- **Compute:** Escolher SKU adequada (B-series dev, D-series geral, E-series memória).
- **Storage:** Premium SSD para IOPS, Standard para archival. Tier automático se possível.
- **Database:** DTU vs vCore, read replicas para distribuir carga de leitura.
- **Cache:** Azure Cache for Redis para reduzir latência de hot paths.
- **CDN/Front Door:** Cache de conteúdo estático próximo ao usuário.

## 5. Profiling & Troubleshooting
- **App Insights Profiler:** Identificar hot paths no código.
- **Snapshot Debugger:** Capturar estado em exceções de produção.
- **KQL Performance Queries:** Consultas para identificar endpoints lentos.
- **Dependency Tracking:** Mapear latência de chamadas externas (SQL, APIs, Storage).

## 6. Toil Reduction
- **Automação de Runbooks:** Documentar e automatizar procedimentos operacionais repetitivos.
- **Medição:** Estimar % de tempo gasto em toil antes e depois da automação.
- **Scripts Reutilizáveis:** Manter biblioteca de scripts operacionais (az cli, PowerShell).
