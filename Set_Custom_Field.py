import requests
import json

print("Set Custom Field API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/custom-fields/65666467348b90225e131e01"

payload = json.dumps({
  "allowedValues": [],
  "description": "string",
  "name": "Custom2",
  "onlyAdminCanEdit": False,
  "placeholder": "Enter Custom1",
  "required": False,
  "status": "INACTIVE",
  "type": "TXT",
  "workspaceDefaultValue": "Type string custom field example value"
})
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
