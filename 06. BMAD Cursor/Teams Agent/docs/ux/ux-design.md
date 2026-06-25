# UX Design — Secretário de Reunião Teams

> **Projeto:** Secretário de Reunião Teams  
> **Versão:** 1.0  
> **Última atualização:** 08/06/2026  
> **Autora:** Sally — UX Designer, Squad MEQ  
> **Status:** Draft para revisão

---

## Índice

1. [Visão Geral de UX](#1-visão-geral-de-ux)
2. [Adaptive Card — Resumo no Chat da Reunião](#2-adaptive-card--resumo-no-chat-da-reunião)
3. [Documento SharePoint — Ata Completa](#3-documento-sharepoint--ata-completa)
4. [Email Template](#4-email-template)
5. [Notificações](#5-notificações)
6. [Fluxo do Usuário](#6-fluxo-do-usuário)
7. [Acessibilidade](#7-acessibilidade)
8. [JSON Schema da Adaptive Card Principal](#8-json-schema-da-adaptive-card-principal)

---

## 1. Visão Geral de UX

### 1.1 Propósito

O Secretário de Reunião Teams é um agente automatizado que transforma reuniões em registros acionáveis. O usuário nunca pede a ata — ela simplesmente aparece, pronta para uso, no chat da reunião em até 5 minutos após o encerramento.

### 1.2 Personas

| Persona | Necessidade principal | Comportamento típico |
|---|---|---|
| **Gestor(a)** | Visão rápida de decisões e riscos | Escaneia o resumo no chat, raramente abre a ata completa |
| **Líder de Projeto** | Rastrear ações e prazos | Abre a ata completa, exporta tarefas para backlog |
| **Participante** | Confirmar o que foi combinado | Lê o resumo rápido e verifica suas ações atribuídas |
| **Compliance / Auditoria** | Registro formal e rastreável | Acessa o documento SharePoint como evidência documental |

### 1.3 Princípios de Design

| Princípio | Aplicação |
|---|---|
| **Clareza** | Linguagem direta, sem jargão. Cada seção tem um título autoexplicativo. O usuário entende o conteúdo sem precisar ler o contexto inteiro. |
| **Escaneabilidade** | Hierarquia visual forte: badges coloridos, ícones, tabelas compactas. O gestor consegue extrair valor em 15 segundos olhando apenas o card no chat. |
| **Acionabilidade** | Cada decisão tem um dono, cada ação tem prazo e responsável. Botões levam diretamente à ação seguinte (abrir ata, enviar email). Zero cliques desnecessários. |
| **Consistência** | O mesmo vocabulário visual (cores, ícones, estrutura) se repete no card, no documento e no email, criando familiaridade imediata. |
| **Confiança** | O agente indica claramente que o conteúdo foi gerado por IA e pode conter imprecisões, convidando o usuário a revisar. Transparência gera confiança. |

### 1.4 Paleta de Cores Semânticas

| Elemento | Cor | Hex | Uso |
|---|---|---|---|
| Positivo | Verde | `#107C10` | Status favorável, tarefas concluídas |
| Atenção | Amarelo/Âmbar | `#FFB900` | Itens que requerem acompanhamento |
| Crítico | Vermelho | `#D13438` | Riscos, bloqueios, atrasos |
| Neutro | Azul Teams | `#6264A7` | Informações gerais, cabeçalhos |
| Texto primário | Cinza escuro | `#242424` | Corpo de texto |
| Texto secundário | Cinza médio | `#616161` | Metadados, timestamps |
| Fundo | Branco | `#FFFFFF` | Background padrão |

---

## 2. Adaptive Card — Resumo no Chat da Reunião

### 2.1 Objetivo

Entregar um resumo executivo imediato no próprio chat da reunião, sem que o usuário precise navegar para outro lugar. O card é o primeiro ponto de contato com a ata.

### 2.2 Estrutura Visual

```
┌──────────────────────────────────────────────────┐
│  📋  ATA DE REUNIÃO                              │
│  Sprint Planning — Squad MEQ                     │
│  📅 08/06/2026  ⏰ 10:00–11:30  👥 8 participantes│
├──────────────────────────────────────────────────┤
│                                                  │
│  📌 RESUMO                                       │
│  • Definidos os 5 épicos do MVP para Q3          │
│  • Aprovado orçamento de infraestrutura cloud    │
│  • Equipe alinhada sobre prazo de entrega: 15/08 │
│  • Identificado risco de dependência com time X  │
│                                                  │
├──────────────────────────────────────────────────┤
│                                                  │
│  ✅ DECISÕES PRINCIPAIS                          │
│  🟢 Aprovado — Migração para Azure em fases      │
│  🟢 Aprovado — Contratação de 2 devs sênior      │
│  🟡 Pendente — Definição de SLA com fornecedor    │
│                                                  │
├──────────────────────────────────────────────────┤
│                                                  │
│  📋 AÇÕES                                        │
│  ┌────────────────┬──────────┬──────────┬──────┐ │
│  │ Ação           │ Responsá.│ Prazo    │Status│ │
│  ├────────────────┼──────────┼──────────┼──────┤ │
│  │ Criar RFC cloud│ Wagner   │ 15/06/26 │ 🔴   │ │
│  │ Entrevistar    │ Paula    │ 20/06/26 │ 🟡   │ │
│  │ Mapear APIs    │ Igor     │ 22/06/26 │ 🟡   │ │
│  │ Setup CI/CD    │ Davi     │ 25/06/26 │ ⚪   │ │
│  │ Testes carga   │ Quinn    │ 30/06/26 │ ⚪   │ │
│  └────────────────┴──────────┴──────────┴──────┘ │
│                                                  │
├──────────────────────────────────────────────────┤
│                                                  │
│  STATUS GERAL:  🟢 Positivo                      │
│                                                  │
├──────────────────────────────────────────────────┤
│  ⚠️ Conteúdo gerado por IA — revise para confirmar│
│                                                  │
│  [ 📄 Ver Ata Completa ]   [ ✉️ Enviar por Email ] │
└──────────────────────────────────────────────────┘
```

### 2.3 Especificação dos Elementos

#### Header

| Elemento | Especificação |
|---|---|
| Ícone | Emoji 📋 ou ícone SVG customizado |
| Título | "ATA DE REUNIÃO" — `TextBlock`, size `Large`, weight `Bolder`, color `Accent` |
| Subtítulo | Assunto da reunião — `TextBlock`, size `Medium`, weight `Default` |
| Metadados | Data, horário início-fim, quantidade de participantes — `ColumnSet` com ícones inline |

#### Seção 1: Resumo

| Elemento | Especificação |
|---|---|
| Título da seção | "📌 RESUMO" — `TextBlock`, weight `Bolder`, separator `true` |
| Conteúdo | 3 a 5 bullet points — `TextBlock` com markdown (`• ponto 1\n• ponto 2`) |
| Comportamento | Sempre visível, nunca colapsável |

#### Seção 2: Decisões Principais

| Elemento | Especificação |
|---|---|
| Título da seção | "✅ DECISÕES PRINCIPAIS" — `TextBlock`, weight `Bolder` |
| Cada decisão | `ColumnSet`: coluna 1 = badge colorido (🟢/🟡/🔴), coluna 2 = status text, coluna 3 = descrição |
| Limite | Top 3 decisões mais relevantes |
| Badges | 🟢 Aprovado, 🟡 Pendente, 🔴 Rejeitado |

#### Seção 3: Ações

| Elemento | Especificação |
|---|---|
| Título da seção | "📋 AÇÕES" — `TextBlock`, weight `Bolder` |
| Tabela | `FactSet` ou `ColumnSet` com 4 colunas: Ação, Responsável, Prazo, Status |
| Limite | Top 5 ações prioritárias |
| Status icons | 🔴 Atrasado, 🟡 Em andamento, ⚪ Pendente, 🟢 Concluído |

#### Seção 4: Status Geral

| Elemento | Especificação |
|---|---|
| Layout | `Container` com background colorido conforme status |
| Badge | `TextBlock` centralizado: "🟢 Positivo" / "🟡 Neutro" / "🔴 Requer Atenção" |
| Lógica | Derivado automaticamente da proporção de decisões aprovadas vs pendentes e ações no prazo vs atrasadas |

#### Disclaimer

| Elemento | Especificação |
|---|---|
| Texto | "⚠️ Conteúdo gerado por IA — revise para confirmar" |
| Estilo | `TextBlock`, size `Small`, color `Attention`, isSubtle `true` |

#### Footer / Ações

| Botão | Tipo | Comportamento |
|---|---|---|
| "📄 Ver Ata Completa" | `Action.OpenUrl` | Abre o documento no SharePoint em nova aba |
| "✉️ Enviar por Email" | `Action.Submit` | Dispara flow que envia email para todos os participantes |

---

## 3. Documento SharePoint — Ata Completa

### 3.1 Objetivo

Servir como registro formal, completo e auditável da reunião. É o documento de referência para compliance, acompanhamento de ações e consulta futura.

### 3.2 Layout do Documento

```
┌──────────────────────────────────────────────────┐
│                                                  │
│          [Logo Empresa / Squad MEQ]              │
│                                                  │
│          ATA DE REUNIÃO                          │
│          Sprint Planning — Squad MEQ             │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  INFORMAÇÕES DA REUNIÃO                          │
│  ┌─────────────────┬───────────────────────┐     │
│  │ Data            │ 08/06/2026            │     │
│  │ Horário         │ 10:00 – 11:30 (1h30)  │     │
│  │ Organizador     │ Marco Silva           │     │
│  │ Plataforma      │ Microsoft Teams       │     │
│  │ ID da Reunião   │ MTG-2026-0608-001     │     │
│  │ Gravação        │ [Link para gravação]  │     │
│  │ Transcrição     │ [Link para transcrição│     │
│  └─────────────────┴───────────────────────┘     │
│                                                  │
│  PARTICIPANTES                                   │
│  ✅ Marco Silva (Organizador)                    │
│  ✅ Paula Mendes                                 │
│  ✅ Wagner Costa                                 │
│  ✅ Felipe Santos                                │
│  ✅ Igor Pereira                                 │
│  ✅ Davi Oliveira                                │
│  ✅ Quinn Almeida                                │
│  ✅ Diana Rocha                                  │
│  ❌ Ana Torres (ausente)                         │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  ÍNDICE                                          │
│  1. Resumo Executivo                             │
│  2. Tópicos Discutidos                           │
│  3. Decisões                                     │
│  4. Ações e Tarefas                              │
│  5. Riscos e Impedimentos                        │
│  6. Próximos Passos                              │
│  7. Observações                                  │
│                                                  │
│  ════════════════════════════════════════════    │
│                                                  │
│  1. RESUMO EXECUTIVO                             │
│  Parágrafo conciso (3-5 frases) capturando       │
│  a essência da reunião, principais conclusões    │
│  e tom geral.                                    │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  2. TÓPICOS DISCUTIDOS                           │
│                                                  │
│  2.1 [Título do Tópico 1]                        │
│      Contexto e discussão...                     │
│      Conclusão/encaminhamento...                 │
│                                                  │
│  2.2 [Título do Tópico 2]                        │
│      Contexto e discussão...                     │
│      Conclusão/encaminhamento...                 │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  3. DECISÕES                                     │
│  ┌────┬──────────────┬────────┬───────────┐      │
│  │ #  │ Decisão      │ Status │ Responsáv.│      │
│  ├────┼──────────────┼────────┼───────────┤      │
│  │ D1 │ Migração...  │🟢 Apro.│ Wagner    │      │
│  │ D2 │ Contratação..│🟢 Apro.│ Paula     │      │
│  │ D3 │ SLA fornec.. │🟡 Pend.│ Igor      │      │
│  └────┴──────────────┴────────┴───────────┘      │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  4. AÇÕES E TAREFAS                              │
│  ┌────┬──────────┬────────┬────────┬──────┐      │
│  │ #  │ Ação     │ Resp.  │ Prazo  │Status│      │
│  ├────┼──────────┼────────┼────────┼──────┤      │
│  │ A1 │ Criar RFC│ Wagner │ 15/06  │ ⏳   │      │
│  │ A2 │ Entrev.  │ Paula  │ 20/06  │ ⏳   │      │
│  │ A3 │ Map. APIs│ Igor   │ 22/06  │ ⏳   │      │
│  │ A4 │ Setup CI │ Davi   │ 25/06  │ ⏳   │      │
│  │ A5 │ Testes   │ Quinn  │ 30/06  │ ⏳   │      │
│  └────┴──────────┴────────┴────────┴──────┘      │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  5. RISCOS E IMPEDIMENTOS                        │
│  ┌────┬──────────────┬──────────┬────────┐       │
│  │ #  │ Descrição    │ Impacto  │ Mitigação│      │
│  ├────┼──────────────┼──────────┼────────┤       │
│  │ R1 │ Dependência  │ 🔴 Alto  │ Reunião │      │
│  │    │ do time X    │          │ alinhamento│   │
│  │ R2 │ Prazo curto  │ 🟡 Médio │ Sprint  │      │
│  │    │ fornecedor   │          │ buffer  │      │
│  └────┴──────────────┴──────────┴────────┘       │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  6. PRÓXIMOS PASSOS                              │
│  • Próxima reunião: 15/06/2026, 10:00            │
│  • Entregáveis até próxima reunião: A1, A2       │
│  • Temas pendentes: SLA fornecedor (D3)          │
│                                                  │
│  ────────────────────────────────────────────    │
│                                                  │
│  7. OBSERVAÇÕES                                  │
│  Notas adicionais, comentários off-record,       │
│  pontos levantados fora da pauta oficial.        │
│                                                  │
│  ════════════════════════════════════════════    │
│  ⚠️ Documento gerado automaticamente por IA.     │
│  Revise o conteúdo para garantir precisão.       │
│  Gerado em: 08/06/2026 11:35:22 UTC-3           │
└──────────────────────────────────────────────────┘
```

### 3.3 Especificação de Cada Seção

#### Cabeçalho

| Elemento | Detalhe |
|---|---|
| Logo | Logo da empresa ou da squad, alinhado à esquerda, max 120px altura |
| Título | "ATA DE REUNIÃO" — H1, fonte semibold |
| Subtítulo | Assunto da reunião — H2, fonte regular |
| Separador | Linha horizontal de 1px, cor `#E0E0E0` |

#### Metadados (Informações da Reunião)

Tabela de 2 colunas sem bordas externas:

| Campo | Formato |
|---|---|
| Data | DD/MM/AAAA |
| Horário | HH:MM – HH:MM (duração) |
| Organizador | Nome completo |
| Plataforma | "Microsoft Teams" |
| ID da Reunião | Código único gerado: `MTG-AAAA-MMDD-SEQ` |
| Gravação | Hyperlink para gravação no Stream/SharePoint (se disponível) |
| Transcrição | Hyperlink para transcrição (se disponível) |

#### Participantes

- Lista com ✅ para presentes e ❌ para ausentes
- Organizador identificado com tag "(Organizador)"
- Ordenação: organizador primeiro, depois alfabética

#### Índice

- Links âncora para cada seção do documento
- Gerado automaticamente a partir dos headings

#### Seção 1: Resumo Executivo

- 3 a 5 frases em parágrafo corrido
- Tom objetivo, sem adjetivos desnecessários
- Captura: contexto, principais conclusões, tom geral

#### Seção 2: Tópicos Discutidos

- Subseções numeradas (2.1, 2.2, 2.3...)
- Cada tópico: título, contexto da discussão, conclusão ou encaminhamento
- Ordenados cronologicamente conforme apareceram na reunião

#### Seção 3: Decisões

Tabela com colunas:

| Coluna | Formato |
|---|---|
| # | ID sequencial: D1, D2, D3... |
| Decisão | Descrição concisa da decisão |
| Status | Badge: 🟢 Aprovado, 🟡 Pendente, 🔴 Rejeitado |
| Responsável | Nome de quem é accountable |

#### Seção 4: Ações e Tarefas

Tabela com colunas:

| Coluna | Formato |
|---|---|
| # | ID sequencial: A1, A2, A3... |
| Ação | Descrição concisa da tarefa |
| Responsável | Nome do responsável |
| Prazo | DD/MM/AAAA |
| Status | ⏳ Pendente, 🔄 Em andamento, ✅ Concluído, ❌ Cancelado |

#### Seção 5: Riscos e Impedimentos

Tabela com colunas:

| Coluna | Formato |
|---|---|
| # | ID sequencial: R1, R2... |
| Descrição | Descrição do risco ou impedimento |
| Impacto | 🔴 Alto, 🟡 Médio, 🟢 Baixo |
| Mitigação | Ação proposta para mitigar |

#### Seção 6: Próximos Passos

- Lista com bullets
- Inclui: data da próxima reunião, entregáveis esperados, temas pendentes

#### Seção 7: Observações

- Campo livre para notas adicionais
- Pontos levantados fora da pauta
- Pode ficar vazio se não houver observações

#### Rodapé

- Disclaimer: "⚠️ Documento gerado automaticamente por IA. Revise o conteúdo para garantir precisão."
- Timestamp de geração: DD/MM/AAAA HH:MM:SS UTC-3

---

## 4. Email Template

### 4.1 Objetivo

Enviar a ata de reunião por email para participantes e stakeholders que preferiram esse canal, ou quando alguém clica "Enviar por Email" no card.

### 4.2 Subject Line

**Padrão:**

```
[Ata] {Assunto da Reunião} — {DD/MM/AAAA}
```

**Exemplos:**

```
[Ata] Sprint Planning — Squad MEQ — 08/06/2026
[Ata] Alinhamento Trimestral — Diretoria — 08/06/2026
```

### 4.3 Layout do Email

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │  📋 ATA DE REUNIÃO                       │    │
│  │  Sprint Planning — Squad MEQ             │    │
│  │  08/06/2026 • 10:00–11:30 • 8 particip.  │    │
│  └──────────────────────────────────────────┘    │
│                                                  │
│  Olá,                                            │
│                                                  │
│  Segue o resumo da reunião realizada hoje.       │
│                                                  │
│  ─── RESUMO EXECUTIVO ───                        │
│                                                  │
│  Foram definidos os 5 épicos do MVP para Q3,     │
│  aprovado o orçamento de infraestrutura cloud    │
│  e alinhado o prazo de entrega para 15/08.       │
│  Foi identificado risco de dependência com       │
│  time X que requer atenção.                      │
│                                                  │
│  ─── DECISÕES ───                                │
│                                                  │
│  🟢 Migração para Azure em fases — Aprovado      │
│  🟢 Contratação de 2 devs sênior — Aprovado      │
│  🟡 SLA com fornecedor — Pendente                 │
│                                                  │
│  ─── AÇÕES PRIORITÁRIAS ───                      │
│                                                  │
│  • Wagner: Criar RFC cloud → até 15/06           │
│  • Paula: Entrevistar candidatos → até 20/06     │
│  • Igor: Mapear APIs → até 22/06                 │
│                                                  │
│  ─── STATUS GERAL: 🟢 Positivo ───               │
│                                                  │
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │                                          │    │
│  │       [ 📄 Ver Ata Completa ]            │    │
│  │                                          │    │
│  └──────────────────────────────────────────┘    │
│                                                  │
│  ────────────────────────────────────────────    │
│  ⚠️ Conteúdo gerado por IA — revise para        │
│  confirmar a precisão das informações.           │
│                                                  │
│  Secretário de Reunião Teams • Squad MEQ         │
│  Este email foi enviado automaticamente.         │
└──────────────────────────────────────────────────┘
```

### 4.4 Especificação

| Elemento | Detalhe |
|---|---|
| **Header** | Banner com fundo `#6264A7` (azul Teams), texto branco, ícone 📋 |
| **Saudação** | "Olá," — genérica, sem nome individual |
| **Resumo Executivo** | 3-5 frases em parágrafo — mesmo conteúdo da Seção 1 do documento |
| **Decisões** | Lista com badges emoji (🟢🟡🔴) — top 3 |
| **Ações** | Lista com responsável + prazo — top 3 |
| **Status Geral** | Badge visual com cor correspondente |
| **CTA** | Botão "📄 Ver Ata Completa" — link para o documento no SharePoint |
| **Disclaimer** | Texto pequeno sobre geração por IA |
| **Rodapé** | Identificação do agente + aviso de envio automático |

### 4.5 Regras de Envio

| Regra | Detalhe |
|---|---|
| **Destinatários** | Todos os participantes da reunião (para) + organizador (CC) |
| **Reply-to** | Organizador da reunião |
| **Formato** | HTML responsivo com fallback texto puro |
| **Gatilho** | Clique em "Enviar por Email" no card OU configuração automática |
| **Frequência** | Máximo 1 email por reunião |

---

## 5. Notificações

### 5.1 Notificação: Ata Pronta

**Quando:** 5 minutos após o encerramento da reunião.

**Canal:** Chat da reunião no Teams (via bot post).

**Conteúdo:** A própria Adaptive Card descrita na Seção 2. A card funciona simultaneamente como notificação e como interface de consumo.

**Comportamento:**

| Aspecto | Detalhe |
|---|---|
| Timing | Até 5 minutos após encerramento. Se demorar mais, enviar mensagem intermediária: "⏳ Preparando a ata da reunião..." |
| Visibilidade | Postada no chat da reunião — visível para todos os participantes |
| Persistência | A card permanece no chat indefinidamente, sempre acessível no histórico |
| Falha | Se o processamento falhar, enviar: "❌ Não foi possível gerar a ata automaticamente. Contate o administrador." |

### 5.2 Notificação: Lembrete de Ações Pendentes (Futuro — v2)

**Quando:** 2 dias úteis antes do prazo de cada ação atribuída.

**Canal:** Chat 1:1 com o responsável no Teams.

**Conteúdo:**

```
┌──────────────────────────────────────────────────┐
│  ⏰ LEMBRETE DE AÇÃO                             │
│                                                  │
│  Você tem uma ação pendente da reunião            │
│  "Sprint Planning — Squad MEQ" (08/06/2026):     │
│                                                  │
│  📋 Criar RFC de migração cloud                   │
│  📅 Prazo: 15/06/2026 (em 2 dias)                │
│                                                  │
│  [ ✅ Marcar como Concluída ]  [ 📄 Ver Ata ]     │
└──────────────────────────────────────────────────┘
```

**Comportamento futuro:**

| Aspecto | Detalhe |
|---|---|
| Frequência | 1 lembrete por ação, 2 dias úteis antes do prazo |
| Opt-out | Usuário pode desativar lembretes nas configurações |
| Interação | Botão "Marcar como Concluída" atualiza o status na ata |
| Escalonamento | Se a ação não for marcada como concluída até o prazo, notificar também o organizador |

---

## 6. Fluxo do Usuário

### 6.1 Jornada Principal

```
┌─────────────┐
│  1. REUNIÃO  │
│  Usuário     │
│  participa   │
│  normalmente │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ 2. ENCERRAR  │
│ Reunião é    │
│ encerrada    │
│ no Teams     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│ 3. PROCESSAMENTO (IA)    │
│ Agente processa          │
│ transcrição e gera ata   │
│ ⏱️ Até 5 min             │
│                          │
│ Se > 2 min:              │
│ "⏳ Preparando a ata..." │
└──────────┬──────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. CARD NO CHAT           │
│ Adaptive Card aparece     │
│ no chat da reunião        │
│ com resumo executivo      │
└──────────┬───────────────┘
           │
     ┌─────┴──────┐
     │             │
     ▼             ▼
┌─────────┐  ┌──────────┐
│ 5a. LER │  │ 5b. ABRIR│
│ RESUMO   │  │ ATA      │
│ RÁPIDO   │  │ COMPLETA │
│ (no card)│  │(SharePt.)│
└─────────┘  └────┬─────┘
                   │
                   ▼
             ┌──────────┐
             │ 6. EMAIL  │
             │ (Opcional)│
             │ Clicar    │
             │ "Enviar"  │
             └──────────┘
```

### 6.2 Cenários Alternativos

| Cenário | Comportamento |
|---|---|
| Reunião muito curta (< 5 min) | Agente gera card simplificado com nota: "Reunião breve — resumo compacto" |
| Reunião sem áudio/transcrição | Card de erro: "Não foi possível gerar a ata — transcrição indisponível" |
| Reunião com muitos participantes (> 20) | Lista de participantes colapsada no card, completa apenas no SharePoint |
| Falha no processamento | Mensagem de erro no chat + log para administrador |
| Reunião recorrente | ID da ata inclui sequência para rastreabilidade (MTG-2026-0608-001, -002...) |

### 6.3 Tempos de Resposta Esperados

| Etapa | Tempo máximo |
|---|---|
| Início do processamento | 30 segundos após encerramento |
| Mensagem intermediária (se necessário) | 2 minutos |
| Entrega do card no chat | 5 minutos |
| Documento disponível no SharePoint | 5 minutos (simultâneo ao card) |
| Envio de email (se solicitado) | 1 minuto após clique |

---

## 7. Acessibilidade

### 7.1 Diretrizes Gerais

O Secretário de Reunião Teams segue as diretrizes WCAG 2.1 nível AA para garantir que todos os outputs sejam acessíveis.

### 7.2 Contraste de Cores

| Par de cores | Ratio mínimo | Uso |
|---|---|---|
| Texto `#242424` sobre fundo `#FFFFFF` | 15.4:1 ✅ | Texto principal |
| Badge verde `#107C10` sobre fundo `#FFFFFF` | 4.8:1 ✅ | Status Aprovado |
| Badge âmbar `#FFB900` sobre fundo `#FFFFFF` | 2.1:1 ⚠️ | Status Pendente — usar texto escuro sobre fundo âmbar |
| Badge vermelho `#D13438` sobre fundo `#FFFFFF` | 4.6:1 ✅ | Status Crítico |
| Texto branco `#FFFFFF` sobre azul `#6264A7` | 4.5:1 ✅ | Header do email |

**Solução para âmbar:** Usar `#FFB900` como fundo com texto `#242424` (ratio 8.2:1), ou substituir por `#986F0B` como texto sobre fundo branco (ratio 4.6:1).

### 7.3 Adaptive Card — Acessibilidade

| Requisito | Implementação |
|---|---|
| Alt text | Todos os `Image` possuem `altText` descritivo |
| Fallback text | Propriedade `fallbackText` na raiz do card com versão texto puro do conteúdo |
| Ordem de leitura | Elementos ordenados logicamente (header → resumo → decisões → ações → footer) |
| Labels em botões | Texto descritivo: "Ver Ata Completa no SharePoint" ao invés de "Clique aqui" |
| Sem informação apenas por cor | Todos os badges incluem texto além da cor (🟢 Aprovado, não apenas 🟢) |

### 7.4 Documento SharePoint — Acessibilidade

| Requisito | Implementação |
|---|---|
| Headings semânticos | H1 para título, H2 para seções, H3 para subseções — hierarquia consistente |
| Tabelas acessíveis | Headers de coluna marcados com `<th scope="col">`, sem tabelas usadas para layout |
| Alt text em imagens | Logo com alt text: "Logo [nome da empresa]" |
| Links descritivos | "Abrir gravação da reunião no Stream" ao invés de "clique aqui" |
| Idioma do documento | `lang="pt-BR"` no elemento raiz |

### 7.5 Email — Acessibilidade

| Requisito | Implementação |
|---|---|
| HTML semântico | Uso de `<h1>`, `<h2>`, `<p>`, `<table>` com roles adequados |
| Versão texto puro | Multipart email com versão plain text completa |
| Alt text no banner | Alt: "Ata de Reunião — [Assunto]" |
| Links acessíveis | Texto descritivo no CTA |
| Largura responsiva | Max-width 600px, fluid em mobile |

### 7.6 Suporte a Leitores de Tela

| Contexto | Comportamento esperado |
|---|---|
| Card no Teams | Leitor de tela narra: "Ata de Reunião. Sprint Planning. 8 de junho de 2026. Resumo: [conteúdo]..." |
| Tabelas no documento | Leitor anuncia cabeçalhos de coluna ao navegar células |
| Badges de status | Leitor narra "Aprovado" e não apenas a cor ou emoji |
| Botões de ação | Leitor narra ação completa: "Botão: Ver Ata Completa no SharePoint" |

---

## 8. JSON Schema da Adaptive Card Principal

### 8.1 Card Completo (Adaptive Card v1.5)

```json
{
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.5",
  "fallbackText": "Ata de Reunião: Sprint Planning — Squad MEQ. Gerada em 08/06/2026. Para visualizar, atualize o Microsoft Teams.",
  "body": [
    {
      "type": "Container",
      "style": "emphasis",
      "bleed": true,
      "items": [
        {
          "type": "ColumnSet",
          "columns": [
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "📋",
                  "size": "Large"
                }
              ],
              "verticalContentAlignment": "Center"
            },
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "ATA DE REUNIÃO",
                  "size": "Large",
                  "weight": "Bolder",
                  "color": "Accent"
                },
                {
                  "type": "TextBlock",
                  "text": "${meetingSubject}",
                  "size": "Medium",
                  "spacing": "None",
                  "wrap": true
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "Small",
          "columns": [
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "📅 ${meetingDate}",
                  "size": "Small",
                  "isSubtle": true
                }
              ]
            },
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "⏰ ${meetingStartTime}–${meetingEndTime}",
                  "size": "Small",
                  "isSubtle": true
                }
              ]
            },
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "👥 ${participantCount} participantes",
                  "size": "Small",
                  "isSubtle": true
                }
              ]
            }
          ]
        }
      ]
    },

    {
      "type": "Container",
      "separator": true,
      "spacing": "Medium",
      "items": [
        {
          "type": "TextBlock",
          "text": "📌 RESUMO",
          "weight": "Bolder",
          "size": "Medium",
          "color": "Accent"
        },
        {
          "type": "TextBlock",
          "text": "${summaryBullets}",
          "wrap": true,
          "spacing": "Small"
        }
      ]
    },

    {
      "type": "Container",
      "separator": true,
      "spacing": "Medium",
      "id": "decisionsSection",
      "items": [
        {
          "type": "TextBlock",
          "text": "✅ DECISÕES PRINCIPAIS",
          "weight": "Bolder",
          "size": "Medium",
          "color": "Accent"
        },
        {
          "type": "ColumnSet",
          "spacing": "Small",
          "columns": [
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision1StatusIcon}",
                  "horizontalAlignment": "Center"
                }
              ]
            },
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision1Status}",
                  "weight": "Bolder",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision1Description}",
                  "wrap": true
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "Small",
          "columns": [
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision2StatusIcon}",
                  "horizontalAlignment": "Center"
                }
              ]
            },
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision2Status}",
                  "weight": "Bolder",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision2Description}",
                  "wrap": true
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "Small",
          "columns": [
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision3StatusIcon}",
                  "horizontalAlignment": "Center"
                }
              ]
            },
            {
              "type": "Column",
              "width": "auto",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision3Status}",
                  "weight": "Bolder",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${decision3Description}",
                  "wrap": true
                }
              ]
            }
          ]
        }
      ]
    },

    {
      "type": "Container",
      "separator": true,
      "spacing": "Medium",
      "id": "actionsSection",
      "items": [
        {
          "type": "TextBlock",
          "text": "📋 AÇÕES",
          "weight": "Bolder",
          "size": "Medium",
          "color": "Accent"
        },
        {
          "type": "ColumnSet",
          "spacing": "Small",
          "columns": [
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "**Ação**",
                  "weight": "Bolder",
                  "size": "Small",
                  "color": "Accent"
                }
              ]
            },
            {
              "type": "Column",
              "width": "80px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "**Resp.**",
                  "weight": "Bolder",
                  "size": "Small",
                  "color": "Accent"
                }
              ]
            },
            {
              "type": "Column",
              "width": "70px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "**Prazo**",
                  "weight": "Bolder",
                  "size": "Small",
                  "color": "Accent"
                }
              ]
            },
            {
              "type": "Column",
              "width": "30px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "**St.**",
                  "weight": "Bolder",
                  "size": "Small",
                  "color": "Accent"
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "None",
          "columns": [
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action1Description}",
                  "wrap": true,
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "80px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action1Owner}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "70px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action1Deadline}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "30px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action1StatusIcon}",
                  "size": "Small"
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "None",
          "columns": [
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action2Description}",
                  "wrap": true,
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "80px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action2Owner}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "70px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action2Deadline}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "30px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action2StatusIcon}",
                  "size": "Small"
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "None",
          "columns": [
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action3Description}",
                  "wrap": true,
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "80px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action3Owner}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "70px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action3Deadline}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "30px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action3StatusIcon}",
                  "size": "Small"
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "None",
          "columns": [
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action4Description}",
                  "wrap": true,
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "80px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action4Owner}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "70px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action4Deadline}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "30px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action4StatusIcon}",
                  "size": "Small"
                }
              ]
            }
          ]
        },
        {
          "type": "ColumnSet",
          "spacing": "None",
          "columns": [
            {
              "type": "Column",
              "width": "stretch",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action5Description}",
                  "wrap": true,
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "80px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action5Owner}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "70px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action5Deadline}",
                  "size": "Small"
                }
              ]
            },
            {
              "type": "Column",
              "width": "30px",
              "items": [
                {
                  "type": "TextBlock",
                  "text": "${action5StatusIcon}",
                  "size": "Small"
                }
              ]
            }
          ]
        }
      ]
    },

    {
      "type": "Container",
      "separator": true,
      "spacing": "Medium",
      "style": "${overallStatusStyle}",
      "items": [
        {
          "type": "TextBlock",
          "text": "STATUS GERAL: ${overallStatusIcon} ${overallStatusText}",
          "weight": "Bolder",
          "horizontalAlignment": "Center",
          "size": "Medium"
        }
      ]
    },

    {
      "type": "Container",
      "separator": true,
      "spacing": "Small",
      "items": [
        {
          "type": "TextBlock",
          "text": "⚠️ Conteúdo gerado por IA — revise para confirmar",
          "size": "Small",
          "isSubtle": true,
          "horizontalAlignment": "Center",
          "color": "Attention"
        }
      ]
    }
  ],

  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "📄 Ver Ata Completa",
      "url": "${sharepointDocumentUrl}",
      "tooltip": "Abrir a ata completa no SharePoint"
    },
    {
      "type": "Action.Submit",
      "title": "✉️ Enviar por Email",
      "data": {
        "action": "sendEmail",
        "meetingId": "${meetingId}",
        "documentUrl": "${sharepointDocumentUrl}"
      },
      "tooltip": "Enviar a ata por email para todos os participantes"
    }
  ]
}
```

### 8.2 Variáveis de Template

| Variável | Tipo | Exemplo |
|---|---|---|
| `${meetingSubject}` | string | "Sprint Planning — Squad MEQ" |
| `${meetingDate}` | string | "08/06/2026" |
| `${meetingStartTime}` | string | "10:00" |
| `${meetingEndTime}` | string | "11:30" |
| `${participantCount}` | number | 8 |
| `${summaryBullets}` | string (markdown) | "• Ponto 1\n• Ponto 2\n• Ponto 3" |
| `${decision[1-3]StatusIcon}` | string | "🟢" / "🟡" / "🔴" |
| `${decision[1-3]Status}` | string | "Aprovado" / "Pendente" / "Rejeitado" |
| `${decision[1-3]Description}` | string | "Migração para Azure em fases" |
| `${action[1-5]Description}` | string | "Criar RFC de migração cloud" |
| `${action[1-5]Owner}` | string | "Wagner" |
| `${action[1-5]Deadline}` | string | "15/06" |
| `${action[1-5]StatusIcon}` | string | "🔴" / "🟡" / "⚪" / "🟢" |
| `${overallStatusStyle}` | string | "good" / "default" / "attention" |
| `${overallStatusIcon}` | string | "🟢" / "🟡" / "🔴" |
| `${overallStatusText}` | string | "Positivo" / "Neutro" / "Requer Atenção" |
| `${sharepointDocumentUrl}` | string (URL) | "https://empresa.sharepoint.com/..." |
| `${meetingId}` | string | "MTG-2026-0608-001" |

### 8.3 Regras de Status Geral

| Condição | Status |
|---|---|
| Todas as decisões aprovadas E nenhuma ação atrasada | 🟢 Positivo |
| Pelo menos 1 decisão pendente OU 1 ação com prazo próximo | 🟡 Neutro |
| Alguma decisão rejeitada OU ação atrasada OU risco alto identificado | 🔴 Requer Atenção |

### 8.4 Notas de Implementação

- **Versão mínima:** Adaptive Cards 1.5 (suportado no Teams Desktop, Web e Mobile)
- **Templating:** Usar [Adaptive Cards Templating SDK](https://learn.microsoft.com/en-us/adaptive-cards/templating/) para popular variáveis
- **Tamanho máximo:** O payload JSON do card não deve exceder 28 KB (limite do Teams)
- **Teste:** Validar no [Adaptive Cards Designer](https://adaptivecards.io/designer/) antes de deploy
- **Fallback:** Propriedade `fallbackText` garante que clientes antigos vejam ao menos o texto puro
- **Dark mode:** Adaptive Cards no Teams adaptam automaticamente as cores ao tema do usuário — evitar hardcoded colors quando possível, preferindo os tokens semânticos (`color: "Accent"`, `style: "emphasis"`)

---

> **Documento elaborado por Sally — UX Designer, Squad MEQ**  
> Para dúvidas ou sugestões de melhoria, entre em contato com a equipe de UX.
