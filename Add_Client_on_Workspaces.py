import requests
import json

print("Add Client on Workspaces API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/clients"

payload = json.dumps({
  "address": "string",
  "email": "vyommistry19@gmail.com",
  "name": "Kiran",
  "note": "string"
})
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
