import requests

url = "http://macmini:8180/auth/realms/test/protocol/openid-connect/token"

payload='client_secret=5b5b6b2f-313f-4663-9409-15f497451cf1&username=user&password=user&grant_type=password&client_id=test'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
