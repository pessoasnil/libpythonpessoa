import pytest

from libpythonpessoa.spam.enviador_de_email import Enviador
from libpythonpessoa.spam.main import EnviadorDeSpam
from libpythonpessoa.spam.modelos import Usuario


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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email('pessoasnil@gmail.com',
                                  'Curso de Python',
                                  'Confira os modulos fantasticos'
     )
    assert len(usuarios) == enviador.qtd_email_eviados





