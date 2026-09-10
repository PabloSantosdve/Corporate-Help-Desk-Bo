from datetime import date
import sqlite3

class Chamado:
    def __init__(self, nome, departamento, categoria, descricao):
        self.nome = nome
        self.departamento = departamento
        self.categoria = categoria
        self.descricao = descricao
        self.status = "Aberto"
        self.data_abertura = date.today().strftime("%Y-%m-%d")

def gerar_protocolo():
    conexao = sqlite3.connect('data/database.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT count(protocolo) from tickets")
    resultado = cursor.fetchone()
    protocolo = f"TICKET-{resultado[0] + 1:04d}"
    conexao.close()
    return protocolo

def abrir_chamado(nome, departamento, categoria, descricao):
    chamado = Chamado(nome, departamento, categoria, descricao)
    protocolo = gerar_protocolo()
    conexao = sqlite3.connect('data/database.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tickets (protocolo, nome, departamento, categoria, descricao, status, data_abertura) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (protocolo, chamado.nome, chamado.departamento, chamado.categoria, chamado.descricao, chamado.status, chamado.data_abertura))
    conexao.commit()
    conexao.close()
    return protocolo

def consultar_chamado(protocolo):
    protocolo = protocolo.strip().upper()
    if not protocolo.startswith("TICKET-"):
        protocolo = f"TICKET-{protocolo.zfill(4)}"

    conexao = sqlite3.connect('data/database.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tickets WHERE protocolo = ?", (protocolo,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return {
            "protocolo": resultado[0],
            "nome": resultado[1],
            "departamento": resultado[2],
            "categoria": resultado[3],
            "descricao": resultado[4],
            "status": resultado[5],
            "data_abertura": resultado[6]
        }
    else:
        return "Chamado não encontrado."
