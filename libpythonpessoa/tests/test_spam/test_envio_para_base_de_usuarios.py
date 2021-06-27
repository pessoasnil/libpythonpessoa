from unittest.mock import Mock

import pytest

from libpythonpessoa.spam.enviador_de_email import Enviador
from libpythonpessoa.spam.main import EnviadorDeSpam
from libpythonpessoa.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_eviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_eviados += 1



@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Lins',email='pessoasnil@gmail.com'),
            Usuario(nome='Pessoa',email='pessoa@gmail.com')
        ],
        [
            Usuario(nome='Lins',email='pessoasnil@gmail.com')
        ]
    ]
)

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email('pessoasnil@gmail.com',
                                  'Curso de Python',
                                  'Confira os modulos fantasticos'
     )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_spam(sessao):
    usuario= Usuario(nome='Lins', email='pessoasnil@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'pessoasnil@gmail.com',
        'Curso de Python',
        'Confira os modulos fantasticos'
     )
    enviador.enviar.assert_called_once_with (
        'pessoasnil@gmail.com',
        'pessoa@gmail.com',
        'Curso de Python'
        'Confira os modulos fantasticos'
    )














