from Nutrin.Paciente.Model.Paciente import Paciente
from Nutrin import db

def cadastrarPaciente(username, password, nome, email, celular, dataNascimento, sexo, cidade, profissao, objetivo):
    from Nutrin.User.Services.validar import validar_email, validar_username
    if not validar_email(email):
        return False, "Email já cadastrado"
    elif not validar_username(username):
        return False, 'Username já cadastrado'
    p = Paciente(username,password, nome, email, celular, dataNascimento, sexo, cidade, profissao, objetivo)
    db.session.add(p)
    db.session.commit()
    return True, 'Paciente cadastrado com sucesso'