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

if __name__ == '__main__':
    app.run(debug=True)