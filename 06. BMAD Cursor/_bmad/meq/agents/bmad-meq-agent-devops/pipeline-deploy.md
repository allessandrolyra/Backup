---
name: pipeline-deploy
description: Configura pipeline de deploy
menu-code: PD
---

# Pipeline de Deploy

Guie o usuário na configuração do pipeline de deploy — staging e produção.

## Processo

1. **Entenda o contexto** — GitHub Actions, GitLab CI, outro? Web, Android ou iOS?

2. **Ambientes:**
   - Staging — deploy automático em merge para main/develop?
   - Produção — manual approval ou automático?
   - Variáveis por ambiente (API_URL, secrets)

3. **Stages de deploy:**
   - Build artifact (web: dist/, mobile: APK/IPA)
   - Push para registry (Docker) ou store (mobile)
   - Deploy para hosting (Vercel, AWS, etc.)

4. **Segurança:**
   - Secrets em variáveis de ambiente (nunca no código)
   - Least privilege — permissões mínimas necessárias
   - Rollback — como reverter se algo falhar

5. **Observabilidade (produção):**
   - Logs — formato estruturado, níveis, retenção
   - Métricas — latência, erros, throughput
   - Alertas — quando algo falha ou degrada
   - Health checks — endpoints para monitoramento

6. **Memória** — Se decisões importantes, sugira salvar (SM).

## Regras

- Automação primeiro — nada manual em produção
- Reprodutibilidade — mesmo build, mesmo resultado
- Rollback documentado e testável
