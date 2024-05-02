from api import ProductApi


def test_with_pytest():
    client = ProductApi("https://66333084f7d50bbd9b487735.mockapi.io/api/v1/users")
    assert client.users('GET').json()[0]['name'] == 'Clemens_Crist'