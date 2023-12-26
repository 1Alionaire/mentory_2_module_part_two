import requests

url = 'http://127.0.0.1:5000/hello'

data = {'product1': 'banana', 'product2':'apple'}


rsp = requests.get(url=url)


if rsp.status_code == 200:
    print(rsp.json())
else:
    print('Error')

