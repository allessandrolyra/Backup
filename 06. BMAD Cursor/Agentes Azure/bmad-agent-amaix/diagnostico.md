---
name: diagnostico
menu-code: DG
description: Diagnóstico de problema — causa provável, evidência, ação imediata e definitiva.
---

# Diagnóstico de Problemas de Migração

Modo de resposta DIAGNÓSTICO: investigar e resolver problemas encontrados durante ou após a migração Azure DevOps.

## Formato de Resposta (OBRIGATÓRIO)

Toda resposta em modo diagnóstico DEVE seguir esta estrutura:

### 1. Sintoma Reportado

Repetir o problema exatamente como descrito pelo usuário, sem interpretação.

### 2. Causa Provável

Listar as causas mais prováveis em ordem de probabilidade:

```
1. [ALTA probabilidade] — Descrição da causa + por que é provável
2. [MÉDIA probabilidade] — Descrição da causa + por que é possível
3. [BAIXA probabilidade] — Descrição da causa + cenário em que ocorreria
```

### 3. Evidência para Confirmar

Para cada causa provável, indicar como confirmar:

```
Causa 1: executar [comando/verificação] e observar [resultado esperado]
Causa 2: verificar [local/configuração] e comparar com [referência]
```

Sempre fornecer comandos executáveis (com placeholders) quando possível.

### 4. Ação Imediata (Workaround)

O que fazer AGORA para desbloquear, mesmo que não seja a solução definitiva:

- Ação concreta com comando/passo
- Risco da ação imediata
- Quanto tempo ganha

### 5. Ação Definitiva (Root Cause Fix)

A solução que resolve a causa raiz:

- Passos detalhados
- Pré-requisitos
- Validação pós-correção

### 6. Prevenção

O que fazer para evitar que o problema ocorra novamente em futuras migrações.

## Problemas Comuns e Padrões de Diagnóstico

### Categoria: Repos/Git

- Push rejeitado (permissões, tamanho, policies)
- Histórico divergente após mirror
- LFS objects não migrados
- Submodules com referências quebradas
- Branch policies não aplicadas no destino

### Categoria: Pipelines

- Pipeline falha no destino (referências quebradas)
- Service connection não encontrada
- Variable group inacessível
- Agent pool sem agents
- Task group incompatível
- Environment approvals não configurados

### Categoria: Boards

- Work items com campos faltando
- Estados inválidos no destino
- Links quebrados (commits, PRs de repos não migrados)
- Anexos não migrados
- Histórico de revisões perdido

### Categoria: Integrações

- Webhook não dispara
- ServiceNow sync falha
- Service hook retorna erro
- Permissões insuficientes para connection

### Categoria: Permissões

- Acesso negado pós-migração
- Grupos de segurança não mapeados
- Pipeline não autorizada para connection/environment
- Branch policy blocks por falta de reviewer group

## Regras de Diagnóstico

- **Nunca adivinhar** — se a causa não é clara, indicar os passos de investigação para coletar mais dados.
- **Isolar variáveis** — sugerir testes que confirmem/eliminem uma causa de cada vez.
- **Verificar o óbvio primeiro** — permissões, conectividade, typos em nomes/URLs.
- **Comparar origem vs destino** — sempre que possível, comparar a configuração que funciona (origem) com a que não funciona (destino).

## Entregável

- Diagnóstico estruturado (5 seções acima)
- Comandos de verificação prontos para executar
- Dossiê atualizado com problema e resolução
