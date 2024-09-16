from collections import defaultdict
import sys
sys.setrecursionlimit(1000005)
n=int(input())
mp=defaultdict(list)
dp=[0]*(n+1)
for i in range(n-1):
    a,b=map(int,input().split())
    mp[a].append(b)
    mp[b].append(a)
maxn=0
def dfs(now,fa):
    global maxn
    for so in mp[now]:
        if so!=fa:
            dfs(so,now)
            if dp[now]+dp[so]+1>maxn:
                maxn=dp[so]+dp[now]+1
            dp[now]=max(dp[now],dp[so]+1)

dfs(1,0)
x=maxn
print(x)