# Name: "Vyomesh Mistry"
# Student Number: "8870525"

import requests
import json

print("Create Webhooks API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/webhooks"

payload = json.dumps({
  "name": "Webhooks0",
  "triggerSource": [],
  "triggerSourceType": "PROJECT_ID",
  "url": "https://docs.clockify.me/#tag/Approval/operation/create_10",
  "webhookEvent": "NEW_TIMER_STARTED"
})
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
