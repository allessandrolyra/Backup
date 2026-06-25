---
stepsCompleted: ["step-01-init.md", "step-02-discovery.md", "step-02b-vision.md", "step-02c-executive-summary.md", "step-03-success.md", "step-04-journeys.md", "step-05-domain.md", "step-06-innovation.md", "step-07-project-type.md", "step-08-scoping.md", "step-09-functional.md", "step-10-nonfunctional.md", "step-11-polish.md", "step-12-complete.md"]
inputDocuments: ["product-brief-estacionamento.md"]
workflowType: prd
date: 2025-03-19
author: Alessandro Lyra
---

# Product Requirements Document — Sistema Web de Gerenciamento de Estacionamento

**Autor:** Alessandro Lyra  
**Data:** 2025-03-19  
**Fonte:** Product Brief `product-brief-estacionamento.md`

---

## 1. Executive Summary

Sistema web para gerenciamento de estacionamentos de médio porte (80 vagas), com controle de entrada/saída, vagas em tempo real, sinalização de lotado e gestão financeira. Acessível via navegador, responsivo, com painel administrativo. Deploy gratuito (GitHub + Vercel/Railway).

**Problema:** Estacionamentos precisam de controle eficiente sem custo de licença.

**Solução:** Sistema web open-source, responsivo, com arquitetura preparada para gateway de pagamento futuro.

---

## 2. Vision & Problem Statement

### Problem Statement

Estacionamentos de médio porte enfrentam dificuldade para gerenciar entrada/saída, controle de vagas, mensalistas e faturamento com ferramentas acessíveis. Soluções proprietárias são caras; planilhas não escalam.

### Proposed Solution

Sistema web responsivo que registra entrada/saída, controla 80 vagas em tempo real, sinaliza lotado, cadastra mensalistas, gerencia faturamento interno e oferece painel administrativo.

---

## 3. Success Criteria

| Critério | Métrica |
|----------|---------|
| Operação rápida | Entrada/saída em < 30 segundos |
| Visibilidade | Vagas disponíveis/ocupadas sempre atualizadas |
| Lotado | Sinalização imediata quando 0 vagas |
| Mensalistas | Cadastro e validação em entrada funcionando |
| Uptime | Sistema operacional 24h |
| Precisão | Zero erros de cobrança por falha do sistema |

---

## 4. User Journeys

### Jornada Operador

1. Login no sistema
2. Acessa tela principal com vagas disponíveis/ocupadas em destaque
3. Registra entrada: informa placa, seleciona tipo (rotativo/mensalista)
4. Sistema valida mensalista (se aplicável) e registra entrada
5. Registra saída: informa placa, sistema calcula valor (rotativos) e exibe
6. Confirma saída e pagamento
7. Vê banner "LOTADO" quando 0 vagas disponíveis

### Jornada Administrador

1. Login no painel admin
2. Cadastra mensalista: nome, placa, validade
3. Configura tarifas (valor por hora, fração mínima)
4. Acompanha ocupação e faturamento no dashboard

---

## 5. Domain Requirements

- **Vagas:** Capacidade fixa de 80 vagas
- **Tipos de veículo:** Rotativo (paga na saída) e Mensalista (cadastrado, sem cobrança por permanência)
- **Tarifação:** Configurável (valor/hora, fração mínima)
- **Placa:** Identificador único por entrada ativa (um veículo por vaga)

---

## 6. MVP Scope

### In Scope (MVP1)

- Entrada/saída de veículos
- Controle de 80 vagas em tempo real
- Sinalização de lotado
- Cadastro manual de mensalistas
- Painel administrativo
- Tela principal com vagas disponíveis/ocupadas
- Gestão financeira interna
- Arquitetura preparada para gateway futuro

### Out of Scope (MVP1)

- Relatórios detalhados
- Integração com gateway de pagamento
- OCR/câmera para placa
- App mobile nativo

---

## 7. Functional Requirements

### 7.1 Autenticação e Acesso

| ID | Requisito |
|----|-----------|
| FR1 | Operador pode fazer login com credenciais válidas |
| FR2 | Administrador pode fazer login com credenciais válidas |
| FR3 | Sistema diferencia permissões entre Operador e Administrador |
| FR4 | Usuário pode fazer logout |

### 7.2 Controle de Vagas

| ID | Requisito |
|----|-----------|
| FR5 | Sistema exibe quantidade de vagas disponíveis em tempo real |
| FR6 | Sistema exibe quantidade de vagas ocupadas em tempo real |
| FR7 | Sistema exibe total de vagas (80) |
| FR8 | Sistema exibe sinalização "LOTADO" quando 0 vagas disponíveis |
| FR9 | Sinalização de lotado é visível na tela principal |

### 7.3 Entrada de Veículos

| ID | Requisito |
|----|-----------|
| FR10 | Operador pode registrar entrada informando placa |
| FR11 | Operador pode selecionar tipo de veículo (rotativo ou mensalista) |
| FR12 | Sistema valida se mensalista está cadastrado e com validade ativa |
| FR13 | Sistema registra horário de entrada automaticamente |
| FR14 | Sistema impede entrada quando estacionamento está lotado |
| FR15 | Sistema impede entrada duplicada (placa já com entrada ativa) |

### 7.4 Saída de Veículos

| ID | Requisito |
|----|-----------|
| FR16 | Operador pode registrar saída informando placa |
| FR17 | Sistema localiza entrada correspondente e calcula valor (rotativos) |
| FR18 | Sistema exibe valor a pagar antes de confirmar saída |
| FR19 | Mensalistas não geram cobrança na saída |
| FR20 | Sistema registra horário de saída e libera a vaga |
| FR21 | Operador pode confirmar pagamento e finalizar saída |

### 7.5 Mensalistas

| ID | Requisito |
|----|-----------|
| FR22 | Administrador pode cadastrar mensalista com nome, placa e validade |
| FR23 | Administrador pode editar mensalista cadastrado |
| FR24 | Administrador pode inativar ou remover mensalista |
| FR25 | Sistema valida validade do mensalista na entrada |

### 7.6 Configuração e Tarifas

| ID | Requisito |
|----|-----------|
| FR26 | Administrador pode configurar valor por hora (rotativos) |
| FR27 | Administrador pode configurar fração mínima de cobrança |
| FR28 | Sistema aplica tarifas configuradas no cálculo de saída |

### 7.7 Painel Administrativo

| ID | Requisito |
|----|-----------|
| FR29 | Administrador visualiza dashboard com vagas disponíveis/ocupadas |
| FR30 | Administrador visualiza faturamento básico (rotativos do dia/período) |
| FR31 | Administrador visualiza lista de entradas ativas |

### 7.8 Arquitetura de Pagamento

| ID | Requisito |
|----|-----------|
| FR32 | Sistema possui camada abstrata (PaymentService) para processamento de pagamento |
| FR33 | MVP usa implementação interna (registro manual) |
| FR34 | Arquitetura permite troca futura por implementação com gateway sem alterar fluxo principal |

---

## 8. Non-Functional Requirements

### 8.1 Performance

| ID | Requisito |
|----|-----------|
| NFR1 | Tela principal deve carregar em < 3 segundos |
| NFR2 | Registro de entrada/saída deve completar em < 2 segundos |
| NFR3 | Atualização de vagas disponíveis/ocupadas deve ser em tempo real (sem refresh manual) |

### 8.2 Usabilidade

| ID | Requisito |
|----|-----------|
| NFR4 | Interface deve ser responsiva (mobile, tablet, desktop) |
| NFR5 | Operador deve conseguir registrar entrada/saída em < 30 segundos |
| NFR6 | Tela principal deve destacar vagas disponíveis e ocupadas de forma clara |

### 8.3 Segurança

| ID | Requisito |
|----|-----------|
| NFR7 | Credenciais devem ser armazenadas de forma segura (hash) |
| NFR8 | Sessão deve expirar após período de inatividade |
| NFR9 | Acesso admin restrito a usuários com perfil Administrador |

### 8.4 Disponibilidade

| ID | Requisito |
|----|-----------|
| NFR10 | Sistema deve estar disponível 24h (deploy em cloud) |
| NFR11 | Dados devem persistir entre reinícios (banco persistente) |

### 8.5 Deploy

| ID | Requisito |
|----|-----------|
| NFR12 | Sistema deve rodar em tier gratuito (Vercel, Railway ou similar) |
| NFR13 | Código deve ser versionado no GitHub |

---

## 9. Critérios de Aceite (Resumo por Feature)

### Entrada de Veículo

- Dado estacionamento com vagas disponíveis  
- Quando operador informa placa e tipo (rotativo/mensalista)  
- Então sistema registra entrada, decrementa vagas e exibe confirmação  

- Dado mensalista com validade ativa  
- Quando operador registra entrada como mensalista  
- Então sistema valida e permite entrada  

- Dado estacionamento lotado  
- Quando operador tenta registrar entrada  
- Então sistema impede e exibe mensagem  

### Saída de Veículo

- Dado veículo rotativo com entrada registrada  
- Quando operador informa placa na saída  
- Então sistema calcula valor, exibe e permite confirmar pagamento  

- Dado mensalista com entrada registrada  
- Quando operador registra saída  
- Então sistema não cobra e libera vaga  

### Vagas e Lotado

- Dado 0 vagas disponíveis  
- Então sistema exibe sinalização "LOTADO" na tela principal  

- Dado qualquer alteração de ocupação  
- Então vagas disponíveis/ocupadas são atualizadas em tempo real  

---

## 10. Próximos Passos

1. **Arquitetura** — Wagner define stack, estrutura e decisões técnicas  
2. **Epics e Stories** — Quebra em epics e user stories  
3. **Implementação** — Felipe executa stories  

---

*PRD criado pelo Time MEQ. Baseado no Product Brief `product-brief-estacionamento.md`.*
