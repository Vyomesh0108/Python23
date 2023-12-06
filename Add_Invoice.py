# Name: "Vyomesh Mistry"
# Student Number: "8870525"

import requests
import json

print("Add Invoice API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/invoices"

payload = json.dumps({
  "clientId": "65654c5b2a47c52a012f6207",
  "currency": "string",
  "dueDate": "2019-08-24T14:15:22Z",
  "issuedDate": "2019-08-24T14:15:22Z",
  "number": "string"
})
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
