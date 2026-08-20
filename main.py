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
        if not pergunta.strip():
            print("Por favor, digite uma pergunta.")
        else:
            resposta = chatbot.perguntar(pergunta)
            print(resposta)

    elif opcao == "2":
        print("Abrindo um chamado...")
        nome = input("Digite seu nome: ")
        departamento = input("Digite seu departamento: ")
        categoria = input("Digite a categoria do problema: ")
        descricao = input("Descreva o problema: ")

        if not nome.strip() or not departamento.strip() or not categoria.strip() or not descricao.strip():
            print("Por favor, preencha todos os campos para abrir um chamado.")
        else:
            protocolo = chatbot.abrir_chamado(nome, departamento, categoria, descricao)
            print("\nChamado aberto com sucesso!")
            print(f"Protocolo: {protocolo}")
            print(f"Nome: {nome}")
            print(f"Departamento: {departamento}")
            print(f"Categoria: {categoria}")
            print(f"Descrição: {descricao}")

    elif opcao == "3":
        print("Consultando um chamado existente...")
        protocolo = input("Digite o número ou protocolo do chamado (ex: 8 ou TICKET-0008): ")
        chamado = chatbot.consultar_chamado(protocolo)
        if isinstance(chamado, dict):
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
    