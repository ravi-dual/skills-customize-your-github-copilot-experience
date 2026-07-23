import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(API_URL)

print(response.status_code)
print(response.text)
