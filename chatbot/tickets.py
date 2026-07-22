from datetime import date

class Chamado:
    def __init__(self, nome, departamento, categoria, descricao):
        self.nome = nome
        self.departamento = departamento
        self.categoria = categoria
        self.descricao = descricao
        self.status = "Aberto"
        self.data_abertura = date.today().strftime("%Y-%m-%d")

