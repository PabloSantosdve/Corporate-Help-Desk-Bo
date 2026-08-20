import tkinter as tk
from chatbot.chatbot import ChatBot

chatbot = ChatBot()

COR_FUNDO = "#f0f4f8"
COR_TITULO = "#1a3c5e"
COR_BOTAO = "#2e6ff2"
COR_SAIR = "#e74c3c"
COR_CARD = "#ffffff"


def ao_clicar():
    pergunta = entrada.get()
    if not pergunta.strip():
        resultado_pergunta.config(text="Por favor, digite uma pergunta.")
    else:
        resposta = chatbot.perguntar(pergunta)
        resultado_pergunta.config(text=resposta)


def abrir_chamado_clicar():
    nome = entrada_nome.get()
    departamento = entrada_departamento.get()
    categoria = entrada_categoria.get()
    descricao = entrada_descricao.get()

    if not nome.strip() or not departamento.strip() or not categoria.strip() or not descricao.strip():
        resultado_chamado.config(text="Por favor, preencha todos os campos para abrir um chamado.")
    else:
        protocolo = chatbot.abrir_chamado(nome, departamento, categoria, descricao)
        texto = (
            f"Chamado aberto com sucesso!\n"
            f"Protocolo: {protocolo}\n"
            f"Nome: {nome}\n"
            f"Departamento: {departamento}\n"
            f"Categoria: {categoria}\n"
            f"Descrição: {descricao}"
        )
        resultado_chamado.config(text=texto)


def consultar_chamado_clicar():
    protocolo = entrada_consultar.get()
    if not protocolo.strip():
        resultado_consulta.config(text="Por favor, insira o número ou protocolo para consultar o chamado.")
    else:
        chamado = chatbot.consultar_chamado(protocolo)
        if isinstance(chamado, dict):
            texto = (
                f"Nome: {chamado['nome']}\n"
                f"Departamento: {chamado['departamento']}\n"
                f"Categoria: {chamado['categoria']}\n"
                f"Descrição: {chamado['descricao']}\n"
                f"Status: {chamado['status']}\n"
                f"Data de Abertura: {chamado['data_abertura']}"
            )
            resultado_consulta.config(text=texto)
        else:
            resultado_consulta.config(text=chamado)


janela = tk.Tk()
janela.title("Corporate Help Desk Bot")
janela.geometry("650x880")
janela.configure(bg=COR_FUNDO)

titulo = tk.Label(janela, text="Corporate Help Desk Bot", font=("Arial", 22, "bold"), bg=COR_FUNDO, fg=COR_TITULO)
titulo.pack(pady=20)

# Perguntar
secao_pergunta = tk.Frame(janela, bg=COR_CARD, bd=1, relief="solid", padx=15, pady=15)
secao_pergunta.pack(pady=10, padx=25, fill="x")

label_pergunta = tk.Label(secao_pergunta, text="Fazer uma pergunta", font=("Arial", 14, "bold"), bg=COR_CARD, fg=COR_TITULO)
label_pergunta.pack(anchor="w")

entrada = tk.Entry(secao_pergunta, font=("Arial", 12), relief="solid", bd=1)
entrada.pack(fill="x", pady=8)

botao = tk.Button(secao_pergunta, text="Perguntar", command=ao_clicar, bg=COR_BOTAO, fg="white",
                   font=("Arial", 11, "bold"), relief="flat", padx=10, pady=5)
botao.pack(pady=5)

resultado_pergunta = tk.Label(secao_pergunta, text="", wraplength=550, font=("Arial", 12), bg=COR_CARD,
                               fg="#333333", justify="left")
resultado_pergunta.pack(pady=5, anchor="w")

# Abrir chamado
secao_chamado = tk.Frame(janela, bg=COR_CARD, bd=1, relief="solid", padx=15, pady=15)
secao_chamado.pack(pady=10, padx=25, fill="x")

label_chamado_titulo = tk.Label(secao_chamado, text="Abrir chamado", font=("Arial", 14, "bold"), bg=COR_CARD, fg=COR_TITULO)
label_chamado_titulo.pack(anchor="w")

label_nome = tk.Label(secao_chamado, text="Nome:", font=("Arial", 11), bg=COR_CARD, fg=COR_TITULO)
label_nome.pack(anchor="w", pady=(8, 0))
entrada_nome = tk.Entry(secao_chamado, font=("Arial", 11))
entrada_nome.pack(fill="x")

label_departamento = tk.Label(secao_chamado, text="Departamento:", font=("Arial", 11), bg=COR_CARD, fg=COR_TITULO)
label_departamento.pack(anchor="w", pady=(8, 0))
entrada_departamento = tk.Entry(secao_chamado, font=("Arial", 11))
entrada_departamento.pack(fill="x")

label_categoria = tk.Label(secao_chamado, text="Categoria:", font=("Arial", 11), bg=COR_CARD, fg=COR_TITULO)
label_categoria.pack(anchor="w", pady=(8, 0))
entrada_categoria = tk.Entry(secao_chamado, font=("Arial", 11))
entrada_categoria.pack(fill="x")

label_descricao = tk.Label(secao_chamado, text="Descrição:", font=("Arial", 11), bg=COR_CARD, fg=COR_TITULO)
label_descricao.pack(anchor="w", pady=(8, 0))
entrada_descricao = tk.Entry(secao_chamado, font=("Arial", 11))
entrada_descricao.pack(fill="x")

botao_chamado = tk.Button(secao_chamado, text="Abrir Chamado", command=abrir_chamado_clicar, bg=COR_BOTAO,
                           fg="white", font=("Arial", 11, "bold"), relief="flat", padx=10, pady=5)
botao_chamado.pack(pady=10)

resultado_chamado = tk.Label(secao_chamado, text="", wraplength=550, font=("Arial", 12), bg=COR_CARD,
                              fg="#333333", justify="left")
resultado_chamado.pack(anchor="w")

# Consultar chamado
secao_consulta = tk.Frame(janela, bg=COR_CARD, bd=1, relief="solid", padx=15, pady=15)
secao_consulta.pack(pady=10, padx=25, fill="x")

label_consulta_titulo = tk.Label(secao_consulta, text="Consultar chamado", font=("Arial", 14, "bold"), bg=COR_CARD, fg=COR_TITULO)
label_consulta_titulo.pack(anchor="w")

label_consultar_chamado = tk.Label(secao_consulta, text="Protocolo:", font=("Arial", 11), bg=COR_CARD, fg=COR_TITULO)
label_consultar_chamado.pack(anchor="w", pady=(8, 0))
entrada_consultar = tk.Entry(secao_consulta, font=("Arial", 11))
entrada_consultar.pack(fill="x")

label_dica_protocolo = tk.Label(secao_consulta, text="Dica: digite apenas o número (ex: 8) ou o protocolo completo (ex: TICKET-0008)",
                                 font=("Arial", 9, "italic"), bg=COR_CARD, fg="#777777")
label_dica_protocolo.pack(anchor="w", pady=(2, 0))

botao_consultar = tk.Button(secao_consulta, text="Consultar Chamado", command=consultar_chamado_clicar,
                             bg=COR_BOTAO, fg="white", font=("Arial", 11, "bold"), relief="flat", padx=10, pady=5)
botao_consultar.pack(pady=10)

resultado_consulta = tk.Label(secao_consulta, text="", wraplength=550, font=("Arial", 12), bg=COR_CARD,
                               fg="#333333", justify="left")
resultado_consulta.pack(anchor="w")

# Sair
botao_sair = tk.Button(janela, text="Sair", command=janela.destroy, bg=COR_SAIR, fg="white",
                        font=("Arial", 11), relief="flat", padx=10, pady=5)
botao_sair.pack(pady=20)

janela.mainloop()