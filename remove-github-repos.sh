# 将 ORG 和 TOKEN 替换待删除仓库的组织名和 Token
ORG="kjhy"
TOKEN="xxx"

for repo in $(cat repos.txt)
do
    echo "Delete "$repo
    curl -XDELETE -H "Authorization: token ${TOKEN}" https://api.github.com/repos/${ORG}/${repo}
done