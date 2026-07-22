import psycopg2

# Configuração da conexão
conn = psycopg2.connect(
    host='localhost',
    database='postgresDB',
    user='postgres',
    password='123'
)

cursor = conn.cursor()

# Criação da tabela (sem a parte do OWNER)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS public."AGENDA"
    (
        id integer NOT NULL,
        nome text NOT NULL,
        telefone char(12) NOT NULL
    );
""")

# Inserir dados na tabela
cursor.execute("""
    INSERT INTO public."AGENDA" (id, nome, telefone)
    VALUES (1, 'teste 1', '02199999999');
""")

cursor.execute("""
    INSERT INTO public."AGENDA" (id, nome, telefone)
    VALUES (2, 'teste 2', '02188888888');
""")

conn.commit()

# Ler os dados
cursor.execute("""
    SELECT id, nome, telefone FROM public."AGENDA";
""")

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")

# Fechar a conexão
cursor.close()
conn.close()