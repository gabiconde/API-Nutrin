def pesquisarPaciente(username, f=False):
    from Nutrin.User.Model.User import User
    from Nutrin import db
    user = db.session.query(User).filter_by(username = username).first()
    if user:
        user_id = user.id
        from Nutrin.Paciente.Model.Paciente import Paciente
        p = user = db.session.query(Paciente).filter_by(user_id = user_id).first()
        if p:
            if f :
                return True, p
            else:
                paciente_dic = {
                'username': p.user.username,
                'password' : p.user.password,
                'nome': p.user.nome,
                'email': p.user.email,
                'celular': p.user.celular,
                'tipo': p.user.tipo,
                'dataNascimento': p.dataNascimento,
                'sexo': p.sexo,
                'cidade': p.cidade,
                'profissao': p.profissao,
                'objetivo': p.objetivo
                }
                return True, paciente_dic
        return False, "usuario não é um paciente"
    return False, "Usuario não encontrado"