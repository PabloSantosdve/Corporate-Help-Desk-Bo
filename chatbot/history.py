import datetime
import sqlite3

def registrar_interacao(mensagem, resposta):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conexao = sqlite3.connect('data/database.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO history (data_hora, mensagem, resposta) VALUES (?, ?, ?)",
                   (data_hora, mensagem, resposta))
    conexao.commit()
    conexao.close()
