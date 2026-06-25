# Memory System for Atlas

**Memory location:** `{project-root}/_bmad/memory/bmad-agent-data-master-architect-ledger/`

## Core Principle

Tokens são caros. Lembrar apenas o que importa. Condensar tudo à essência.

## File Structure

### `index.md` — Project Ledger (Primary Source)

**Load on activation.** Contém:

**A. Contexto do Projeto**
- Nome, objetivo, cloud providers, plataformas
- Stack tecnológico (ingestão, processamento, BI, governança)
- Ambientes (dev/test/homolog/prod)

**B. Decisões Arquiteturais (ADR Log)**
- Data | Decisão | Alternativas | Trade-off | Status
- Registrar toda escolha entre alternativas

**C. Artefatos Gerados**
- Pipelines, queries SQL, modelos dimensionais, IaC, DAX
- Referência ao contexto e capability que gerou

**D. Estado Atual da Plataforma**
- Maturidade por dimensão (Dados, Governança, Observabilidade, DataOps, IA)
- Componentes implementados vs planejados

**E. Troubleshooting Log**
- Problemas diagnosticados com RCA
- Soluções aplicadas e prevenções

**F. Otimizações e FinOps**
- Otimizações aplicadas com impacto em custo/performance
- KPIs de custo monitorados

**G. Padrões e Convenções**
- Naming conventions, coding standards, tagging
- Preferências do usuário aprendidas

**H. Riscos e Pendências**
- Riscos identificados (sempre no topo, por prioridade)
- Itens pendentes e próximos passos

**Update:** Quando contexto essencial muda (imediatamente para dados críticos).

### `access-boundaries.md` — Access Control

**Load on activation.** Contém:
- **Read access** — Folders/patterns que o agente pode ler
- **Write access** — Folders/patterns que o agente pode escrever
- **Deny zones** — Folders explicitamente proibidos

### `patterns.md` — Padrões Aprendidos

**Load when needed.** Contém:
- Preferências do usuário descobertas ao longo do tempo
- Padrões recorrentes de arquitetura
- Convenções específicas do projeto

### `chronology.md` — Timeline

**Load when needed.** Contém:
- Resumos de sessão
- Eventos significativos (migrações, incidentes, releases)

## Memory Persistence Strategy

### Write-Through (Immediate Persistence)

Persistir imediatamente quando:
1. **Decisão arquitetural tomada** — ADRs, escolhas de tecnologia
2. **Artefato gerado** — pipeline, query, IaC, modelo
3. **Troubleshooting concluído** — RCA, solução, prevenção
4. **User requests save** — capability `[SM] - Save Memory`

### Checkpoint (Periodic Persistence)

Atualizar periodicamente após:
- N interações significativas (default: 5-10)
- Conclusão de uma capability/tarefa
- Quando arquivo cresce além do tamanho alvo

### Save Triggers

**Após estes eventos, sempre atualizar memória:**
- Decisão arquitetural entre alternativas (ADR)
- Conclusão de troubleshooting com RCA
- Geração de artefato complexo (pipeline, modelo, IaC)
- Resultado de maturity assessment
- Otimização de custo aplicada

## Write Discipline

Antes de escrever na memória:

1. **Vale lembrar?** — Se não → skip
2. **Mínimo de tokens** — Condensar à essência
3. **Qual arquivo?**
   - `index.md` → contexto essencial, trabalho ativo, decisões
   - `patterns.md` → preferências, padrões recorrentes
   - `chronology.md` → resumos de sessão, eventos
4. **Requer update do index?** — Se sim → atualizar

## Memory Maintenance

Regularmente (a cada poucas sessões):
1. **Condensar entradas verbosas** — Resumir à essência
2. **Podar conteúdo obsoleto** — Mover para chronology ou remover
3. **Consolidar padrões** — Merge de entradas similares
4. **Atualizar chronology** — Arquivar eventos passados significativos

## First Run

Se sidecar não existe, load `init.md` para criar a estrutura.
