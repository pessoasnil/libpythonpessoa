from libpythonpessoa.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

def test_remetente():
    enviador= Enviador()
    resultado=enviador.enviar(
        'pessoasnil@gmail.com',
        'snil.pessoa@hotmail.com',
        'Cursos de python',
        'Turma henrique bastos'
 )
    assert 'pessoasnil@gmail.com' in resultado