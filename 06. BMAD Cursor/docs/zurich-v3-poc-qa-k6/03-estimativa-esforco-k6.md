# Estimativa de Esforco - PoC K6 Performance

## Premissas gerais
- Primeira configuracao de K6 integrado a esteira Azure DevOps
- Horas incluem gordura para aprendizado e troubleshooting
- Faixas: `minimo`, `maximo` e `referencia` (ponto medio pratico)
- Profissionais humanos, sem uso de agentes de IA

---

## Resumo por papel

| Papel              | Min (h) | Max (h) | Ref (h) |
|--------------------|---------|---------|---------|
| Arquiteto          | 18      | 28      | 23      |
| SRE / DevOps       | 28      | 44      | 36      |
| QA Performance     | 16      | 26      | 21      |
| **Total**          | **62**  | **98**  | **80**  |

---

## Detalhamento por atividade

### Arquiteto

| Atividade                                                        | Min | Max | Ref |
|------------------------------------------------------------------|-----|-----|-----|
| Levantamento tecnico e alinhamento com time QA Zurich            | 3   | 5   | 4   |
| Desenho da arquitetura K6 integrada a esteira existente          | 4   | 6   | 5   |
| Definicao do modelo de integracao pipeline + K6 + storage        | 3   | 5   | 4   |
| Definicao do padrao de scripts, thresholds e parametrizacao      | 3   | 5   | 4   |
| Premissas de capacity, rede e seguranca para a VM K6             | 2   | 3   | 3   |
| Apoio tecnico, revisoes e ajustes durante a configuracao         | 3   | 4   | 3   |

### SRE / DevOps

| Atividade                                                        | Min | Max | Ref |
|------------------------------------------------------------------|-----|-----|-----|
| Provisionamento da VM K6 Executor e rede                         | 6   | 8   | 7   |
| Instalacao e configuracao do K6 e dependencias na VM             | 4   | 6   | 5   |
| Configuracao do Self-hosted Agent Pool para performance          | 4   | 6   | 5   |
| Integracao com a esteira Azure DevOps existente                  | 4   | 8   | 6   |
| Integracao com Storage, Monitor e Log Analytics                  | 4   | 6   | 5   |
| Configuracao de alertas e dashboards basicos                     | 2   | 4   | 3   |
| Testes tecnicos, troubleshooting e estabilizacao inicial         | 4   | 6   | 5   |

### QA Performance

| Atividade                                                        | Min | Max | Ref |
|------------------------------------------------------------------|-----|-----|-----|
| Definicao dos cenarios piloto com equipe Zurich                  | 3   | 5   | 4   |
| Criacao dos scripts K6 para cenarios iniciais                    | 4   | 6   | 5   |
| Parametrizacao de thresholds e massa de teste                    | 2   | 4   | 3   |
| Execucao piloto e validacao dos resultados                       | 3   | 5   | 4   |
| Documentacao dos cenarios e modelo de uso para autonomia         | 2   | 3   | 3   |
| Apoio ao time Zurich para handover operacional                   | 2   | 3   | 2   |

---

## Estimativa em semanas

Considerando dedicacao parcial (nao exclusiva) e paralelismo entre papeis:

| Cenario         | Duracao estimada |
|-----------------|------------------|
| Otimista        | 2 semanas        |
| Referencia      | 3 semanas        |
| Conservador     | 4 semanas        |

---

## Observacoes
- A estimativa nao inclui execucao massiva de campanha de carga em nome do cliente
- O handover e a governanca de scripts fazem parte do escopo
- Se o K6 for configurado junto com o Selenium Grid (mesma janela de projeto), ha sinergia de esforco na infra base (rede, agent pool, monitor) que pode reduzir o total em 15-20%
