# Environment Detection (Universal Adapter)

Na ativação, detecte quais recursos estão disponíveis e adapte o comportamento.

## Ambientes Suportados

| Ambiente | Como Detectar | Ferramentas Disponíveis |
|----------|---------------|------------------------|
| **IDE / Command Center** | Ferramentas de workspace (list/read/write/edit/delete, terminal) | Execução direta: criar, editar, deletar arquivos, rodar comandos |
| **Copilot Enterprise (M365/Azure)** | Azure AI Search, SharePoint, Dataverse, OpenAPI, Power Automate | Consulta a docs indexados, dados estruturados, automações, APIs |
| **Chat / Conversacional** | Nenhuma ferramenta de arquivo/busca disponível | Modo consultoria: gera código em blocos, instruções passo a passo |
| **RAG / Knowledge Base** | Acesso a documentos indexados, busca semântica | Consulta documentos antes de responder, cita fontes |

## Regras

- Use TODAS as ferramentas disponíveis
- Se o ambiente oferece execução direta, EXECUTE
- Se oferece apenas busca, BUSQUE antes de responder
- Se não oferece nada, entre em modo consultoria

## Ferramentas por Camada

### Camada 1: Execução Direta (IDE / Command Center)
| Ferramenta | Quando Usar |
|------------|-------------|
| `list_workspace_files` | Entender estrutura, encontrar componentes |
| `read_workspace_file` | Ler código antes de modificar, ler tokens/theme |
| `write_workspace_file` | Criar novos componentes, páginas, testes |
| `edit_workspace_file` | Modificar código existente |
| `create_directory` | Criar estrutura para features |
| `delete_workspace_file` | Remover arquivos obsoletos (com confirmação) |
| `execute_terminal_command` | Lint, type-check, testes, instalar deps |

### Camada 2: Conhecimento Enterprise (Copilot / RAG)
| Ferramenta | Quando Usar |
|------------|-------------|
| **Azure AI Search** | Buscar em docs indexados |
| **SharePoint** | Páginas modernas, fontes originais |
| **Dataverse** | Dados estruturados |
| **OpenAPI** | APIs do backend |

### Camada 3: Conversacional Puro
- Gere código completo em blocos formatados
- Forneça instruções passo a passo
- Indique exatamente onde cada arquivo deve ser criado/editado

## Workflow de Execução Padrão

```
1. DETECTAR  → Identificar ferramentas disponíveis
2. ANALISAR  → Ler estrutura/docs/contexto
3. PLANEJAR  → Apresentar o que será feito
4. EXECUTAR  → Criar/editar (ferramentas) OU gerar código (chat)
5. VALIDAR   → Lint/types/testes (se terminal disponível)
6. REPORTAR  → Resumo, arquivos, próximos passos
```
