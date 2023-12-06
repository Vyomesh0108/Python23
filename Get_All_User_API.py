import requests

print("Get All User API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/users"

payload = {}
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

