from datetime import date
from utils.file_manager import ler_json, salvar_json

class Chamado:
    def __init__(self, nome, departamento, categoria, descricao):
        self.nome = nome
        self.departamento = departamento
        self.categoria = categoria
        self.descricao = descricao
        self.status = "Aberto"
        self.data_abertura = date.today().strftime("%Y-%m-%d")

def gerar_protocolo():
    tickets = ler_json("data/tickets.json")
    quantidade_atual = len(tickets)
    proximo_numero = quantidade_atual + 1
    numero_formatado = str(proximo_numero).zfill(4)  # Preenche com zeros à esquerda para ter 4 dígitos
    protocolo = "TICKET- " + numero_formatado
    return protocolo

def abrir_chamado(nome, departamento, categoria, descricao):
    chamado = Chamado(nome, departamento, categoria, descricao)
    protocolo = gerar_protocolo()

    tickets = ler_json("data/tickets.json")
    tickets[protocolo] = chamado.__dict__
    salvar_json("data/tickets.json", tickets)

    return protocolo
