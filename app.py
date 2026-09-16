from flask import Flask, render_template, request
from chatbot.chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    pergunta = request.form['pergunta']
    if not pergunta.strip():
        return render_template('resultado.html', titulo="Ops!",
                                conteudo="Por favor, digite uma pergunta.", erro=True)

    resposta = chatbot.perguntar(pergunta)
    return render_template('resultado.html', titulo="Resposta", conteudo=resposta, erro=False)

@app.route('/abrir-chamado', methods=['POST'])
def abrir_chamado():
    nome = request.form['nome']
    departamento = request.form['departamento']
    categoria = request.form['categoria']
    descricao = request.form['descricao']

    if not nome.strip() or not departamento.strip() or not categoria.strip() or not descricao.strip():
        return render_template('resultado.html', titulo="Ops!",
                               conteudo="Por favor, preencha todos os campos para abrir um chamado.", erro=True)
    protocolo = chatbot.abrir_chamado(nome, departamento, categoria, descricao)
    conteudo = (
        f"Chamado aberto com sucesso!<br>"
        f"Protocolo: {protocolo}<br>"
        f"Nome: {nome}<br>"
        f"Departamento: {departamento}<br>"
        f"Categoria: {categoria}<br>"
        f"Descrição: {descricao}"
    )
    return render_template('resultado.html', titulo="Chamado Aberto", conteudo=conteudo, erro=False)

@app.route('/consultar-chamado', methods=['POST'])
def consultar_chamado():
    protocolo = request.form['protocolo']
    if not protocolo.strip():
        return render_template('resultado.html', titulo="Ops!",
                               conteudo="Por favor, informe o protocolo para consultar o chamado.", erro=True)
    chamado = chatbot.consultar_chamado(protocolo)

    if isinstance(chamado, dict):
        conteudo = (
            f"<strong>Protocolo:</strong> {protocolo}<br>"
            f"<strong>Nome:</strong> {chamado['nome']}<br>"
            f"<strong>Departamento:</strong> {chamado['departamento']}<br>"
            f"<strong>Categoria:</strong> {chamado['categoria']}<br>"
            f"<strong>Descrição:</strong> {chamado['descricao']}<br>"
            f"<strong>Status:</strong> {chamado['status']}<br>"
            f"<strong>Data de Abertura:</strong> {chamado['data_abertura']}"
        )
        return render_template(
            'resultado.html',
            titulo="Chamado Encontrado",
            conteudo=conteudo,
            erro=False
        )
    else:
        return render_template(
            'resultado.html',
            titulo="Não Encontrado",
            conteudo=chamado,
            erro=True
        )
    
if __name__ == '__main__':
    app.run(debug=True)