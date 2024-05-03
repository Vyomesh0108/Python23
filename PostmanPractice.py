import requests

# Assertion on JSON and Response Code both.
def test_zippop():
    url = "http://api.zippopotam.us/IN/110001"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    response1 = requests.get(url)

    response_body = response1.json()

    assert response_body["country"] == "India"
    assert response_body["post code"] == "110001"

    assert response.status_code == 200

    print(response.text)

def test_weather():

    url = "https://api.openweathermap.org/data/2.5/weather?q=Waterloo&appid=cf5d6ad2bbd5c67f574478e8644403aa"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response1 = requests.get(url)

    response_body = response1.json()

    assert response_body["dt"] == 1702484485
    assert response_body["visibility"] == 10000

    assert response.status_code == 200

    print(response.text)
