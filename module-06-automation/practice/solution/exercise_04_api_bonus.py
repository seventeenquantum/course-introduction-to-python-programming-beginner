import requests

response = requests.get("https://api.github.com/users/octocat", timeout=10)
if response.status_code == 200:
    data = response.json()
    print(data["login"], data["public_repos"])
else:
    print("Request failed with status", response.status_code)
