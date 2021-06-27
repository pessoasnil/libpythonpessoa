from libpythonpessoa.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Lins', email='pessoasnil@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios(sessao):
    usuarios =[
        Usuario(nome='Lins',email='pessoasnil@gmail.com'),
        Usuario(nome='Pessoa',email='pessoa@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



