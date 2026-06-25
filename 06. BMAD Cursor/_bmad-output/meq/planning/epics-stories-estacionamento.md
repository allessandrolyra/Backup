# Epics e User Stories — Sistema de Estacionamento

**Autor:** Paula (Product Developer)  
**Data:** 2025-03-19  
**Fonte:** PRD, Arquitetura, Revisão Diana

---

## Epic 1: Autenticação e Acesso

### E1-S1: Login e Logout
**Como** operador ou administrador  
**Quero** fazer login com email e senha  
**Para** acessar o sistema de acordo com meu perfil  

**Critérios de Aceite:**
- [ ] AC1.1: Formulário de login com email e senha
- [ ] AC1.2: Validação de credenciais via Supabase Auth
- [ ] AC1.3: Redirecionamento: operador → /dashboard, admin → /admin/dashboard
- [ ] AC1.4: Mensagem de erro em credenciais inválidas
- [ ] AC1.5: Botão/logout que encerra sessão

---

### E1-S2: Proteção de Rotas por Role
**Como** sistema  
**Quero** restringir acesso por perfil  
**Para** garantir que operador não acesse admin  

**Critérios de Aceite:**
- [ ] AC2.1: Middleware verifica role (operador/admin) em user_metadata
- [ ] AC2.2: Rotas /admin/* bloqueadas para operador
- [ ] AC2.3: Redirecionamento para login se não autenticado

---

## Epic 2: Controle de Vagas e Tela Principal

### E2-S1: Exibir Vagas em Tempo Real
**Como** operador  
**Quero** ver vagas disponíveis e ocupadas em destaque  
**Para** saber o status do estacionamento  

**Critérios de Aceite:**
- [ ] AC1.1: Exibir total (80), disponíveis e ocupadas
- [ ] AC1.2: Atualização em tempo real via Supabase Realtime
- [ ] AC1.3: Números em destaque na tela principal

---

### E2-S2: Sinalização de Lotado
**Como** operador  
**Quero** ver aviso "LOTADO" quando 0 vagas  
**Para** informar clientes  

**Critérios de Aceite:**
- [ ] AC2.1: Banner/aviso visível quando disponíveis = 0
- [ ] AC2.2: Aviso na tela principal (não apenas modal)

---

## Epic 3: Entrada de Veículos

### E3-S1: Registrar Entrada (Rotativo)
**Como** operador  
**Quero** registrar entrada de veículo rotativo  
**Para** controlar ocupação e cobrança  

**Critérios de Aceite:**
- [ ] AC1.1: Campo placa + seleção tipo "rotativo"
- [ ] AC1.2: Sistema registra entrada_em automaticamente
- [ ] AC1.3: Impede se lotado (0 vagas)
- [ ] AC1.4: Impede se placa já tem entrada ativa
- [ ] AC1.5: Decrementa vagas disponíveis em tempo real

---

### E3-S2: Registrar Entrada (Mensalista)
**Como** operador  
**Quero** registrar entrada de mensalista  
**Para** liberar sem cobrança  

**Critérios de Aceite:**
- [ ] AC2.1: Campo placa + seleção tipo "mensalista"
- [ ] AC2.2: Sistema valida placa em mensalistas (ativo, validade_ate >= hoje)
- [ ] AC2.3: Se válido: registra entrada com mensalista_id
- [ ] AC2.4: Se inválido: exibe mensagem e impede entrada

---

## Epic 4: Saída de Veículos

### E4-S1: Registrar Saída (Rotativo) com Cálculo
**Como** operador  
**Quero** registrar saída e ver valor a pagar  
**Para** cobrar corretamente  

**Critérios de Aceite:**
- [ ] AC1.1: Campo placa para buscar entrada ativa
- [ ] AC1.2: Sistema calcula valor (valor_hora, fracao_minima da config)
- [ ] AC1.3: Exibe valor antes de confirmar
- [ ] AC1.4: Operador confirma pagamento → registra saida_em, valor_pago
- [ ] AC1.5: Libera vaga (incrementa disponíveis)

---

### E4-S2: Registrar Saída (Mensalista)
**Como** operador  
**Quero** registrar saída de mensalista sem cobrança  
**Para** liberar a vaga  

**Critérios de Aceite:**
- [ ] AC2.1: Campo placa para buscar entrada ativa
- [ ] AC2.2: Sistema identifica tipo mensalista
- [ ] AC2.3: Não exibe valor; confirma saída sem cobrança
- [ ] AC2.4: Registra saida_em, valor_pago = NULL

---

## Epic 5: Mensalistas (Admin)

### E5-S1: Cadastrar Mensalista
**Como** administrador  
**Quero** cadastrar mensalista com nome, placa e validade  
**Para** liberar entrada sem cobrança  

**Critérios de Aceite:**
- [ ] AC1.1: Formulário: nome, placa, validade_ate
- [ ] AC1.2: Placa única (não duplicar)
- [ ] AC1.3: Validação de dados (campos obrigatórios)
- [ ] AC1.4: Lista de mensalistas cadastrados

---

### E5-S2: Editar e Inativar Mensalista
**Como** administrador  
**Quero** editar ou inativar mensalista  
**Para** manter cadastro atualizado  

**Critérios de Aceite:**
- [ ] AC2.1: Botão editar abre formulário com dados atuais
- [ ] AC2.2: Botão inativar (ativo = false)
- [ ] AC2.3: Mensalista inativo não valida em nova entrada

---

## Epic 6: Configuração e Tarifas (Admin)

### E6-S1: Configurar Tarifas
**Como** administrador  
**Quero** configurar valor por hora e fração mínima  
**Para** calcular cobrança de rotativos  

**Critérios de Aceite:**
- [ ] AC1.1: Formulário: valor_hora, fracao_minima_minutos
- [ ] AC1.2: Valores aplicados no próximo cálculo de saída
- [ ] AC1.3: Validação (valores >= 0)

---

## Epic 7: Painel Administrativo

### E7-S1: Dashboard Admin
**Como** administrador  
**Quero** ver vagas, ocupação e faturamento  
**Para** acompanhar o estacionamento  

**Critérios de Aceite:**
- [ ] AC1.1: Vagas disponíveis/ocupadas
- [ ] AC1.2: Faturamento do dia (soma valor_pago de rotativos com saida_em hoje)
- [ ] AC1.3: Lista de entradas ativas (placa, tipo, entrada_em)

---

## Epic 8: Infraestrutura e PaymentService

### E8-S1: Setup Next.js + Supabase
**Como** desenvolvedor  
**Quero** projeto configurado com Next.js e Supabase  
**Para** implementar as features  

**Critérios de Aceite:**
- [ ] AC1.1: Next.js 14 App Router
- [ ] AC1.2: Cliente Supabase (browser, server)
- [ ] AC1.3: Variáveis de ambiente (.env.local)
- [ ] AC1.4: Migration 001 aplicada no Supabase

---

### E8-S2: PaymentService Abstrato
**Como** sistema  
**Quero** camada abstrata de pagamento  
**Para** permitir gateway futuro  

**Critérios de Aceite:**
- [ ] AC2.1: Interface PaymentService com processPayment()
- [ ] AC2.2: Implementação InternalPaymentService (MVP)
- [ ] AC2.3: Injeção/configuração para troca futura

---

## Ordem de Implementação Sugerida

1. **E8-S1** — Setup projeto
2. **E1-S1, E1-S2** — Auth
3. **E2-S1, E2-S2** — Vagas e lotado
4. **E3-S1, E3-S2** — Entrada
5. **E4-S1, E4-S2** — Saída
6. **E6-S1** — Config (necessário para cálculo)
7. **E5-S1, E5-S2** — Mensalistas
8. **E7-S1** — Dashboard admin
9. **E8-S2** — PaymentService

---

*Epics e Stories criados por Paula. Pronto para Felipe implementar.*
