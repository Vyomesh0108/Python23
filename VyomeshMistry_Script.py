import requests
import json

url = "https://fakerestapi.azurewebsites.net/api/v1/Books"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = "https://fakerestapi.azurewebsites.net/api/v1/Books"

payload = json.dumps({
  "id": 202,
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

print(response.text)

url = "https://fakerestapi.azurewebsites.net/api/v1/Books/199"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = "https://fakerestapi.azurewebsites.net/api/v1/Books/198"

payload = {}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

url = "https://fakerestapi.azurewebsites.net/api/v1/Books/198"

payload = json.dumps({
  "id": 198,
  "title": "string",
  "description": "string",
  "pageCount": 120,
  "excerpt": "string",
  "publishDate": "2023-12-13T17:39:07.560Z"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
