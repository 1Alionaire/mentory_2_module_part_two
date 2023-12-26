import requests

url = 'https://jsonplaceholder.typicode.com/posts'
rsp = requests.get(url=url)

if rsp.status_code == 200:
    print('Get')
    print(rsp.json())
else:
    print('Error')

data = {
    'userId': 1,
    'id': 1,
    'title': 'New Title',
    'body': 'New Body'
}

rsp_2 = requests.put(url=f'{url}/1', json=data)


if rsp_2.status_code == 200:
    update_post = rsp_2.json()
    print('Put')
    print(f'Обновленный такой: {update_post}')
else:
    print('Error')
