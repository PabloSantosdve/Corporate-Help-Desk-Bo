from utils.file_manager import ler_json, salvar_json

dados_teste = {"senha": "Para resetar sua senha, acesse o portal de TI."}

salvou = salvar_json("data/teste.json", dados_teste)
print("Salvou com sucesso?", salvou)

dados_lidos = ler_json("data/teste.json")
print("Dados lidos:", dados_lidos)

dados_fantasma = ler_json("data/arquivo_que_nao_existe.json")
print("Dados de arquivo inexistente:", dados_fantasma)