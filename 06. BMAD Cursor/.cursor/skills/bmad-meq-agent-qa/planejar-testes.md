---
name: planejar-testes
description: Planeja cenários de teste
menu-code: PT
---

# Planejar Testes

Guie o usuário no planejamento de cenários de teste e estratégia de cobertura.

## Processo

1. **Entenda o escopo** — Feature, fluxo ou sistema a testar? (da Paula ou conversa)

2. **Tipos de teste:**
   - **Unit** — Funções, componentes isolados. Rápidos, muitos.
   - **Integration** — APIs, serviços, banco. Testam integração.
   - **API/Contract** — Contratos de API (Igor). Request/response, status codes.
   - **E2E** — Fluxos completos. Simulam usuário. Mais lentos.

3. **Cenários:**
   - Happy path — fluxo principal
   - Edge cases — limites, vazios, inválidos
   - Erros — tratamento de falhas

4. **Priorização:**
   - O que quebrar é mais crítico?
   - Cobertura primeiro nas áreas de risco

5. **Documente** — Resuma cenários. Sugira gerar E2E (GE) ou salvar (SM).

## Regras

- Cobertura primeiro, otimização depois
- Testes simples e mantíveis
- Nunca pular execução — sempre rodar e verificar
