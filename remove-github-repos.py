import requests
from time import sleep

orgName = 'kjhy' # 组织名
token = 'xxx'
apiUrl = 'https://api.github.com/repos/{}/{}'

with open('./repos.txt', 'r', encoding='utf-8') as f:
    repos = f.readlines()

urls = []
# 带组织名：
# ./repos.txt
# 用户名/仓库名
# username/repo1
# for line in repos:
#     name, repo = line.strip().split('/')
#     urls.append(apiUrl.format(name, repo))

# 不带组织名：
# ./repos.txt
# 仓库名
# repo1
# for repo in repos:
#     urls.append(apiUrl.format(orgName, repo.strip()))

headers = {
    # 'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token ' + token,
    # 'X-OAuth-Scopes': 'repo'
}
for line in repos:
    repo = line.strip()
    url = apiUrl.format(orgName, repo)
    print('删除仓库：{}/{}'.format(orgName, repo))
    r = requests.delete(url=url, headers=headers)
    # print('删除结果：{}'.format(r.json()))
    print('删除结果：{}'.format(r.status_code))
    sleep(2)
