import sqlite3

conexao = sqlite3.connect('data/database.db')
cursor = conexao.cursor()
  
cursor.execute("SELECT count(protocolo) from tickets")
resultado = cursor.fetchall()
print(resultado)

conexao.commit()
conexao.close()
