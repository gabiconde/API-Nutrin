from Nutrin import db
from Nutrin.User.Services.listarUser import listarUser

def alterarSenha(dados):
    users = listarUser(True)
    for u in users:
        if u.username == dados['username']:
            u.password = dados['password']
            db.session.commit()
            return True
    return False
    
    
    
