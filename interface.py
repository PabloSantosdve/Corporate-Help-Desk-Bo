import tkinter  as tk
from chatbot.chatbot import ChatBot

chatbot = ChatBot()

def ao_clicar():
    pergunta = entrada.get()
    resposta = chatbot.perguntar(pergunta)
    resultado.config(text=resposta)

janela = tk.Tk()
janela.title("Corporate Help Desk Bot") 
janela.geometry("1220x980") #Definindo o tamanho da janela

titulo = tk.Label(janela, text="Corporate Help Desk Bot")
titulo.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Perguntar", command=ao_clicar)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()
