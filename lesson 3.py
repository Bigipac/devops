import requests

response = requests.get("https://api.github.com/users/Bigipac/repos")
if response.status_code == 200:
    print("Success")

repos = response.json()
# for repo in repos:
#     if "devops" in str(repo["name"]).lower():
#         print(repo["name"])
for repo in repos:
    print(repo["name"])
