# Azure Observability & SRE

Azure Monitor, Log Analytics, Application Insights e cultura SRE.

## 1. Golden Signals
Sempre monitore e defina alertas para:
- **Latência:** Tempo para processar requests (p50, p95, p99).
- **Tráfego:** Demanda colocada no sistema (RPS).
- **Erros:** Rate de requests falhando (5xx, 4xx críticos).
- **Saturação:** Quão "cheio" está o serviço (CPU, memória, connections, IOPS).

## 2. SLO/SLI & Error Budgets
- **SLIs:** Métricas específicas que indicam sucesso (ex: % requests < 200ms, uptime).
- **SLOs:** Alvos de performance (ex: 99.9% de sucesso mensal).
- **Error Budget:** Se o orçamento de erro for estourado, priorizar estabilidade sobre novas features.
- **Error Budget Policy:** Definir ações claras quando budget ≤ 20% (feature freeze) e ≤ 0% (all-hands on reliability).

## 3. KQL (Kusto Query Language)
- **Log Analytics:** Queries para troubleshooting e detecção de padrões de erro.
- **Workbooks:** Dashboards dinâmicos para visualização de SRE.
- **Alertas baseados em KQL:** Log alerts para detecção de anomalias.
- **Exemplos Úteis:** Latência por endpoint, error rate trend, dependency failures.

## 4. Instrumentação & Observabilidade Avançada
- **OpenTelemetry (OTel):** Priorizar para tracing e instrumentação distribuída.
- **Application Insights:** Auto-instrumentation para .NET, Java, Node, Python.
- **Distributed Tracing:** Correlação cross-service com Correlation ID.
- **Métricas de Negócio:** Log de eventos de negócio para correlação com métricas técnicas.

## 5. Sampling & Custo
- **Sampling Strategies:** Definir taxas de amostragem para traces e logs.
- **Data Retention:** Ajustar retenção por workspace (30d default, 90d prod).
- **Ingestion Control:** Filtrar dados desnecessários na origem (não no destino).
- **Commitment Tiers:** Log Analytics Commitment Tiers para volumes altos.

## 6. Dashboards & Alertas
- **Azure Dashboard:** Visão executiva com KPIs de negócio e SLOs.
- **Grafana (Azure Managed):** Dashboards operacionais detalhados.
- **Alert Rules:** Baseados em métricas (near real-time) e logs (5min+).
- **Action Groups:** Notificações (email, Teams, PagerDuty) e automação (Logic Apps, Functions).
