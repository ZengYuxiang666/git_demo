from collections import defaultdict
edg = defaultdict(list)  # edg[i][0]表示第i节点的左儿子，edg[i][1]表示右儿子
n = int(input())
values = [0]+list(map(int,input().split()))
for i in range(1,n+1):
  l,r = map(int,input().split())
  edg[i].append(l)
  edg[i].append(r)
res = []
def dfs(node,value):
  if value == 0:
    res.append(values[node])
  if edg[node] != []:
    if edg[node][0] != -1:
      dfs(edg[node][0],value+1)  # 找左儿子
    if edg[node][1] != -1:
      dfs(edg[node][1],value-1)  # 找右儿子
dfs(1,0)
print(sum(res))