import requests as Req

url_padrao = "http://127.0.0.1:5000"

def testeCadastrarUser():
    url = url_padrao + "/usuarios/cadastrar"
    user = {
        "username":'Mokey',
        "password":"789456123",
        'nome':'Monkey D. Luffy',
        'email':'luffy@gmail.com',
        'celular':'11955554662',
        'tipo':'A'
        }
    Dados = Req.api.post(url, json=user).json()
    return Dados

def testeAlterarSenha(username, senha):
    url = url_padrao + "/usuario/alterar-senha"
    user = {
        "username": username,
        "password": senha
        }
    Dados = Req.api.put(url, json=user).json()
    return Dados

def testeAlterarUser():
    url = url_padrao + "/usuario/alterar-user"
    user = {
        "username_atual":"luffy",
        "username":'luffy2',
        'nome':'Monkey D.',
        'email':'luffy2@gmail.com',
        'celular':'11955554662',
        'tipo':'A'
        }
    Dados = Req.api.put(url, json=user).json()
    return Dados

def testeListarUser():
    url = url_padrao + "/usuarios"
    Dados = Req.api.get(url).json()
    return Dados

def testeBuscarUser(username):
    url = url_padrao + "/usuario/" + username
    Dados = Req.api.get(url).json()
    return Dados

def main():
    print(testeBuscarUser('Mokey'))

main()