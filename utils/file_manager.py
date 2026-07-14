import json

def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            dados = json.load(file)
            return dados
    except FileNotFoundError:
        dados = {}
        return dados
    except json.JSONDecodeError:
        dados = {}
        return dados


def salvar_json(caminho_arquivo, dados):
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            # Salva os dados em formato JSON formatado (indentado) e com suporte a acentos (ensure_ascii=False) Sem isso, o json.dump transformaria acentos em códigos estranhos tipo \u00e7 ao invés de mostrar "ç" de verdade no arquivo
        
            json.dump(dados, file, ensure_ascii=False, indent=4)
            return True
    except FileNotFoundError:
        return False
    except PermissionError:
        return False
    except TypeError:
        return False
    