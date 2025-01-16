# http запросы бывают следующих типов

# 1. GET запрос - для получения данных
# 2. POST запрос - для публикации данных
# 3. PUT запрос - для редактирования данных
# 4. DELETE запрос - для удаления данных

import requests
import json

    # url = "https://jsonplaceholder.typicode.com/"

    # res = requests.get(url + "posts")
    # data = res.json()

# JSON - Java Script Object Notation - строка, которая 
# передается между сервером и клиентом
# в этой строке может быть список или словать, который был 
# получен путем запроса инфрормации из БД

# для того чтобы вывести инфромацию с запроса в 
# отфроматированном виде необходимо сделать следующее

    # print(json.dumps(data, indent=4))

# прежде чем делать вывод инфромации, необходимо
# проверить что запрос был выполнен успешно

url = "https://jsonplaceholder.typicode.com/"
res = requests.get(url + "posts/" + "3")
data = res.json()

if res.ok:
    data = res.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Ошибка {res.status_code}")