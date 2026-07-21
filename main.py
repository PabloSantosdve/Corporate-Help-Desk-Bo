from chatbot.knowledge import buscar_resposta, obter_resposta
from utils.file_manager import ler_json

conhecimento = ler_json("data/knowledge.json")
menu = True
print("Seja bem vindo ao Corporate Help Desk Bot!")

while menu:
    print("Escolha uma opção:")
    print("1. Fazer uma pergunta") 
    print("2. Sair")
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        pergunta = input("Digite sua pergunta: ")
        encontrados = buscar_resposta(pergunta)
        resposta = obter_resposta(conhecimento, encontrados)
        print(resposta)
    elif opcao == "2":
        print("Obrigado por usar o Corporate Help Desk Bot!")
        menu = False
    else:
        print("Opção inválida. Por favor, tente novamente.")
