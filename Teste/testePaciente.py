import requests as Req

Url = "http://127.0.0.1:5000/paciente/cadastrar"
user = {"username":'ozob', "password":"0123456",'nome':'Emerson','email':'ozob@gmail.com','celular':'11955554662','dataNascimento':'01-08-1998','sexo':"M",'cidade':'são paulo','profissao':'programador','objetivo':'emagrecer'}
Dados = Req.api.post(Url, json=user).json()
print(Dados)


Url = "http://127.0.0.1:5000/pacientes"
Dados = Req.api.get(Url).json()
print(Dados)