import requests


def test_Dogs_all():
    url = "https://dog.ceo/api/breeds/list/all"


    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_Dogs_all_error():
    url = "https://dog.ceo/api/breeds/list/al"


    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)


def test_Dogs_all_404():
    url = "https://dog.ceo/api/breeds/list/al"


    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 404

    print(response.text)


