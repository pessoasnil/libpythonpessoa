import pytest

from libpythonpessoa.spam.deb import Conexao
from libpythonpessoa.spam.modelos import Usuario

@pytest.fixture()
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear Down
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Lins')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Lins'), Usuario(nome='Pessoa')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
