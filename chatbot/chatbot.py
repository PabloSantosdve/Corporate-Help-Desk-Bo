from chatbot.knowledge import buscar_resposta, obter_resposta
from chatbot.history import registrar_interacao
from chatbot.tickets import abrir_chamado as abrir_chamado_service, consultar_chamado as consultar_chamado_service
from utils.file_manager import ler_json, salvar_json

class ChatBot:
    def __init__(self):
        self.conhecimento = ler_json("data/knowledge.json")

    def perguntar(self, pergunta):
        encontrados = buscar_resposta(pergunta)
        resposta = obter_resposta(self.conhecimento, encontrados)
        registrar_interacao(pergunta, resposta)
        return resposta

    def abrir_chamado(self, nome, departamento, categoria, descricao):
        protocolo = abrir_chamado_service(nome, departamento, categoria, descricao)
        return protocolo

    def consultar_chamado(self, protocolo):
        chamado = consultar_chamado_service(protocolo)
        return chamado