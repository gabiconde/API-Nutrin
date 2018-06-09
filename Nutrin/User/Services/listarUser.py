from Nutrin.User.Model.User import User

def listarUser(f=False):
    users = User.query.all()
    if f == True:
        return users
    user_dic = []
    for u in users:
        user_dic.append({
            'username': u.username,
            'password' : u.password,
            'nome': u.nome,
            'email': u.email,
            'celular': u.celular,
            'tipo': u.tipo
        })
    return user_dic