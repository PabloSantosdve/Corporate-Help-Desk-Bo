import tkinter as tk
from chatbot.chatbot import ChatBot

chatbot = ChatBot()

COR_FUNDO = "#0f172a"
COR_TITULO = "#e2e8f0"
COR_SUBTITULO = "#94a3b8"
COR_BOTAO = "#4f7cff"
COR_BOTAO_HOVER = "#3b63d6"
COR_SAIR = "#ef4444"
COR_SAIR_HOVER = "#dc2626"
COR_CARD = "#1e293b"
COR_TEXTO = "#cbd5e1"
COR_BORDA = "#334155"
COR_DICA = "#64748b"


def ao_clicar():
    pergunta = entrada.get()
    if not pergunta.strip():
        resultado_pergunta.config(text="Por favor, digite uma pergunta.", fg="#f87171")
    else:
        resposta = chatbot.perguntar(pergunta)
        resultado_pergunta.config(text=resposta, fg=COR_TEXTO)


def abrir_chamado_clicar():
    nome = entrada_nome.get()
    departamento = entrada_departamento.get()
    categoria = entrada_categoria.get()
    descricao = entrada_descricao.get()

    if not nome.strip() or not departamento.strip() or not categoria.strip() or not descricao.strip():
        resultado_chamado.config(text="Por favor, preencha todos os campos para abrir um chamado.", fg="#f87171")
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
        resultado_chamado.config(text=texto, fg=COR_TEXTO)


def consultar_chamado_clicar():
    protocolo = entrada_consultar.get()
    if not protocolo.strip():
        resultado_consulta.config(text="Por favor, insira o número ou protocolo para consultar o chamado.", fg="#f87171")
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
            resultado_consulta.config(text=texto, fg=COR_TEXTO)
        else:
            resultado_consulta.config(text=chamado, fg="#f87171")


def criar_botao(parent, texto, comando, cor_normal, cor_hover):
    botao = tk.Button(parent, text=texto, command=comando, bg=cor_normal, fg="white",
                       font=("Segoe UI", 11, "bold"), relief="flat", padx=14, pady=8,
                       activebackground=cor_hover, activeforeground="white", cursor="hand2",
                       borderwidth=0)
    botao.bind("<Enter>", lambda e: botao.config(bg=cor_hover))
    botao.bind("<Leave>", lambda e: botao.config(bg=cor_normal))
    return botao


janela_raiz = tk.Tk()
janela_raiz.title("Corporate Help Desk Bot")
janela_raiz.geometry("680x700")
janela_raiz.configure(bg=COR_FUNDO)

# Canvas + Scrollbar: permitem rolar o conteúdo quando ele é maior que a janela
canvas = tk.Canvas(janela_raiz, bg=COR_FUNDO, highlightthickness=0)
scrollbar = tk.Scrollbar(janela_raiz, orient="vertical", command=canvas.yview)
frame_scroll = tk.Frame(canvas, bg=COR_FUNDO)

frame_scroll.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Permite rolar com a roda do mouse
def rolar_com_mouse(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", rolar_com_mouse)

# A partir daqui, tudo que era "filho" de janela vira filho de frame_scroll
janela = frame_scroll

titulo = tk.Label(janela, text="Corporate Help Desk Bot", font=("Segoe UI", 22, "bold"), bg=COR_FUNDO, fg=COR_TITULO)
titulo.pack(pady=(24, 4))

subtitulo = tk.Label(janela, text="Suporte corporativo rápido e simples", font=("Segoe UI", 10), bg=COR_FUNDO, fg=COR_SUBTITULO)
subtitulo.pack(pady=(0, 20))

# Perguntar
secao_pergunta = tk.Frame(janela, bg=COR_CARD, highlightbackground=COR_BORDA, highlightthickness=1, padx=18, pady=18)
secao_pergunta.pack(pady=10, padx=25, fill="x")

label_pergunta = tk.Label(secao_pergunta, text="💬  Fazer uma pergunta", font=("Segoe UI", 13, "bold"), bg=COR_CARD, fg=COR_TITULO)
label_pergunta.pack(anchor="w")

entrada = tk.Entry(secao_pergunta, font=("Segoe UI", 11), relief="flat", bg="#0f172a", fg=COR_TEXTO,
                    insertbackground=COR_TEXTO, highlightbackground=COR_BORDA, highlightthickness=1)
entrada.pack(fill="x", pady=(10, 8), ipady=6)

botao = criar_botao(secao_pergunta, "Perguntar", ao_clicar, COR_BOTAO, COR_BOTAO_HOVER)
botao.pack(pady=4)

resultado_pergunta = tk.Label(secao_pergunta, text="", wraplength=600, font=("Segoe UI", 10), bg=COR_CARD,
                               fg=COR_TEXTO, justify="left")
resultado_pergunta.pack(pady=(8, 0), anchor="w")

# Abrir chamado
secao_chamado = tk.Frame(janela, bg=COR_CARD, highlightbackground=COR_BORDA, highlightthickness=1, padx=18, pady=18)
secao_chamado.pack(pady=10, padx=25, fill="x")

label_chamado_titulo = tk.Label(secao_chamado, text="📩 Abrir chamado", font=("Segoe UI", 13, "bold"), bg=COR_CARD, fg=COR_TITULO)
label_chamado_titulo.pack(anchor="w")

def campo_com_label(parent, texto_label):
    label = tk.Label(parent, text=texto_label, font=("Segoe UI", 9, "bold"), bg=COR_CARD, fg=COR_SUBTITULO)
    label.pack(anchor="w", pady=(10, 2))
    entrada_campo = tk.Entry(parent, font=("Segoe UI", 11), relief="flat", bg="#0f172a", fg=COR_TEXTO,
                              insertbackground=COR_TEXTO, highlightbackground=COR_BORDA, highlightthickness=1)
    entrada_campo.pack(fill="x", ipady=6)
    return entrada_campo

entrada_nome = campo_com_label(secao_chamado, "Nome")
entrada_departamento = campo_com_label(secao_chamado, "Departamento")
entrada_categoria = campo_com_label(secao_chamado, "Categoria")
entrada_descricao = campo_com_label(secao_chamado, "Descrição")

botao_chamado = criar_botao(secao_chamado, "Abrir Chamado", abrir_chamado_clicar, COR_BOTAO, COR_BOTAO_HOVER)
botao_chamado.pack(pady=(14, 4))

resultado_chamado = tk.Label(secao_chamado, text="", wraplength=600, font=("Segoe UI", 10), bg=COR_CARD,
                              fg=COR_TEXTO, justify="left")
resultado_chamado.pack(anchor="w")

# Consultar chamado
secao_consulta = tk.Frame(janela, bg=COR_CARD, highlightbackground=COR_BORDA, highlightthickness=1, padx=18, pady=18)
secao_consulta.pack(pady=10, padx=25, fill="x")

label_consulta_titulo = tk.Label(secao_consulta, text="🔍  Consultar chamado", font=("Segoe UI", 13, "bold"), bg=COR_CARD, fg=COR_TITULO)
label_consulta_titulo.pack(anchor="w")

entrada_consultar = campo_com_label(secao_consulta, "Protocolo")

label_dica_protocolo = tk.Label(secao_consulta, text="Dica: digite apenas o número (ex: 8) ou o protocolo completo (ex: TICKET-0008)",
                                 font=("Segoe UI", 8, "italic"), bg=COR_CARD, fg=COR_DICA)
label_dica_protocolo.pack(anchor="w", pady=(4, 0))

botao_consultar = criar_botao(secao_consulta, "Consultar Chamado", consultar_chamado_clicar, COR_BOTAO, COR_BOTAO_HOVER)
botao_consultar.pack(pady=(14, 4))

resultado_consulta = tk.Label(secao_consulta, text="", wraplength=600, font=("Segoe UI", 10), bg=COR_CARD,
                               fg=COR_TEXTO, justify="left")
resultado_consulta.pack(anchor="w")

# Sair
botao_sair = criar_botao(janela, "Sair", janela_raiz.destroy, COR_SAIR, COR_SAIR_HOVER)
botao_sair.pack(pady=24)

janela_raiz.mainloop()