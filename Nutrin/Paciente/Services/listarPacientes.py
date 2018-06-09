from Nutrin.Paciente.Model.Paciente import Paciente

def listarPacientes(f=False):
    pacientes = Paciente.query.all()
    if f:
        return pacientes
    pacientes_dic = []
    for p in pacientes:
        pacientes_dic.append({
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
        })
    return pacientes_dic