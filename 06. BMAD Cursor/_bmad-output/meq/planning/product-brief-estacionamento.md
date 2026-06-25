---
stepsCompleted: [1, 2, 3, 4, 5, 6]
inputDocuments: []
date: 2025-03-19
author: Alessandro Lyra
---

# Product Brief: Sistema Web de Gerenciamento de Estacionamento

---

## Executive Summary

Sistema web para gerenciamento de estacionamentos de médio porte, com controle de entrada/saída de veículos, vagas disponíveis/ocupadas, sinalização de lotado e gestão financeira. Acessível via navegador, responsivo, com painel administrativo. Deploy gratuito no GitHub (Vercel/Railway).

**Problema:** Estacionamentos de médio porte precisam de controle eficiente de vagas, entrada/saída e faturamento sem custo de licença.

**Solução:** Sistema web open-source, responsivo, com painel admin, preparado para rodar free no GitHub.

---

## Core Vision

### Problem Statement

Estacionamentos de médio porte (até ~80 vagas) enfrentam dificuldade para gerenciar entrada/saída, controle de vagas, mensalistas e faturamento com ferramentas acessíveis. Soluções proprietárias são caras; planilhas não escalam.

### Problem Impact

- Perda de vagas por falta de visibilidade em tempo real
- Erros de cobrança por controle manual
- Falta de sinalização de lotado gera frustração e confusão
- Mensalistas sem cadastro adequado

### Why Existing Solutions Fall Short

- Sistemas proprietários: custo alto de licença
- Planilhas: sem tempo real, sem controle de vagas
- Soluções locais: sem acesso remoto, sem responsividade

### Proposed Solution

Sistema web responsivo que:
- Registra entrada/saída de veículos
- Controla 80 vagas em tempo real
- Sinaliza lotado quando 0 vagas disponíveis
- Cadastra mensalistas manualmente
- Gerencia faturamento interno (rotativos e mensalistas)
- Oferece painel administrativo
- Arquitetura preparada para gateway de pagamento futuro

### Key Differentiators

- **Gratuito:** Deploy free no GitHub (Vercel/Railway)
- **Open-source:** Código aberto, adaptável
- **Extensível:** Camada de pagamento abstrata para gateway futuro

---

## Target Users

### Primary Users

**Operador de Estacionamento** — Funcionário que registra entrada/saída de veículos no dia a dia. Precisa de interface rápida, visibilidade de vagas e cálculo automático de valor. Usa o sistema em tablet ou celular no ponto de controle.

**Administrador** — Gerente ou dono do estacionamento. Cadastra mensalistas, configura tarifas, acompanha ocupação e faturamento. Usa painel admin em desktop ou navegador.

### Secondary Users

**Mensalista** — Cliente com vaga garantida. Beneficia-se do cadastro rápido e da validação automática na entrada.

### User Journey

**Operador:** Login → Tela principal com vagas disponíveis/ocupadas → Registra entrada (placa) → Registra saída (placa, valor calculado) → Vê lotado quando 0 vagas.

**Administrador:** Login admin → Cadastra mensalista (nome, placa, validade) → Configura tarifas → Acompanha ocupação e faturamento.

---

## Success Metrics

### User Success

- Operador registra entrada/saída em < 30 segundos
- Vagas disponíveis/ocupadas sempre visíveis e atualizadas
- Sinalização de lotado clara e imediata
- Mensalistas cadastrados e validados em entrada

### Business Objectives

- Sistema operacional em 24h sem downtime
- Zero erros de cobrança por falha do sistema
- Redução de tempo de gestão vs planilha/manual

### Key Performance Indicators

- Tempo médio de registro de entrada/saída
- Uptime do sistema
- Precisão de cálculo de valores (rotativos)

---

## MVP Scope

### Core Features

| Feature | Descrição |
|---------|-----------|
| **Entrada de veículo** | Registro de placa (e tipo: rotativo/mensalista), horário de entrada |
| **Saída de veículo** | Registro de placa, horário, cálculo automático de valor (rotativos) |
| **Controle de vagas** | 80 vagas totais, disponíveis vs ocupadas em tempo real |
| **Sinalização de lotado** | Banner/aviso visível quando 0 vagas disponíveis |
| **Cadastro de mensalistas** | Manual: nome, placa, validade |
| **Painel administrativo** | Login, dashboard com vagas, ocupação, faturamento básico |
| **Tela principal** | Vagas disponíveis e ocupadas em destaque |
| **Gestão financeira interna** | Controle de rotativos (pagamento na saída) e mensalistas (sem cobrança) |
| **Arquitetura preparada** | Camada PaymentService abstrata para gateway futuro |

### Out of Scope for MVP

- Relatórios detalhados (MVP2)
- Integração com gateway de pagamento (MVP futuro)
- Integração com câmera/OCR para placa
- App mobile nativo

### MVP Success Criteria

- Sistema operacional com 80 vagas
- Entrada/saída funcionando sem erros
- Vagas disponíveis/ocupadas corretas em tempo real
- Lotado sinalizado quando 0 vagas
- Mensalistas cadastrados e validados em entrada

### Future Vision

| Versão | Features |
|--------|----------|
| **MVP2** | Relatórios (faturamento, ocupação, histórico) |
| **Futuro** | Integração com gateway (Stripe, Mercado Pago) |
| **Futuro** | OCR para leitura de placa |
| **Futuro** | App mobile (PWA ou nativo) |

---

## Technical Context (prepared by Wagner)

- **Plataforma:** Web responsiva
- **Deploy:** GitHub + Vercel/Railway (free tier)
- **Stack sugerida:** Next.js + SQLite/Supabase + deploy Vercel
- **Preparação:** PaymentService abstrato para gateway futuro

---

*Product Brief criado pelo Time MEQ. Próximo passo: PRD ou Arquitetura.*
