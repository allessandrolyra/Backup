# 🤖 Agentes que ajudam no Deploy no GitHub

Mapeamento dos agentes da equipe DevOps para cada etapa da publicação do projeto.

---

## Fluxo geral

```
[01 Orquestrador] → coordena
       ↓
[02 CI] → valida build
       ↓
[03 CD] → faz deploy
       ↓
[04 Segurança] → protege credenciais
       ↓
[06 Observabilidade] → monitora o site
```

---

## Por etapa

| Etapa | Agente | Como ajuda |
|-------|--------|------------|
| **Preparar código** | **08_analise_codigo** | Revisa qualidade, sugere melhorias antes do push |
| **Build e testes** | **02_ci** | Garante que o build passa (GitHub Actions) |
| **Deploy** | **03_cd** | Automatiza publicação no GitHub Pages |
| **Segurança** | **04_seguranca** | Garante que .env não vai pro repo, valida secrets |
| **Infra** | **05_iac** | Workflow como código (`.github/workflows/`) |
| **Integração** | **09_banco_integracoes** | Configura Supabase, Redirect URLs |
| **Monitoramento** | **06_observabilidade** | Health check, logs, disponibilidade |
| **Comunicação** | **07_colaboracao** | Documentação, checklist, notificações |
| **Arquitetura** | **10_arquitetura_solucao** | Decisões de base path, SPA, etc. |

---

## Ordem sugerida para usar os agentes

1. **01_Orquestrador** – Define o plano e prioridades
2. **04_seguranca** – Confere .gitignore e secrets
3. **09_banco_integracoes** – Ajusta Supabase para produção
4. **02_ci** / **03_cd** – Configura e valida o pipeline
5. **06_observabilidade** – Configura health check e monitoramento
6. **07_colaboracao** – Atualiza documentação e checklist

---

## Arquivos criados para deploy

| Arquivo | Responsável (agente) |
|---------|----------------------|
| `.github/workflows/deploy.yml` | 03_cd, 05_iac |
| `DEPLOY_GITHUB.md` | 07_colaboracao |
| `vite.config.ts` (base path) | 10_arquitetura_solucao |
| `.gitignore` | 04_seguranca |

---

*Documento de referência para o projeto Agenda Médica*
