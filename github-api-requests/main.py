import requests

response = requests.get("https://api.github.com/users/ziadali001/repos")
user_data = response.json()

# print the whole objects list
print(user_data)
print(type(user_data))

# print just the names and urls
for repo in user_data:
    print(f"Repo Name: {repo['name']}\nRepo Url: {repo['html_url']}\n")



