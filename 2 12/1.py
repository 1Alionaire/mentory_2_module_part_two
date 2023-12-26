import requests

class Requester():
    # инициируем класс
    def __init__(self, url):
        self.url = url

    def get_request(self):
        result = None
        # Пытаемся дернуть инфу
        try:
            response = requests.get(url=self.url)
        #     Если не получилось, то вызываем ошибку
        except requests.RequestException as e:
            return f"Error: {e}"
        else:
            # Если получилось
            if response.status_code == 200:
                try:
                    # Пытаемся дернуть сначала JSON
                    result = response.json()
                except:
                    try:
                        # Потом пытаемся дернуть контент
                        result = response.content()#response.text
                    except:
                        try:
                            # На худой конец пытаемся дернуть текст
                            result = response.text#response.content()
                        except:
                            result = 'ошибка: '
            else:
                result = 'ошибка: '+ str(response.status_code)
        print(result)

need_url = str(input('Введите ваш URL'))
requester = Requester(need_url)
result = requester.get_request()
print(result)


