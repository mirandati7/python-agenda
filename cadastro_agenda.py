from conexao import conecta_db


def consultar(conexao):
    contatos = []
    cursor = conexao.cursor()
    cursor.execute("select id,nome,email,data_nascimento from contato")
    registros = cursor.fetchall()
    print("|-----------------------------------|")
    for registro in registros:
        item = {
            "id": registro[0],
            "nome": registro[1],
            "email": registro[2]
        }
        contatos.append(item)
        print(item)
    return contatos

def inserir(conexao, nome,email,telefone, data_nascimento):
    cursor = conexao.cursor()
    sql_insert = "insert into contato (nome,email,telefone,data_nascimento) values (%s,%s,%s,%s)"
    dados   = (nome, email, telefone, data_nascimento)
    cursor.execute(sql_insert, dados)
    conexao.commit()
    return True