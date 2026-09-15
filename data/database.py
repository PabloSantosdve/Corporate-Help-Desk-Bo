import sqlite3

conexao = sqlite3.connect('data/database.db')
cursor = conexao.cursor()

# Passo 1: descobrir o id da categoria "email"
cursor.execute("SELECT id FROM categorias WHERE nome = ?", ("email",))
categoria_id = cursor.fetchone()[0]

# Passo 2: inserir a nova palavra-chave, ligada a esse id
cursor.execute("INSERT INTO palavras_chave (palavra, categoria_id) VALUES (?, ?)",
               ("configuração", categoria_id))

conexao.commit()
conexao.close()

print("Palavra-chave adicionada!")