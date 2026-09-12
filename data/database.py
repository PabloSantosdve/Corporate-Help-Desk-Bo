import sqlite3

conexao = sqlite3.connect('data/database.db')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora TEXT,
        mensagem TEXT,
        resposta TEXT
    )
""")

conexao.commit()
conexao.close()