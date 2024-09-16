import os
import sys

# 请在此输入您的代码
n,m=map(int,input().split())
state=[]
for i in range(2**m):  # 记录每一行的合法状态，不存在连续的3个1
  cnt=0
  flag=1
  ok=i
  while i:
    if i&1!=0:  #最后一位是1
      cnt+=1
    else:
      cnt=0
    if cnt==3:
      flag=0
      break
    i>>=1
  if flag:
    state.append(ok)
# 需要3个状态，哪一行，当前状态，上一个状态
dp=[[[0 for i in range(2**m)]for i in range(2**m)] for i in range(n)]
for i in state:
  dp[0][i][0]=1

# 遍历求解
for i in range(1,n):
  for j in state:  # 当前状态
    for k in state: # 上一行状态
      for h in state:  # 在上一行状态
        if j&k&h==0:  #
          dp[i][j][k]+=dp[i-1][k][h]
ans=0
for i in state:  # 求和输出
  ans+=sum(dp[n-1][i])


print(ans)
