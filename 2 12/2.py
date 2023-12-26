import requests

url = 'http://localhost:8000/kek'

while True:
    rsp = requests.get(url = url)
    if rsp.status_code == 200:
        print(rsp.text)
    else:
        print('Error')
