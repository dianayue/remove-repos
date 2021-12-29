from time import sleep
import requests

organization = 'kjhy'
token = 'xxx'
api = 'https://api.github.com/repos/{}/{}'

with open('./repos.txt', 'r', encoding='utf-8') as f:
    repos = f.readlines()

urls = []
# 带组织名：
# ./repos.txt
# 用户名/仓库名
# username/repo1
# for line in repos:
#     name, repo = line.strip().split('/')
#     urls.append(api.format(name, repo))

# 不带组织名：
# ./repos.txt
# 仓库名
# repo1
for repo in repos:
    urls.append(api.format(organization, repo))

headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token ' + token,
    'X-OAuth-Scopes': 'repo'
}
for url in urls:
    requests.delete(url=url, headers=headers)
    sleep(2)
