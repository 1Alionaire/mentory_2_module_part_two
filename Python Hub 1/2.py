import requests

params = {"q": "funny cats"}

response = requests.get('https://www.google.kz/search', params=params)

# print(f'response.status_codes {response.status_code}')
# print(f'response.headers {response.headers}')
# print(f'response.content {response.content}')
print(f'response.text {response.text}')
