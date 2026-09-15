import sqlite3

def buscar_resposta(pergunta):
    encontrados = []
    conexao = sqlite3.connect('data/database.db')
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT categorias.nome, categorias.resposta, palavras_chave.palavra
        FROM palavras_chave
        JOIN categorias ON palavras_chave.categoria_id = categorias.id
    """)
    resultado = cursor.fetchall()
    conexao.close()

    for nome, resposta, palavra in resultado:
        if palavra.lower() in pergunta.lower():
            if nome not in encontrados:
                encontrados.append(nome)

    return encontrados


def obter_resposta(encontrados):
    if not encontrados:
        return "Desculpe, não encontrei uma resposta para a sua pergunta, por favor tente novamente ou entre em contato com o suporte."

    elif len(encontrados) == 1:
        conexao = sqlite3.connect('data/database.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT resposta FROM categorias WHERE nome = ?", (encontrados[0],))
        resultado = cursor.fetchone()
        conexao.close()
        return resultado[0]

    elif len(encontrados) > 1:
        respostas = []
        conexao = sqlite3.connect('data/database.db')
        cursor = conexao.cursor()
        for nome in encontrados:
            cursor.execute("SELECT resposta FROM categorias WHERE nome = ?", (nome,))
            resultado = cursor.fetchone()
            respostas.append(resultado[0])
        conexao.close()
        return "Encontrei múltiplas respostas:\n" + "\n".join(respostas)