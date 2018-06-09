from Nutrin import db
from Nutrin.User.Services.listarUser import listarUser

def alterarUser(username_atual, username, nome, email, celular, tipo):
    users = listarUser(True)
    for u in users:
        if u.username == username_atual:
            if u.username != username:
                from Nutrin.User.Services.validar import validar_username
                if not validar_username(username):
                    return False, "Username já cadastrado"
            if u.email != email:
                from Nutrin.User.Services.validar import validar_email
                if not validar_email(email):
                    return False, "Email já cadastrado"
            u.username = username
            u.nome = nome
            u.email = email
            u.celular = celular
            u.tipo = tipo
            db.session.commit()
            return True, "Usuario alterado com sucesso"
    return False, "Usuario não encontrado"