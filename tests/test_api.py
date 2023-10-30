import requests


def test_api():
    url = 'http://127.0.0.1:5000/'
    response = requests.get(url)
    assert response.status_code == 200
    assert 'Hello, my frend!' in response.text
