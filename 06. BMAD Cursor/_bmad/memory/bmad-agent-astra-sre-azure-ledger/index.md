# Project Memory Ledger — Astra SRE Azure

> **Última atualização:** 2026-05-07T18:00:00-03:00  
> **Agente:** bmad-agent-astra-sre-azure  
> **Subscription:** Visual Studio Enterprise Subscription (9cfd9e0c-2a0a-4f03-9386-43f53b03da4d)

---

## Status do Ambiente

| Ferramenta | Status | Versão |
|------------|--------|--------|
| Azure CLI | ✅ Instalado | 2.83.0 |
| Terraform | ✅ Instalado | 1.14.8 |
| Bicep CLI | ❌ Não instalado | — |
| Autenticação Azure | ✅ Logado | VS Enterprise |

---

## Histórico de Sessões

### Sessão 1 — 2026-05-07

**Contexto:** Usuário solicitou informações sobre provisionamento de VNET no Azure.

**Decisões:**
- Apresentar opções de IaC: Terraform (padrão) vs Bicep
- Seguir padrão Hub-Spoke CAF para enterprise
- Definir CIDR planning sem overlaps

**Artefatos Gerados:**
- [ ] Módulo Terraform para VNET (pendente aprovação)
- [ ] Documentação de pré-requisitos

**Pendências:**
- Instalar Bicep CLI (opcional): `az bicep install`
- Definir CIDR range do projeto
- Definir região e ambiente (dev/stg/prd)

### Sessão 2 — 2026-05-07

**Contexto:** Usuário solicitou requisitos para provisionar **Storage (Storage Account)** no Azure.

**Decisões:**
- Cobrir SKU/replicação (LRS/ZRS/GRS/GZRS), tier (Hot/Cool/Archive), e caminho enterprise (private endpoint + TLS 1.2+).
- Diferenciar **Storage Account genérico** vs **ADLS Gen2** (`isHnsEnabled`) para analytics/lakehouse.

**Artefatos Gerados:**
- [ ] Módulo Terraform/Bicep para Storage Account (pendente parâmetros: RG, nome globalmente único, SKU, networking).

**Pendências:**
- Escolher **tipo de workload** (blobs, filas, tabelas, files, data lake).
- Definir **rede** (public endpoint com firewall vs private endpoint).
- Definir **soft delete / versioning / immutability** conforme compliance.

---

## Decisões Arquiteturais (ADRs)

*Nenhuma ADR registrada ainda.*

---

## Artefatos Entregues

| Data | Artefato | Tipo | Status |
|------|----------|------|--------|
| — | — | — | — |

