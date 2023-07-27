import requests

endpoint = "http://127.0.0.1:8000/api/posts/"

response = requests.post(endpoint, json={"title":"Post Using API", "body":"COOOL"})

print(response.text)