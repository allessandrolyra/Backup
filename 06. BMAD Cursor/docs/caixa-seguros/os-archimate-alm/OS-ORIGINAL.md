# OS Original - Mapeamento de Arquitetura Corporativa e Rastreabilidade ALM

> **Recebida em:** 08/04/2026
> **Prazo para resposta:** 5 dias uteis

---

## Referencia Metodologica
- TOGAF Standard, 10th Edition
- ArchiMate 3.2
- Architecture-as-Code (Git-based via Archi Collaboration Plugin)
- Azure DevOps (ADO) & Neo4j Graph DB

---

## 1. Objetivo Estrategico

Mapeamento logico-estrutural da organizacao, estabelecendo um "Gemeo Digital" da arquitetura corporativa.
Foco em Objetos de Arquitetura (Abstracoes Logicas), NAO instancias fisicas (CMDB).
Rastreabilidade total: estrategia de negocio <-> componentes tecnologicos <-> ALM.

## 2. Escopo de Mapeamento (Camadas ArchiMate)

- **Camada de Negocio:** Capabilities, Processos, Funcoes, Atores + Parceiros Externos (obrigatorio)
- **Camada de Aplicacao:** Componentes e Servicos de Aplicacao (responsabilidades funcionais + interfaces)
- **Camada de Tecnologia:** Nos logicos, plataformas de servico, infraestrutura de suporte
- **Interdependencias:** APIs, Troca de Arquivos (Batch/SFTP), Mensageria, integracoes com terceiros

Granularidade suficiente para tomada de decisao tecnica, SEM detalhe de infra fisica.

## 3. Taxonomia de Relacionamentos

| Categoria | Tipos | Aplicacao |
|-----------|-------|-----------|
| Estruturais | Composition, Assignment, Realization | Hierarquias e entrega de servicos |
| Dependencia | Serving, Access, Influence | APIs, consumo de dados, conformidade |
| Dinamicos | Triggering, Flow | Orquestracao de processos e fluxos |

## 4. Integracao com Azure DevOps & ALM (MANDATORIO)

- Work Items (User Story, Feature, Task) vinculados ao ID do objeto ArchiMate
- Vinculo componente logico <-> repositorio de codigo (Azure Repos)
- Pipeline automatico: alteracao Git -> atualiza Neo4j

## 5. Neo4j - Consulta e Analise de Impacto

- Consultas de impacto (alteracao API -> processos afetados)
- Dashboard de Coerencia: "Desenvolvimentos Sombra" + "Arquiteturas Orfas"

## 6. Governanca

- Git-based (Archi Collaboration Plugin)
- Portabilidade: Open Exchange Format XML

## 7. Entregaveis

1. Repositorio Git com modelo ArchiMate versionado
2. Scripts de Ingestao Cypher para Neo4j + pipeline ADO
3. Matriz de Rastreabilidade Dinamica (Business -> App -> Tech -> Work Item)
4. Manual de Taxonomia

## 8. Estimativa de Custo

- Perfis + horas por perfil
- Valor-hora conforme tabela contratual
- 100% off-site
- Pagamento por entrega

## 9. Estimativa de Prazo

- Prazo em dias por entrega
- Inicio: 10 dias apos OS aceita e assinada
- Resposta a cotacao: 5 dias uteis
