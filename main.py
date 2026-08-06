from chatbot.chatbot import ChatBot

chatbot = ChatBot()
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
        resposta = chatbot.perguntar(pergunta)
        print(f"Resposta: {resposta}")
    elif opcao == "2":
        print("Abrindo um chamado...")
        nome = input("Digite seu nome: ")
        departamento = input("Digite seu departamento: ")
        categoria = input("Digite a categoria do problema: ")
        descricao = input("Descreva o problema: ")
        protocolo = chatbot.abrir_chamado(nome, departamento, categoria, descricao)
        print(f"Chamado aberto com sucesso! Protocolo: {protocolo}")
    elif opcao == "3":
        print("Consultando um chamado existente...")
        protocolo = input("Digite o protocolo do chamado: ")
        chamado = chatbot.consultar_chamado(protocolo)
        if isinstance(chamado, dict):
            print(f"Protocolo: {protocolo}")
            print(f"Nome: {chamado['nome']}")
            print(f"Departamento: {chamado['departamento']}")
            print(f"Categoria: {chamado['categoria']}")
            print(f"Descrição: {chamado['descricao']}")
        else:
            print(chamado)
    elif opcao == "4":
        print("Obrigado por usar o Corporate Help Desk Bot!")
        menu = False
    else:
        print("Opção inválida. Por favor, tente novamente.")
