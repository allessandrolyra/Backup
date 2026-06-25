# Servicos da Arquitetura K6 para QA

## Visao geral
A arquitetura de `K6` foi desenhada para ser simples na PoC e reutilizar o mesmo racional operacional da proposta de `Selenium Grid`: integracao com `Azure DevOps`, `Self-hosted Agents`, seguranca por rede privada e observabilidade centralizada.

## Servicos e papeis

### 1. Azure DevOps
E o ponto de orquestracao. Recebe os scripts versionados, dispara a pipeline, executa stages de preparacao e publica os resultados da execucao.

### 2. Self-hosted Agent Pool
Executa a pipeline em ambiente controlado. E importante porque permite instalar `K6`, dependencias, certificados, bibliotecas e manter acesso privado aos ambientes Zurich.

### 3. VM K6 Executor
Maquina onde os testes de performance realmente rodam. Nela ficam o binario do `K6`, os arquivos de script e as configuracoes da execucao. Na PoC, uma VM dedicada normalmente basta.

### 4. Repositorio de Scripts K6
Local onde a equipe guarda os cenarios de carga, thresholds, variaveis por ambiente e parametros de autenticacao. Isso padroniza o uso da ferramenta e facilita a autonomia futura.

### 5. Azure Key Vault
Armazena segredos usados pelos testes, como tokens, usuarios tecnicos, senhas e chaves. Evita hardcode de credenciais nos scripts e na pipeline.

### 6. Storage Account
Recebe artefatos da execucao, como logs, arquivos exportados, relatorios e evidencias. Tambem pode servir como repositorio simples de saida para auditoria.

### 7. Azure Monitor
Coleta sinais de saude e eventos da infraestrutura. Ajuda a enxergar falhas operacionais, indisponibilidade e comportamento da execucao.

### 8. Log Analytics Workspace
Complementa o monitoramento com consulta centralizada de logs. E util para troubleshooting, comparacao entre execucoes e leitura tecnica da PoC.

### 9. Dashboards e Alertas
Transformam os dados da operacao em acompanhamento visual. Na PoC, podem ser simples, mas ja ajudam a mostrar autonomia, visibilidade e sustentacao.

### 10. VNet, Subnet, NSG e Acesso Privado
Garantem que o trafego de testes passe de forma controlada ate a aplicacao piloto. Isso e especialmente importante quando as APIs da Zurich nao devem ser expostas publicamente.

### 11. Aplicacao Piloto / APIs Zurich
E o alvo dos testes de performance. A recomendacao e iniciar por APIs pequenas e relevantes, para gerar dados reais sem elevar demais o risco da PoC.

## Fluxo operacional resumido
1. O time de QA cria ou ajusta scripts `K6`.
2. A execucao e iniciada manualmente ou pela pipeline.
3. O `Self-hosted Agent` prepara o job e aciona a `VM K6 Executor`.
4. A VM roda o `K6` contra a aplicacao piloto.
5. Resultados sao publicados em `Storage`.
6. Telemetria e eventos vao para `Azure Monitor` e `Log Analytics`.
7. O time Zurich consulta dashboards e usa a estrutura de forma autonoma.

## O que fica fora da PoC
- grandes testes distribuidos em varias maquinas
- tuning profundo de capacidade final
- execucao completa de campanha de carga em nome do cliente
- thresholds finais de producao

## Recomendacao de apresentacao
Explique a solucao como uma `trilha de performance` complementar:
- `Selenium Grid` valida comportamento funcional
- `K6` valida capacidade, resposta e estabilidade
- ambos reaproveitam a mesma disciplina de pipeline, runner, seguranca e observabilidade
