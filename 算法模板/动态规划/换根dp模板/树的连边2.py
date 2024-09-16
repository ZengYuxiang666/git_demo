from collections import defaultdict
n = int(input())
edg = defaultdict(list)
# 构建双向邻接表
for _ in range(n-1):
  u,v = map(int,input().split())
  edg[u].append(v)
  edg[v].append(u)

# 初始化dp列表
down1 = [0]*(n+1)  # i节点向下的最长深度
down2 = [0]*(n+1)  # i节点向下的次长深度
p1 = [0]*(n+1)  # i节点向下最长深度的子节点
p2 = [0]*(n+1)  # i节点向下次长深度的子节点
up = [0]*(n+1)  # i节点向上的最长深度

def dfs1(u,fa):  # 第一遍搜索，搜索u节点向下的最长深度和次长深度并储存,从下往上搜索
  for v in edg[u]:  # 遍历u的每个子节点
    if v == fa:  # 如果为父节点，跳过，避免重复搜索
      continue
    dfs1(v,u)
    t = down1[v]+1  # 更新dp列表
    if t > down1[u]:
      down2[u] = down1[u]
      p2[u] = p1[u]
      down1[u] = t
      p1[u] = v
    elif t > down2[u]:
      down2[u] = t
      p2[u] = v
dfs1(1,0)  # 第一遍搜索，因为是双向表，任意节点都可作为根节点，从上往下搜索

def dfs2(u,fa):  # 更新该节点向上的最长深度
  for v in edg[u]:
    if v == fa:  # 避免重复搜索
      continue
    if v != p1[u]:  # 如果该子节点不是父节点向下最长深度的子节点，该字节的向上最长深度应为该父节点向下最长深度+1
      up[v] = max(up[v],down1[u]) + 1
    else:  # 如果该子节点为父节点向下最长深度的子节点，该字节的向上最长深度应为该父节点次最长深度+1
      up[v] = max(up[v],down2[u]) + 1
dfs2(1,0)

res = 0  # 最长深度
for x in range(1,n+1):  # 遍历每个节点
  res = max(res,down1[x]+down2[x],down1[x]+up[x])  # 最长深度为 该节点向下最长+向下次长 或 该节点向下最长+向上最长
print(res)