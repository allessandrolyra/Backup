---
name: checklist
menu-code: CK
description: Checklist por componente com dependências e critérios de aceite.
---

# Checklist de Migração por Componente

Gerar checklists detalhados por componente Azure DevOps, cobrindo dependências críticas e critérios de aceite.

## Estrutura de Cada Checklist

Cada componente deve ter:

1. **Pré-requisitos** — o que deve estar pronto antes de migrar este componente
2. **Itens de execução** — passos concretos com checkbox
3. **Dependências críticas** — o que pode quebrar se não for validado
4. **Critérios de aceite** — como saber que a migração deste componente está completa
5. **Evidência obrigatória** — o que documentar/capturar como prova

## Checklists por Componente

### Azure Boards

**Pré-requisitos:**
- [ ] Process template destino configurado
- [ ] Custom fields mapeados (Field Mapping Plan)
- [ ] Áreas e Iterações criadas no destino
- [ ] Ferramenta de migração selecionada e configurada

**Execução:**
- [ ] Migrar work items (dry run)
- [ ] Validar mapeamento de campos
- [ ] Validar estados e transições
- [ ] Migrar links e relações (parent/child, related)
- [ ] Migrar anexos
- [ ] Migrar histórico de revisões
- [ ] Migrar work items (produção)
- [ ] Validar queries salvas
- [ ] Recriar/validar dashboards

**Dependências Críticas:**
- [ ] Links para commits/PRs referenciando repos já migrados
- [ ] Menções a service connections em descriptions
- [ ] URLs hardcoded para org/projeto origem

**Critérios de Aceite:**
- [ ] Contagem de work items origem = destino
- [ ] Amostra de 10% validada campo a campo
- [ ] Hierarquias parent/child preservadas
- [ ] Histórico de revisões visível

### Azure Repos

**Pré-requisitos:**
- [ ] Estratégia Git definida (mirror/clean/rebase)
- [ ] Repos destino criados
- [ ] Permissões de push configuradas

**Execução:**
- [ ] Clone/mirror de cada repo
- [ ] Push para destino
- [ ] Validar branches preservadas
- [ ] Validar tags preservadas
- [ ] Validar histórico de commits (amostra)
- [ ] Configurar branch policies no destino
- [ ] Configurar proteções de branch

**Dependências Críticas:**
- [ ] LFS objects (se usado)
- [ ] Submodules referenciando outros repos
- [ ] Build policies referenciando pipelines

**Critérios de Aceite:**
- [ ] Contagem de branches origem = destino
- [ ] Contagem de tags origem = destino
- [ ] Commit count amostral consistente
- [ ] Branch policies reaplicadas

### Pipelines

**Pré-requisitos:**
- [ ] Repos já migrados (pipelines referenciam repos)
- [ ] Service connections configuradas no destino
- [ ] Variable groups recriados
- [ ] Agent pools disponíveis
- [ ] Environments criados

**Execução:**
- [ ] Exportar/recriar pipeline definitions
- [ ] Atualizar referências (repo, service connection, variable group, pool)
- [ ] Testar cada pipeline (smoke run)
- [ ] Configurar triggers
- [ ] Configurar approvals/checks em environments
- [ ] Validar task groups migrados

**Dependências Críticas:**
- [ ] Service connections com tokens/secrets válidos
- [ ] Variable groups com secrets repopulados
- [ ] Agent pools com agents online
- [ ] Container registries acessíveis
- [ ] Feeds NuGet/npm referenciados

**Critérios de Aceite:**
- [ ] Cada pipeline executa com sucesso (ao menos smoke test)
- [ ] Triggers funcionando
- [ ] Approvals/checks configurados
- [ ] Logs sem erros de referência quebrada

### Service Connections

- [ ] Inventário completo das connections origem
- [ ] Classificação por tipo (Azure RM, Docker, GitHub, Generic, etc.)
- [ ] Recriação no destino (sem copiar secrets — reconfigurar)
- [ ] Validação de conectividade de cada connection
- [ ] Permissões configuradas (NÃO "grant access to all pipelines")

### Integrações (Service Hooks / Webhooks)

- [ ] Inventário de hooks ativos na origem
- [ ] Mapeamento de endpoints destino
- [ ] Recriação/reconfiguração no destino
- [ ] Teste de disparo (evento simulado)
- [ ] Validação de payload recebido no endpoint

### Segurança e Permissões

- [ ] Grupos de segurança mapeados
- [ ] Permissões por projeto validadas
- [ ] Permissões por repo validadas
- [ ] Permissões de pipeline validadas
- [ ] Least privilege aplicado

## Checklist Pré-Cutover (Gate Final)

- [ ] TODOS os checklists de componente completos
- [ ] Pipelines executando com sucesso
- [ ] Permissões/policies corretas
- [ ] Integrações testadas com evidência
- [ ] Smoke tests OK
- [ ] Rollback planejado e testado
- [ ] Comunicação para times preparada
- [ ] Janela de cutover confirmada

## Entregável

- Checklists completos em Markdown (com checkboxes)
- Dossiê atualizado com status de cada componente
