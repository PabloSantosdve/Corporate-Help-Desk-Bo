import datetime
from utils.file_manager import ler_json, salvar_json

def registrar_interacao(mensagem, resposta):
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    historico = ler_json("data/history.json")
    historico[data_hora] = {
        "mensagem": mensagem,
        "resposta": resposta
    }
    salvar_json("data/history.json", historico)