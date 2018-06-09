import requests as Req

Url = "http://127.0.0.1:5000/usuarios/cadastrar"
user = {"username":'emersonscarbonaro', "password":"0123456",'nome':'Emerson','email':'emersonscarbonaro@gmail.com','celular':'11955554662','tipo':'A'}
Dados = Req.api.post(Url, json=user).json()
print(Dados)

Url = "http://127.0.0.1:5000/usuarios/cadastrar"
user = {"username":'gabrielaConde', "password":"0123456",'nome':'Gabi','email':'gabi@gmail.com','celular':'11955554662','tipo':'A'}
Dados = Req.api.post(Url, json=user).json()
print(Dados)

Url = "http://127.0.0.1:5000/usuario/alterar-senha"
user = {"username":'emersoncarbono', "password":"0420"}
Dados = Req.api.put(Url, json=user).json()
print(Dados)

Url = "http://127.0.0.1:5000/usuario/alterar-user"
user = {"username_atual":"gabiconde","username":'gabi', "password":"0123456",'nome':'Gabi Conde','email':'gabi@gmail.com','celular':'11955554662','tipo':'A'}
Dados = Req.api.put(Url, json=user).json()
print(Dados)

Url = "http://127.0.0.1:5000/usuarios"
Dados = Req.api.get(Url).json()
print(Dados)
