import requests, json

url = "https://jsonplaceholder.typicode.com/"

params = {
    "_limit": 10
}

res = requests.get(url + "posts/", params=params)

if res.ok:
    data = json.dumps(res.json(), indent=4)
    print(data)
else:
    print("Error: ", res.status_code)