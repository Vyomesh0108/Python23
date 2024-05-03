import requests
import json

def test_get_all_books():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

    print(response.text)

def test_get_all_books_404():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Book"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 404

    print(response.text)

def test_post_books():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books"

    payload = json.dumps({
      "id": 200,
      "title": "New Book 202",
      "description": "Book 202",
      "pageCount": 900,
      "excerpt": "Posted New Book 202",
      "publishDate": "2023-12-13T17:27:58.467Z"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200

    print(response.text)

def test_post_books_404():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books2"

    payload = json.dumps({
      "id": 203,
      "title": "New Book 202",
      "description": "Book 202",
      "pageCount": 900,
      "excerpt": "Posted New Book 202",
      "publishDate": "2023-12-13T17:27:58.467Z"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 404

    print(response.text)

def test_get_book_by_Id():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/199"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    response1 = requests.get(url)
    response_body = response1.json()

    assert response_body['id'] == 199
    assert response.status_code == 200

    print(response.text)

def test_get_book_by_Id_title():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/199"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    response1 = requests.get(url)
    response_body = response1.json()

    assert response_body['title'] == 'Book 199'
    assert response.status_code == 200

    print(response.text)

def test_put_book_by_id_pagecount():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/198"

    payload = json.dumps({
      "id": 198,
      "title": "string",
      "description": "string",
      "pageCount": 19800,
      "excerpt": "string",
      "publishDate": "2023-12-13T17:39:07.560Z"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    response1 = requests.get(url)
    response_body = response1.json()

    assert response_body['pageCount'] == 19800

    assert response.status_code == 200

    print(response.text)


def test_put_book_by_id_Error():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/205"

    payload = json.dumps({
      "id": 205,
      "title": "string",
      "description": "string",
      "pageCount": 25000,
      "excerpt": "string",
      "publishDate": "2023-12-13T17:39:07.560Z"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    response1 = requests.get(url)
    response_body = response1.json()

    assert response_body["pageCount"] == 25000

    assert response.status_code == 404

    print(response.text)

def test_del_books_by_id():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/198"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    response1 = requests.get(url)
    response_body = response1.json()

    assert response_body['id'] == 198

    assert response.status_code == 200

    print(response.text)

def test_del_books_by_title():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/198"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    response1 = requests.get(url)
    response_body = response1.json()

    assert response_body['title'] == 'Book 198'

    assert response.status_code == 200

    print(response.text)
