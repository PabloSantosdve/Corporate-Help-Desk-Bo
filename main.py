from chatbot.knowledge import buscar_resposta, obter_resposta
from chatbot.history import registrar_interacao
from chatbot.tickets import abrir_chamado, consultar_chamado
from utils.file_manager import ler_json

conhecimento = ler_json("data/knowledge.json")
menu = True
print("Seja bem vindo ao Corporate Help Desk Bot!")

while menu:
    print("Escolha uma opção:")
    print("1. Fazer uma pergunta") 
    print("2. Abrir Chamado") 
    print("3. Consultar um Chamado") 
    print("4. Sair")
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        pergunta = input("Digite sua pergunta: ")
        encontrados = buscar_resposta(pergunta)
        resposta = obter_resposta(conhecimento, encontrados)
        print(resposta)
        registrar_interacao(pergunta, resposta)
    elif opcao == "2":
        print("Abrindo um novo chamado...")
        nome = input("Digite seu nome: ")
        departamento = input("Digite o departamento: ")
        categoria = input("Digite a categoria: ")
        descricao = input("Digite a descrição do problema: ")
        protocolo = abrir_chamado(nome, departamento, categoria, descricao)
        print(f"Chamado aberto com sucesso! Protocolo: {protocolo}")
    elif opcao == "3":
        print("Consultando um chamado existente...")
        protocolo = input("Digite o protocolo do chamado: ")
        chamado = consultar_chamado(protocolo)
        if isinstance(chamado, dict):
            print(f"Protocolo: {protocolo}")
            print(f"Nome: {chamado['nome']}")
            print(f"Departamento: {chamado['departamento']}")
            print(f"Categoria: {chamado['categoria']}")
            print(f"Descrição: {chamado['descricao']}")
            print(f"Status: {chamado['status']}")
            print(f"Data de Abertura: {chamado['data_abertura']}")
        else:
            print(chamado)
    elif opcao == "4":
        print("Obrigado por usar o Corporate Help Desk Bot!")
        menu = False
    else:
        print("Opção inválida. Por favor, tente novamente.")
