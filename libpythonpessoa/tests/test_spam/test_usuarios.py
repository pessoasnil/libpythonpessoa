def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Lins')
    sessao.salvar(usuario)
    assert isinstance.(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Lins'),Usuario(nome='Pessoa')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuario == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()






