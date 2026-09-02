from flask import Flask, render_template, request
from chatbot.chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    pergunta = request.form['pergunta']
    resposta = chatbot.perguntar(pergunta)
    return resposta

@app.route('/abrir-chamado', methods=['POST'])
def abrir_chamado():
    nome = request.form['nome']
    departamento = request.form['departamento']
    categoria = request.form['categoria']
    descricao = request.form['descricao']
    protocolo = chatbot.abrir_chamado(nome, departamento, categoria, descricao)
    return f"Chamado aberto com sucesso! Protocolo: {protocolo}"

@app.route('/consultar-chamado', methods=['POST'])
def consultar_chamado():
    protocolo = request.form['protocolo']
    chamado = chatbot.consultar_chamado(protocolo)
    if isinstance(chamado, dict):
        return (
            f"Protocolo: {protocolo}<br>"
            f"Nome: {chamado['nome']}<br>"
            f"Departamento: {chamado['departamento']}<br>"
            f"Categoria: {chamado['categoria']}<br>"
            f"Descrição: {chamado['descricao']}<br>"
            f"Status: {chamado['status']}<br>"
            f"Data de Abertura: {chamado['data_abertura']}"
        )
    else:
        return chamado
    
if __name__ == '__main__':
    app.run(debug=True)