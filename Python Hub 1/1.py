import requests

response = requests.get('https://www.google.kz/?hl=ru')

print(f'response.status_codes {response.status_code}')
print(f'response.headers {response.headers}')
print(f'response.content {response.content}')
print(f'response.text {response.text}')
