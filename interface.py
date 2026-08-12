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
janela.configure(bg="#f0f4f8")  # cor de fundo da janela

titulo = tk.Label(janela, text="Corporate Help Desk Bot", font=("Arial", 24, "bold"), bg="#f0f4f8", fg="#1a3c5e")
titulo.pack(pady=20)

entrada = tk.Entry(janela, width=50, font=("Arial", 14), relief="solid", bd=1)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Perguntar", command=ao_clicar, bg="#2e6ff2", fg="white", font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5)
botao.pack(pady=10)

resultado = tk.Label(janela, text="", wraplength=450, font=("Arial", 13), bg="#f0f4f8", fg="#333333", justify="left")
resultado.pack(pady=15)

botao_sair = tk.Button(janela, text="Sair", command=janela.destroy, bg="#e74c3c", fg="white", font=("Arial", 11), relief="flat", padx=10, pady=5)
botao_sair.pack(pady=10)

janela.mainloop()
