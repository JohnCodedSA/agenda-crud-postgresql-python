import psycopg2

# Configuração da conexão
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgresDB',
    user = 'postgres',
    password = '123'
)

cursor = conn.cursor()

# --- Bloco da imagem de Exclusão ---
# Excluir dados
cursor.execute("""
DELETE FROM public."AGENDA"
    WHERE id = 1;
""")
conn.commit()

# --- Bloco da imagem de Leitura ---
# Ler os dados atualizados
cursor.execute("""
SELECT id, nome, telefone FROM public."AGENDA";
""")

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")

# Fechar a conexão
cursor.close()
conn.close()