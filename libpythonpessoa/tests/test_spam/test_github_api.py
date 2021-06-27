from unittest.mock import Mock

from libpythonpessoa import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value={'login': 'Lins', 'id': 673297,
                                 'node_id': 'MDQ6VXNlcjY3MzI5Nw==',
                                 'avatar_url': 'https://avatars.githubusercontent.com/u/673297?v=4',
    }

    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('Lins')
    assert 'https://avatars.githubusercontent.com/u/673297?v=4' == url
