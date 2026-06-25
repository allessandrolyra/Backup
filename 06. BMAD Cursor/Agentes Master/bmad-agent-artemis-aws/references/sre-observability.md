# SRE & Observabilidade

Foco em confiabilidade e visibilidade total.

## 1. Golden Signals
Sempre monitore e defina alertas para:
- **Latência:** Tempo para processar requests.
- **Tráfego:** Demanda colocada no sistema.
- **Erros:** Rate de requests falhando.
- **Saturação:** Quão "cheio" está o serviço.

## 2. SLO/SLI & Error Budgets
- **SLIs:** Métricas específicas que indicam sucesso (ex: uptime, % requests abaixo de 200ms).
- **SLOs:** Alvos de performance (ex: 99.9% de sucesso mensal).
- **Error Budget:** Se o orçamento de erro for estourado, priorizar estabilidade sobre novas features.

## 3. Instrumentação & Observabilidade Avançada
- **OpenTelemetry:** Priorizar para tracing e instrumentação distribuída.
- **Correlation IDs:** Garantir rastreabilidade de ponta a ponta.
- **Sampling Strategies:** Definir estratégias de amostragem para traces e logs para controle de custo.
- **Dashboards:** Criar visões por serviço e visão executiva de impacto de negócio.

## 4. Padrões de Resiliência (Confiabilidade Avançada)
Sempre considere e projete para:
- **Retry com Exponential Backoff:** Para falhas transientes.
- **Circuit Breaker:** Para prevenir falhas em cascata.
- **Timeout & Fallback:** Garantir que o sistema degrade graciosamente.
- **Bulkhead Isolation:** Isolar recursos de workloads diferentes.

## 5. Chaos Engineering & GameDays
- **Testes de Falha:** Propor simulações de falha de AZ, latência injetada e falha de dependência.
- **GameDays:** Criar planos com hipóteses claras, execução controlada e métricas de sucesso.
- **Ferramentas:** AWS Fault Injection Simulator (FIS) ou simulações manuais via scripts.
