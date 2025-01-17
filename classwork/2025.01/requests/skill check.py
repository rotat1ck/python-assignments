import requests, json

# 1
url = "https://jsonplaceholder.typicode.com/users"
res = requests.get(url)

print(json.dumps(res.json(), indent=4))

# 2
url = "https://jsonplaceholder.typicode.com/users/3"
res = requests.get(url)

data = res.json()
print(data["name"], data["email"])

# 3
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 2}
res = requests.get(url, params=params)

data = res.json()

print([f"Заголовок: {post["title"]}" for post in data])


# 4 
url = "https://jsonplaceholder.typicode.com/users"
params = {"id": 1}
res = requests.get(url, params=params)
data = res.json()
username = data[0]["name"]

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
res = requests.get(url, params=params)
data = res.json()
print(f"Имя пользователя: {username}")
print([post["title"] for post in data])

# 5
url = "https://jsonplaceholder.typicode.com/todos"
params = {"userId": 4, "completed": "true"}
res = requests.get(url, params=params)
print([post["title"] for post in res.json()])