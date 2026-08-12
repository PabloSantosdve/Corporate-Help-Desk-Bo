import tkinter  as tk
from chatbot.chatbot import ChatBot

chatbot = ChatBot()

def ao_clicar():
    pergunta = entrada.get()
    resposta = chatbot.perguntar(pergunta)
    resultado.config(text=resposta)

janela = tk.Tk()
janela.title("Corporate Help Desk Bot") 
janela.geometry("600x500") #Definindo o tamanho da janela

titulo = tk.Label(janela, text="Corporate Help Desk Bot" , font=("Arial", 24, "bold"))
titulo.pack()

entrada = tk.Entry(janela, width=50, font=("Arial", 14))
entrada.pack(pady=10)

botao = tk.Button(janela, text="Perguntar", command=ao_clicar)
botao.pack(pady=10)

resultado = tk.Label(janela, text="", wraplength=400, font=("Arial", 14))
resultado.pack(pady=10)

botao_sair = tk.Button(janela, text="Sair", command=janela.destroy)
botao_sair.pack(pady=10)

janela.mainloop()
