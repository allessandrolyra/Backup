---
name: plano-de-migracao
menu-code: PM
description: Plano de migração completo com fases, riscos, rollback e Dossiê.
---

# Plano de Migração Azure DevOps

Criar um plano de migração completo, aplicando todas as habilidades cross-cutting do SKILL.md (seleção de ferramentas, avaliação de complexidade, comparação de abordagens, pré-requisitos, stack completa).

## Roteamento por Contexto

- **Dossiê fornecido:** executar Delta Analysis — identificar lacunas críticas, riscos novos, mudanças desde última sessão, próximos passos.
- **Sem Dossiê:** iniciar do zero seguindo o fluxo completo abaixo.

## Fluxo de Planejamento

### 1. Descoberta (Discovery)

Coletar informações essenciais sobre a migração:

- **Origem e destino:** orgs, projetos, URLs
- **Escopo:** quais componentes (Boards, Repos, Pipelines, Integrações)
- **Volume:** quantidade de repos, work items, pipelines, anexos
- **Customizações:** process templates, custom fields, estados personalizados
- **Integrações ativas:** ServiceNow, Jira, webhooks, service hooks
- **Restrições:** janela de downtime, compliance, data limits
- **Times impactados:** quantidade, fusos, dependências

Aplicar a Regra de Assertividade: para informações de alto impacto que não foram fornecidas, marcar como FALTA CONFIRMAR. Para médio/baixo, assumir e marcar ASSUMIDO – CONFIRMAR.

### 2. Classificação de Complexidade

Aplicar habilidade cross-cutting de Avaliação de Complexidade: classificar como BAIXA | MÉDIA | ALTA | ENTERPRISE e calibrar o plano:

| Nível | Dry Runs | Validação | Automação | Hypercare |
|-------|----------|-----------|-----------|-----------|
| BAIXA | 1 | Amostral | Opcional | 1 semana |
| MÉDIA | 2 | Por componente | Recomendada | 2 semanas |
| ALTA | 3+ | Completa + automatizada | Obrigatória | 3-4 semanas |
| ENTERPRISE | 5+ | Completa + auditada | Obrigatória + CI | 4-8 semanas |

### 3. Seleção de Ferramentas por Componente

Para cada componente no escopo, aplicar habilidade cross-cutting de Seleção de Ferramentas:

**Boards:**
- Avaliar: ferramenta especializada (ex: nkdAgility) vs API/ETL custom vs export/import nativo
- Decidir estratégia de mapeamento: 1:1 (máxima fidelidade) vs transformação (custom fields/workflows)

**Repos:**
- Avaliar: git mirror vs import/clone vs clean migration
- Definir preservação: histórico, tags, branches, LFS

**Pipelines:**
- Avaliar: recriação manual vs scripts/API vs export/import
- Mapear dependências: variable groups, service connections, agent pools, environments

**Integrações:**
- Avaliar: recriação manual vs migração de configs vs conectores oficiais
- Mapear: service hooks, webhooks, endpoints externos

### 4. Transformação de Dados (Boards)

Quando houver diferenças de processo entre origem e destino:

- Mapear campos (source → target)
- Identificar incompatibilidades (tipos, estados, regras, campos obrigatórios, templates)
- Propor transformação (renomear/mapear valores/normalizar)

Sempre indicar impacto em:
- Histórico (revisões/auditoria)
- Links e relações (hierarquia, related, commits)
- Relatórios (queries, dashboards, analytics)

**Entregável:** Field Mapping Plan (YAML ou Markdown) + riscos.

### 5. Análise de Dependências

Listar e validar todas as dependências críticas:

- Service connections usadas em pipelines
- Variable groups e secrets
- Agent pools
- Environment approvals/checks
- Integrações externas (endpoints, tokens, IP allowlist)
- Referências hardcoded (URLs, IDs, nomes de projeto/repo)

Se houver risco ALTO e dependência NÃO validada → emitir: **"STOP: BLOQUEAR EXECUÇÃO ATÉ VALIDAR"** + checklist do que validar.

### 6. Plano por Fases

Estruturar com gates de entrada/saída/evidência:

1. **Descoberta** — inventário, mapeamento, premissas
2. **Preparação** — ambiente destino, ferramentas, acessos, dry run #1
3. **Execução** — migração incremental com validação por componente
4. **Validação** — testes automatizados, smoke tests, comparação amostral
5. **Cutover** — switch final, congelamento origem, comunicação
6. **Pós-Migração** — hypercare, monitoramento, estabilização

### 7. Montagem do Plano

Usar o Formato Padrão de Saída do SKILL.md (10 seções) e entregar:

- Dossiê atualizado (YAML)
- Plano por fases com gates
- Risk register
- Critérios de aceite (DoD)
- Plano de rollback
- Próximos passos priorizados [ALTO|MÉDIO|BAIXO]
