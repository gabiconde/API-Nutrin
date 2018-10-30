from Nutrin.Consulta.Services.TipoEstado.readTipoEstado import readEstadoById
from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readAtendimentoById
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoById
from Nutrin.Paciente.Services.pesquisarPaciente import pesquisarPacienteById

def readConsulta(f=False):
    from Nutrin.Consulta.Model.Consulta import Consulta
    consultas = Consulta.query.all()
    if consultas != None:
        if f:
            return True, consultas
        consulas_dic = []
        for c in consultas:
            tipoEstado = readEstadoById(c.tipoEstado_id)
            tipoAtendimento = readAtendimentoById(c.tipoAtendimento_id)
            horario = readOcupadoById(c.horario_id)
            paciente = pesquisarPacienteById(c.paciente_id)
       
            consulas_dic.append({
                'id': c.id,
                'paciente_id': paciente,
                'tipoAtendimento_id': tipoAtendimento.nome,
                'horario_id': horario,
                'tipoEstado_id':tipoEstado.nome,
                'antropometria_id': c.antropometria_id,
                'dieta': c.dieta,
                'pagamento': c.pagamento
            })
        return True, consulas_dic
    return False, 'Nenhuma Consulta cadastrada'


def readConsultaId(id_consulta,f=False):
    from Nutrin.Consulta.Model.Consulta import Consulta
    #consultas = Consulta.query().filter(id==id_consulta)
    consultas = Consulta.query.get(id_consulta)
    print(consultas)
    if consultas != None:
        if f:
            return True, consultas
        consultas_dic = []
        for c in consultas:
            consultas_dic.append({
                'id': c.id,
                'paciente_id': c.paciente_id.nome,
                'tipoAtendimento_id': c.tipoAtendimento_id.nome,
                'horario_id': c.horario_id,
                'tipoEstado_id': c.tipoEstado_id.nome,
                'antropometria_id': c.antropometria_id,
                'dieta': c.dieta,
                'pagamento': c.pagamento
            })
        return True, consultas_dic
    return False, 'Nenhuma consulta com este id'

