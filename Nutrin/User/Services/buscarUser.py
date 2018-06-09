def buscarUser(username, f = False):
    from Nutrin.User.Services.listarUser import listarUser
    users = listarUser(True)
    for u in users:
        if username == u.username:
            if f:
                return u
            else:
                user = {
                    'username': u.username,
                    'password' : u.password,
                    'nome': u.nome,
                    'email': u.email,
                    'celular': u.celular,
                    'tipo': u.tipo
                }
                return user
    return False