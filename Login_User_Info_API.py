import requests

print("Login User Info API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/user"

payload = {}
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
