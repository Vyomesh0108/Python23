import requests
import json

print("Update Clients API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/clients/65665cbff8bf2b116110a33e"

payload = json.dumps({
  "address": "string",
  "archived": True,
  "email": "karanpatel12@gmail.com",
  "name": "KaranPatel",
  "note": "string"
})
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
