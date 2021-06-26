from libpythonpessoa.spam.enviador_de_email import Enviador
from libpythonpessoa.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_email('pessoasnil@gmail.com',
                                  'Curso de Python',
                                  'Confira os modulos fantasticos'
 )
