# Name: "Vyomesh Mistry"
# Student Number: "8870525"

import requests
import json

print("Add Workspaces API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces"

payload = json.dumps({
  "name": "workspace2"
})
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
