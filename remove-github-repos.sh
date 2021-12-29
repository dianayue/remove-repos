# 将 DELETE_KOKEN 和 GithubName 替换为将要删除的仓库的对应信息
DELETE_KOKEN="33ede4e961e574dfdb204ece0ef20309756cbc9e"
GithubName="itzhangbao"

for repoName in $(cat repos.txt)
do
    echo "Delete "$repoName
    curl -XDELETE -H "Authorization: token ${DELETE_KOKEN}" https://api.github.com/repos/${GithubName}/${repoName}
done