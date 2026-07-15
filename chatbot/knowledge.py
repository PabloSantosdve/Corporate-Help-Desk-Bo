from utils.file_manager import ler_json

def buscar_resposta(pergunta):
    encontrados = []
    conhecimento = ler_json("data/knowledge.json")

    for categoria, dados_categoria in conhecimento.items():
        for palavra_chave in dados_categoria["palavras_chave"]:
            if palavra_chave.lower() in pergunta.lower():
                encontrados.append(categoria)
                break  # Para evitar múltiplas respostas para a mesma pergunta

    return encontrados