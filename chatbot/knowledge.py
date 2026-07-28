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

def obter_resposta(categorias, encontrados):
    if not encontrados:
        return "Desculpe, não encontrei uma resposta para a sua pergunta, por favor tente novamente ou entre em contato com o suporte."  
    elif len(encontrados) == 1:
        categoria = encontrados[0]
        return f"Encontrei uma resposta na categoria '{categoria}': {categorias[categoria]['resposta']}"
    elif len(encontrados) > 1:
        respostas = [f"{categoria}: {categorias[categoria]['resposta']}" for categoria in encontrados]
        return "Encontrei múltiplas respostas:\n" + "\n".join(respostas)
     