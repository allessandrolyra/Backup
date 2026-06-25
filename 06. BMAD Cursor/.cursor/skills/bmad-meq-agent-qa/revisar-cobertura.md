---
name: revisar-cobertura
description: Revisa cobertura de testes
menu-code: RC
---

# Revisar Cobertura

Analise a cobertura de testes e identifique gaps.

## Processo

1. **Entenda o projeto** — Stack, estrutura de testes existente.

2. **Áreas a revisar:**
   - Features críticas — estão cobertas?
   - APIs — testes de contrato?
   - Fluxos E2E — principais jornadas?
   - Edge cases — limites e erros?

3. **Gaps comuns:**
   - Feature nova sem testes
   - API sem testes de integração
   - Fluxo crítico sem E2E
   - Tratamento de erro não testado

4. **Recomendações:**
   - Priorize por risco
   - Sugira cenários faltantes
   - Indique GE para gerar E2E quando apropriado

5. **Documente** — Registre gaps e plano. Sugira salvar (SM).

## Regras

- Foco em áreas de alto risco — o que quebrar seria crítico?
- Cobertura útil > cobertura numérica — priorize cenários que importam
- Testes que não rodam não valem — sempre executar e verificar
