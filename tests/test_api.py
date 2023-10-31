import requests


def test_api():
    url = 'http://app:5000/'
    response = requests.get(url)
    assert response.status_code == 200
    assert 'Hello, my frend' in response.text
