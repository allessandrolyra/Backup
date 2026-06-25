# Cadastro de Médicos, Funções e Usuários

**Referência:** Maestro - [01_Orquestrador.md](01_Orquestrador.md)

---

## Agentes indicados para as atualizações

| Agente | Documento | Responsabilidade |
|--------|-----------|------------------|
| **Visionary** | 10_arquitetura_solucao.md | Arquitetura de roles, modelo de dados, fluxo de permissões |
| **Nexus** | 09_banco_integracoes.md | Schema SQL, tabelas, migrações, integração Supabase |
| **Shield** | 04_seguranca.md | RLS, políticas de acesso, auditoria de funções |
| **Insight** | 08_analise_codigo.md | Revisão de código, qualidade, testes após implementação |

---

## 1. Especialidades médicas (sugestão pré-cadastradas)

- Clínica Geral
- Cardiologia
- Dermatologia
- Endocrinologia
- Gastroenterologia
- Ginecologia e Obstetrícia
- Neurologia
- Oftalmologia
- Ortopedia
- Otorrinolaringologia
- Pediatria
- Pneumologia
- Psiquiatria
- Urologia

---

## 2. Sistema de funções (roles)

### 2.1 Funções pré-cadastradas

| Função | Descrição | Permissões |
|--------|-----------|------------|
| Administrador | Acesso total | CRUD usuários, funções, médicos, horários, consultas |
| Médico | Profissional de saúde | Ver agenda, confirmar próprias consultas |
| Atendente | Recepção | Cadastrar pacientes, agendar, listar consultas |
| Paciente | Usuário final | Agendar, ver e cancelar próprias consultas |

### 2.2 Funções customizáveis

- Admin pode criar novas funções (ex.: Enfermeiro, Gerente)
- Cada função tem nome, descrição e permissões (lista)
- Funções pré-cadastradas não podem ser excluídas (is_system = true)

---

## 3. Alterações no banco (Nexus)

### Novas tabelas

- **specialties** – id, name, is_system
- **roles** – id, name, description, is_system, permissions (JSONB)
- **profiles** – alterar: role_id FK para roles (substituir enum)
- **doctors** – alterar: specialty_id FK, user_id FK (vínculo com usuário)

### Seed

- Inserir 14 especialidades
- Inserir 4 funções pré-cadastradas com permissões

---

## 4. Interface (telas)

| Tela | Descrição |
|------|-----------|
| Admin > Funções | Listar, criar, editar funções |
| Admin > Usuários | Cadastrar usuário, escolher função |
| Admin > Médicos | Cadastro com especialidade, vínculo com usuário |

---

## 5. Ordem de execução (Maestro)

1. Nexus: migrations SQL
2. Nexus: seed
3. Shield: RLS
4. Implementação: telas Admin
5. Insight: revisão
