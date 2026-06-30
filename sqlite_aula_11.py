# Exercício 1 – ex01_sqlite.py
import sqlite3
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# criando a tabela de produtos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL
    )
""")

conexao.commit()

# inserindo os três produtos
cursor.execute(
    "INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?)",
    (1, "Arroz", 5.50)
)

cursor.execute(
    "INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?)",
    (2, "Feijão", 6.50)
)

cursor.execute(
    "INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?)",
    (3, "Calabresa", 7.00)
)

# Exercício 2 – ex02_sqlite.py
conexao.row_factory = sqlite3.Row
cursor.execute(" SELECT * FROM produtos")
todos = cursor.fetchall()
for linha in todos:
    print(dict(linha))

# Exercício 3 – Desafio – ex03_sqlite.py
# testes http 
