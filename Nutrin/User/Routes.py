from flask import jsonify, request
from Nutrin import app
from Nutrin.Model.Response import response

@app.route("/usuarios", methods=["GET"])
def ListarUserRoute():
    from Nutrin.User.Services.listarUser import listarUser
    response["Status"] = "Sucesso"
    response["Dados"] = listarUser()
    response["Mensagem"] = "Usuarios listado com sucesso"
    return jsonify(response)

@app.route("/usuarios/cadastrar", methods=["POST"])
def CadastarUserRoute():
    from Nutrin.User.Services.cadastrarUser import cadastrarUser
    dados = request.get_json()
    username = dados["username"]
    password = dados["password"]
    nome = dados["nome"]
    email = dados["email"]
    celular = dados["celular"]
    tipo = dados["tipo"]
    status, mensagem = cadastrarUser(username, password, nome, email, celular, tipo)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
    

@app.route("/usuario/alterar-senha", methods=["PUT"])
def AlterarSenhaRoute():
    from Nutrin.User.Services.alterarSenha import alterarSenha
    dados = request.get_json()
    alterarSenha(dados)
    response["Status"] = "Sucesso"
    response["Dados"] = ""
    response["Mensagem"] = "Senha alterada com sucesso"
    return jsonify(response)

@app.route("/usuario/alterar-user", methods=['PUT'])
def AlterarUserRoute():
    from Nutrin.User.Services.alterarUser import alterarUser
    dados = request.get_json()
    username_atual = dados['username_atual']
    username = dados['username']
    nome = dados['nome']
    email = dados['email']
    celular = dados['celular']
    tipo = dados["tipo"]
    status, mensagem = alterarUser(username_atual, username, nome, email, celular, tipo)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)