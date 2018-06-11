import requests as Req

url_basica = 'http://127.0.0.1:5000'

def testeListarPaciente():
    url = url_basica + '/pacientes'
    dados = Req.api.get(url).json()
    return dados

def testeCadastrarPaciente():
    url = url_basica + '/paciente/cadastrar'
    paciente = {
        "username":'emersoncarbono',
         "password":"0123456",
         'nome':'Emerson',
         'email':'emerson@gmail.com',
         'celular':'11955554662',
         'dataNascimento':'01-08-1998',
         'sexo':"M",
         'cidade':'são paulo',
         'profissao':'programador',
         'objetivo':'emagrecer'
    }
    dados = Req.api.post(url, json=paciente).json()
    return dados


def main():
    print(testeListarPaciente())
    print(testeCadastrarPaciente())

main()
