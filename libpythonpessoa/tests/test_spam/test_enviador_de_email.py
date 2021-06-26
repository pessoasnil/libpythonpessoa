import pytest

from libpythonpessoa.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario ',
    ['foo@bar.com.br', 'pessoasnil@gmail.com', ]
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'snil.pessoa@hotmail.com',
        'Cursos de python',
        'Turma henrique bastos'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'pessoasnil', ]
)
def test_remetente_ivalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'snil.pessoa@hotmail.com',
            'Cursos de python',
            'Turma henrique bastos'
        )

