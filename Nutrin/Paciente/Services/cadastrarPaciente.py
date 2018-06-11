from Nutrin.Paciente.Model.Paciente import Paciente
from Nutrin.User.Services.cadastrarUser import cadastrarUser
from Nutrin.User.Services.buscarUser import buscarUser
from Nutrin import db

def cadastrarPaciente(username, password, nome, email, celular, dataNascimento, sexo, cidade, profissao, objetivo):
    status, mensagem = cadastrarUser(username, password, nome, email, celular, "P")
    if status:
        user = buscarUser(username, True)
        id_user = user.id
        p = Paciente(id_user, dataNascimento, sexo, cidade, profissao, objetivo)
        db.session.add(p)
        db.session.commit()
        return True, 'Paciente cadastrado com sucesso'
    return status, mensagem