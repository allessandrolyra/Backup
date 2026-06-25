---
name: docker-config
description: Configura Docker
menu-code: DC
---

# Configuração Docker

Guie o usuário na configuração de Docker — Dockerfile, compose e multi-stage.

## Processo

1. **Entenda o contexto** — App web (Node, Python, etc.) ou mobile? Monolito ou microserviços?

2. **Dockerfile:**
   - Multi-stage — build em um stage, runtime em outro (imagem menor)
   - .dockerignore — excluir node_modules, .git, etc.
   - Usuário não-root quando possível
   - Health check se aplicável

3. **Docker Compose (quando útil):**
   - app + db + cache
   - Volumes para persistência
   - Networks isoladas
   - Variáveis de ambiente por serviço

4. **Boas práticas:**
   - Imagem base mínima (alpine quando faz sentido)
   - Layers em ordem de mudança (dependências antes do código)
   - Tags versionadas (não latest em prod)

5. **Memória** — Se decisões importantes, sugira salvar (SM).

## Regras

- Imagem menor = deploy mais rápido
- Reprodutibilidade — mesmo Dockerfile, mesmo resultado
- Alinhado à arquitetura (Wagner)
