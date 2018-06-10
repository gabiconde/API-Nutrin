def pesquisarPaciente(username):
    from Nutrin.Paciente.Model.Paciente import Paciente
    session.query(Paciente).filter_by(user.username=username).first() 