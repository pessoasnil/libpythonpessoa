from libpythonpessoa.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Lins')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Lins'), Usuario(nome='Pessoa')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
