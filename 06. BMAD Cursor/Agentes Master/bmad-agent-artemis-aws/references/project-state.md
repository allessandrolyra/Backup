# Project State Memory System

O sistema de memória persistente do Artemis AWS deve ser carregado e atualizado em cada sessão interativa.

## Estrutura Obrigatória do Project State
O arquivo de memória localizado em `{project-root}/_bmad/memory/bmad-agent-artemis-aws-sidecar/index.md` deve seguir esta estrutura:

### A) Contexto do Projeto
- Nome, Objetivo, Stakeholders, Ambientes, Regiões, Contas.

### B) Decisões (com data)
- Registro histórico de escolhas arquiteturais e técnicas.

### C) Artefatos Gerados
- Repositórios, módulos, templates, dashboards criados.

### D) Variáveis e Parâmetros Chave
- CIDRs, Tags, Budgets, RTO/RPO, SLOs.

### E) Pendências / Próximos Passos
- Lista priorizada.

### F) Riscos e Assunções
- O que foi assumido por falta de info.

---

## Instruções para o Agente
- **Leitura:** Sempre leia o `Project State` ao iniciar.
- **Atualização:** Após cada mudança significativa ou decisão tomada, resuma as alterações e peça para atualizar o `Project State`.
- **Mudança de Contexto:** Se o usuário mudar um requisito, registre como "Decisão Alterada" e atualize os trade-offs.
