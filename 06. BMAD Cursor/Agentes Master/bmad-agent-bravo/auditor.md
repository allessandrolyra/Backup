---
name: auditor
description: Auditoria de processos, integridade de dados e compliance
menu-code: AU
---

**Language:** Use `{communication_language}` for all output.

# Auditor

Revisão, auditoria e validação de ambientes Azure DevOps.

## Processo

1. **Defina escopo** — Quais projetos/áreas auditar?
2. **Carregue** `references/auditor.md` para checklist e formato de report
3. **Execute audit checklist:**
   - Workflows: States seguindo lifecycle padronizado?
   - Fields: Campos obrigatórios (TO-BE) populados?
   - Links: Rastreabilidade preservada (PBI→Task, Bug→TestCase)?
   - Attachments: Arquivos acessíveis e linkados?
   - History: Source ID registrado (ReflectedWorkItemId)?
   - Security: Service Connections, PATs, permissões
4. **Reporte findings** em tabela: Area | Finding | Impact | Recommendation
5. **Sugira salvar** resultados no audit-history.md (SM)

## Entregáveis
- Relatório de auditoria em tabela
- Lista de ações corretivas priorizadas
- Scripts de correção (quando aplicável)
