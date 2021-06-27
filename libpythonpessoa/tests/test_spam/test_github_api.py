from unittest.mock import Mock

import pytest

from libpythonpessoa import github_api

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/63809250?v=4'
    resp_mock.json.return_value = {
        'login': 'Lins', 'id': 673297,
        'node_id': 'MDQ6VXNlcjY3MzI5Nw==',
        'avatar_url': url,
    }
    get_original = github_api.request.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('pessoasnil')
    assert avatar_url == url






def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('pessoasnil')
    assert 'https://avatars.githubusercontent.com/u/63809250?v=4' == url

