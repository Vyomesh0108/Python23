import requests

print("Get All Invoices API Response", end="\n\n")
url = "https://api.clockify.me/api/v1/workspaces/654c010bc7d5882517f7e416/invoices"

payload = {}
headers = {
  'x-api-key': 'YjAwMzJjYjItMTg5ZS00M2Y1LWFlZDYtOGJjYzM3ZjYwZTU2'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
