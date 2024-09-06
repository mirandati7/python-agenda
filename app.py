from flask import Flask, redirect, render_template, request, url_for

from cadastro_agenda import consultar, inserir
from conexao import conecta_db

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nome  = request.form['nome']
        email = request.form["email"]
        telefone = request.form["telefone"]
        data_nascimento = request.form["data_nascimento"]
        print("Data Nascimento ", data_nascimento)

        conexao = conecta_db()
        validar =  inserir(conexao,nome,email,telefone,data_nascimento)

        if validar == True:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('falha'))

    return render_template('contato.html')    

@app.route("/success")
def success():
    return "Salvo com Sucesso"

@app.route("/falha")
def falha():
    return "Erro ao Salvar"

if __name__ == "__main__":
    app.run(debug=True)







