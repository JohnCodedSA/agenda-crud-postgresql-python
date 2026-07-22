# 📞 Agenda Eletrônica (Python & PostgreSQL)

Aplicação em **Python** integrada ao banco de dados relacional **PostgreSQL** através da biblioteca **psycopg2**, demonstrando as operações fundamentais de criação, manipulação, atualização e exclusão de dados (CRUD).

---

### 🚀 Funcionalidades e Conceitos Demonstrados

- **Conexão com Banco de Dados Relacional:**
  - Estabelecimento de conexão com o PostgreSQL (`psycopg2.connect`).
  - Gerenciamento de sessão e fecho de conexões (`cursor.close()`, `conn.close()`).
  - Tratamento de exceções e uso de blocos `try/except/finally` para controle de erros.
- **Operações SQL no PostgreSQL:**
  - **DDL:** Criação da tabela `AGENDA` com restrições `NOT NULL` e tipos de dados nativos (`integer`, `text`, `char`).
  - **DML:** Inserção de dados com tratamento para evitar erros de duplicidade (`psycopg2.errors.UniqueViolation`).
  - **Consultas e Leitura:** Seleção (`SELECT`) e exibição formatada dos registros.
  - **Exclusão:** Remoção de registros utilizando a cláusula `WHERE`.

---

### 🛠️ Tecnologias Utilizadas

- **Python 3**
- **PostgreSQL**
- **Psycopg2** (Driver de integração Python-PostgreSQL)

---

### 💻 Como executar o projeto

1. Certifique-se de ter o **Python 3** e o **PostgreSQL** instalados no computador.
2. Crie um banco de dados no seu PostgreSQL com o nome `postgresDB` (ou ajuste as credenciais nos arquivos se necessário).
3. Instale a dependência necessária:
   - `pip install -r requirements.txt`
4. Execute os scripts na ordem recomendada:
   - **Passo 1 (Criar e inserir):** `python Create.py`
   - **Passo 2 (Atualizar e listar):** `python Update.py`
   - **Passo 3 (Deletar e verificar):** `python Delete.py`

---

### 📄 Código Fonte

Você pode conferir os scripts do projeto nos links abaixo:
- 📄 **[Acessar Create.py](https://github.com/JohnCodedSA/agenda-crud-postgresql-python/blob/main/Create.py)**
- 📄 **[Acessar Update.py](https://github.com/JohnCodedSA/agenda-crud-postgresql-python/blob/main/Update.py)**
- 📄 **[Acessar Delete.py](https://github.com/JohnCodedSA/agenda-crud-postgresql-python/blob/main/Delete.py)**
