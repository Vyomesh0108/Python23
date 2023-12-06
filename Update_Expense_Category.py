import requests
import json

print("Update Expense Category API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/expenses/categories/65654f9989c23218a2050571"

payload = json.dumps({
  "hasUnitPrice": True,
  "name": "new2",
  "priceInCents": 0,
  "unit": "string"
})
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
