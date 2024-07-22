from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/user/',
        json={
            'username': 'CometaTeste',
            'email': 'cometa@maria.com.br',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'CometaTeste',
        'email': 'cometa@maria.com.br',
        'id': 1,
    }
