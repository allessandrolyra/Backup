---
name: execucao-assistida
menu-code: EX
description: Instalação de ferramentas, execução de scripts e configuração do ambiente (requer autorização).
---

# Execução Assistida

Quando o usuário autorizar explicitamente, o agente pode sair do modo advisory e executar ações reais para concluir a migração. Esta capability opera sob um protocolo rígido de 5 gates.

**REGRA FUNDAMENTAL:** Esta capability só é ativada com autorização explícita do usuário (ex: "pode executar", "autorizo", "vai em frente").

## Categorias de Execução

### 1. Instalação de Ferramentas

Instalar e configurar ferramentas necessárias para a migração:

- **CLIs:** Azure CLI (`az`), extensão `az devops`, Git, PowerShell modules
- **Ferramentas de migração:** nkdAgility Migration Tools, OpsHub, ferramentas open-source
- **Extensões Azure DevOps:** marketplace extensions no org destino
- **Dependências:** Python, Node.js, módulos PowerShell, pacotes NuGet

### 2. Execução de Código e Scripts

Executar scripts de migração, validação e automação:

- Scripts de migração Git (clone/mirror/push)
- Chamadas REST API (criação de projetos, work items, policies)
- Scripts de validação pós-migração (contagem, comparação, smoke tests)
- Execução de ferramentas de migração (dry run e produção)

### 3. Configuração de Ambiente

Realizar configurações no Azure DevOps destino:

- Criação/configuração de projetos, áreas, iterações
- Configuração de branch policies e proteções
- Setup de service connections (sem segredos — o usuário fornece via prompt seguro)
- Configuração de variable groups (estrutura apenas — secrets via UI ou vault)
- Setup de environments, approvals e checks
- Configuração de agent pools e permissões

---

## Protocolo de 5 Gates (OBRIGATÓRIO)

Toda execução real DEVE seguir este protocolo sequencialmente. Não pular gates.

### GATE 1 — Autorização Inicial

- O usuário deve dizer explicitamente que autoriza a execução
- Se não houver autorização clara → permanecer em modo advisory
- Registrar no Dossiê: `execucao_autorizada: true`, `autorizado_por: <nome>`, `data: <timestamp>`

### GATE 2 — Preview Obrigatório

Antes de executar QUALQUER ação, apresentar:

```
📋 PREVIEW DE EXECUÇÃO
━━━━━━━━━━━━━━━━━━━━━
Ação: [descrição clara do que será feito]
Comando: [comando exato]
Impacto: [o que muda no ambiente]
Risco: [ALTO|MÉDIO|BAIXO]
Reversível: [Sim/Não — se sim, como reverter]
━━━━━━━━━━━━━━━━━━━━━
Confirma execução? (s/n)
```

Aguardar confirmação explícita antes de prosseguir.

### GATE 3 — Pré-Requisitos

Validar que todos os pré-requisitos estão atendidos:

- Ferramentas instaladas e funcionando
- Permissões suficientes para a ação
- Conectividade com endpoints necessários
- Tokens/credenciais configurados (sem pedir valores)
- Admin/sudo quando necessário para instalações

Se faltar algo → BLOQUEAR e listar exatamente o que falta.

### GATE 4 — Execução Controlada

- Executar ação por ação, NUNCA em batch sem supervisão
- Após cada ação, exibir:

```
✅ RESULTADO
━━━━━━━━━━━
Status: [SUCESSO | FALHA | PARCIAL]
Output: [resumo relevante]
Próxima ação: [o que vem a seguir]
```

- Se FALHA → parar, diagnosticar (usar capability [DG]), propor correção, aguardar autorização para continuar
- Manter log de execução para o Dossiê

### GATE 5 — Validação Pós-Ação

- Após cada ação executada, rodar validação correspondente
- Registrar evidência no Dossiê (comando, output, status, timestamp)
- Se validação falhar → emitir alerta e propor rollback da ação

---

## Classificação de Risco por Tipo de Ação

| Risco | Tipo de Ação | Gates Necessários |
|-------|-------------|-------------------|
| **BAIXO** | Instalação de CLI/ferramenta, leitura de configs, dry run | Preview + Confirmação |
| **MÉDIO** | Clone/mirror de repos, criação de projeto, import de work items | Preview + Confirmação + Validação |
| **ALTO** | Push para destino, configuração de policies/permissions, cutover | Preview + Confirmação + Validação + Rollback preparado |
| **CRÍTICO** | Ações destrutivas (arquivar/desativar origem, alterar permissões prod) | Preview + Confirmação DUPLA + Rollback testado + Aprovação adicional |

Para ações CRÍTICAS, solicitar confirmação dupla:
1. Preview normal → "Confirma?"
2. Reforço: "Esta ação é CRÍTICA e pode ser irreversível. Confirma novamente com 'CONFIRMO'?"

---

## Anti-Patterns de Execução (NUNCA FAZER)

- Executar múltiplas ações destrutivas em sequência sem validação intermediária
- Executar em produção sem dry run prévio bem-sucedido
- Instalar ferramentas sem verificar compatibilidade de versão
- Executar scripts com segredos hardcoded (sempre variáveis de ambiente)
- Continuar execução após falha sem diagnóstico e autorização
- Assumir permissões de admin sem verificar
- Modificar org/projeto origem sem autorização explícita

## Entregável

- Log de execução completo (ações, status, outputs, timestamps)
- Evidências de validação por ação
- Dossiê atualizado com registro de execução
- Lista de ações pendentes (se fluxo foi interrompido)
