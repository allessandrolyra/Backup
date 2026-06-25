---
name: estrategia-git
menu-code: GS
description: Estratégia Git (mirror/rebase/clean) com preservação e pós-migração.
---

# Estratégia de Migração Git

Definir a estratégia completa de migração de repositórios Git entre organizações/projetos Azure DevOps.

## 1. Seleção de Estratégia

Apresentar as três opções com comparação (tabela):

### Mirror (Recomendada na maioria dos casos)

- **O que preserva:** todo o histórico, todas as branches, todas as tags, refs
- **Quando usar:** migração padrão onde fidelidade é prioridade
- **Quando NÃO usar:** repo com histórico muito grande (>10 GB) ou com dados sensíveis no histórico

### Clean Migration

- **O que preserva:** snapshot atual das branches selecionadas
- **Quando usar:** repo com histórico problemático, dados sensíveis, ou quando se deseja "fresh start"
- **Quando NÃO usar:** quando auditoria ou rastreabilidade do histórico é requisito

### Rebase

- **O que preserva:** histórico reescrito/linearizado
- **Quando usar:** padronização de histórico (geralmente evitar)
- **Quando NÃO usar:** na maioria dos casos — altera hashes de commit e quebra referências

## 2. Inventário de Repos

Para cada repositório, coletar:

- Nome e tamanho (incluindo LFS)
- Quantidade de branches e tags
- Branch default
- Políticas de branch ativas
- Pipelines que referenciam este repo
- Submodules (se houver)
- LFS tracking patterns

## 3. Execução por Repo

Para cada repositório, gerar comandos com o formato obrigatório (objetivo, comando, explicação, risco, validação):

**Mirror:**

```bash
# Clone mirror da origem
git clone --mirror https://<PAT_ORIGEM>@dev.azure.com/<ORG_ORIGEM>/<PROJECT_ORIGEM>/_git/<REPO_NAME>

# Entrar no diretório
cd <REPO_NAME>.git

# Adicionar remote destino
git remote add target https://<PAT_DESTINO>@dev.azure.com/<ORG_DESTINO>/<PROJECT_DESTINO>/_git/<REPO_NAME>

# Push mirror para destino
git push --mirror target
```

**Clean Migration:**

```bash
# Clone normal (apenas branches desejadas)
git clone https://<PAT_ORIGEM>@dev.azure.com/<ORG_ORIGEM>/<PROJECT_ORIGEM>/_git/<REPO_NAME>
cd <REPO_NAME>

# Adicionar remote destino
git remote add target https://<PAT_DESTINO>@dev.azure.com/<ORG_DESTINO>/<PROJECT_DESTINO>/_git/<REPO_NAME>

# Push branches selecionadas
git push target --all
git push target --tags  # se quiser preservar tags
```

## 4. Validação Pós-Migração

Para cada repo migrado, validar:

```bash
# Comparar contagem de branches
git ls-remote --heads origin | wc -l
git ls-remote --heads target | wc -l

# Comparar contagem de tags
git ls-remote --tags origin | wc -l
git ls-remote --tags target | wc -l

# Comparar último commit da branch default
git log origin/<DEFAULT_BRANCH> -1 --format="%H %s"
git log target/<DEFAULT_BRANCH> -1 --format="%H %s"
```

## 5. Pós-Migração (OBRIGATÓRIO)

### Atualização de Remotes (instrução para devs)

Gerar comunicação para os desenvolvedores:

```bash
# Atualizar remote para novo repositório
cd <REPO_LOCAL>
git remote set-url origin https://dev.azure.com/<ORG_DESTINO>/<PROJECT_DESTINO>/_git/<REPO_NAME>
git fetch --all
git pull
```

### Reaplicar Proteções e Policies

- Branch policies (reviewers, build validation, merge strategy)
- Permissões por branch
- Status checks
- Auto-complete rules

### Congelamento/Arquivamento da Origem

**Somente com autorização explícita:**

- Tornar repo origem read-only (ou disabled)
- Adicionar README indicando migração e novo local
- Manter acessível por período definido (auditoria)
- Definir data de descomissionamento

## 6. Casos Especiais

### Repos com LFS

- Verificar que LFS storage está configurado no destino
- Migrar LFS objects: `git lfs fetch --all` → `git lfs push --all target`
- Validar LFS tracking patterns preservados

### Repos com Submodules

- Mapear dependências entre repos
- Migrar na ordem correta (dependências primeiro)
- Atualizar `.gitmodules` com novos URLs

### Repos Muito Grandes (>5 GB)

- Considerar migração incremental por branch
- Avaliar shallow clone se histórico completo não for necessário
- Planejar janela de transferência adequada

## Entregável

- Estratégia definida por repo (tabela: repo, estratégia, justificativa)
- Comandos prontos para execução (com placeholders)
- Plano de comunicação para devs
- Checklist de validação pós-migração
- Dossiê atualizado
