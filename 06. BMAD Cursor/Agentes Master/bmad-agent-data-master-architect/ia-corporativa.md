---
name: ia-corporativa
description: IA Corporativa — RAG, Agentic AI, LLMs, embeddings, vector search
menu-code: IA
---

**Language:** Use `{communication_language}` for all output.

# IA Corporativa

Projete e implante soluções de IA sobre dados corporativos: RAG, Agentic AI, LLMs, embeddings, vector search e knowledge graphs.

## Escopo

- **Plataformas:** Azure OpenAI, Azure AI Foundry, Amazon Bedrock, Databricks Mosaic AI, Snowflake Cortex, Copilot Studio, Microsoft Fabric AI
- **Frameworks:** LangChain, LangGraph, Semantic Kernel, AutoGen
- **Capacidades:** RAG, Agentic RAG, Multi-Agent Systems, Embeddings, Vector Search, Semantic Search, Knowledge Graph
- **Infraestrutura:** Vector databases (Azure AI Search, Pinecone, Weaviate, pgvector), chunking, indexing

## Processo

Ao receber um pedido de IA corporativa:

### NÍVEL 1 — Arquitetura

1. **Caso de uso** — Q&A sobre docs, assistente de dados, code generation, summarization, agentes
2. **Dados fonte** — Documentos, databases, wikis, APIs, data warehouse
3. **Padrão arquitetural:**

| Padrão | Quando Usar | Trade-off |
|---|---|---|
| RAG básico | Q&A sobre documentos, knowledge base | Simples, limitado a recuperação |
| Agentic RAG | Raciocínio complexo, multi-step | Poderoso, mais custoso e complexo |
| Multi-Agent | Orquestração de tarefas complexas | Máxima flexibilidade, governança crítica |
| Fine-tuning | Domínio muito específico, consistência | Performance, custo de treino |
| Embeddings + Search | Busca semântica, similaridade | Fundação para RAG, requer indexação |

4. **Modelo LLM** — GPT-4o, Claude, Llama, Mistral — critérios: qualidade, latência, custo, compliance

### NÍVEL 2 — Pipeline de Dados para IA

1. **Data preparation** — Extração, limpeza, chunking de documentos
2. **Chunking strategy:**

| Estratégia | Quando Usar |
|---|---|
| Fixed-size | Documentos uniformes, simplicidade |
| Semantic | Documentos com estrutura, contexto preservado |
| Recursive | Documentos longos e complexos |
| Parent-child | Hierarquias de informação |

3. **Embedding model** — text-embedding-ada-002, text-embedding-3-large, open source
4. **Vector indexing** — HNSW, IVF, configuração de dimensões e métrica
5. **Atualização incremental** — Pipeline para novos documentos sem reindexar tudo

### NÍVEL 3 — Implementação

1. **RAG pipeline** — Código completo (Python + framework)
2. **Prompt engineering** — System prompts, few-shot, chain-of-thought
3. **Guardrails** — Content filtering, grounding, citation, hallucination detection
4. **Evaluation** — Métricas de qualidade (relevance, faithfulness, answer similarity)

### NÍVEL 4 — Operação

1. **Monitoramento** — Latência, tokens, custo, qualidade das respostas
2. **Segurança** — Data access control, PII filtering, audit trail
3. **Governança** — Responsible AI, bias detection, transparency
4. **Custo** — Token optimization, caching, model selection por complexidade

## Progressão

- **NÍVEL 1 → 2:** Após confirmar caso de uso e padrão arquitetural com o usuário, prosseguir para pipeline de dados
- **NÍVEL 2 → 3:** Após o usuário aprovar pipeline e chunking strategy, prosseguir para implementação
- **NÍVEL 3 → 4:** Após entregar código funcional, perguntar se deseja configurar operação e monitoramento
- **A qualquer momento:** O usuário pode solicitar apenas um nível específico — respeitar o escopo pedido

## Saída

Sempre carregar `references/standard-output.md` e seguir o formato padrão de resposta.

Incluir:
- Arquitetura da solução de IA
- Pipeline de dados para IA (ingestão, chunking, embedding)
- Código funcional (Python, LangChain/Semantic Kernel)
- Guardrails e avaliação de qualidade
