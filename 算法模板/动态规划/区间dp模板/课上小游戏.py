# 在合并区间时，一般会有消耗（根据题意去计算），状态转移方程就可以表示成：
# dp[i][j] = min(dp[i][j], dp[i,k] + dp[k+1][j] + 合并区间的消耗 ) （k是区间分割点）
# 请在此输入您的代码
n = int(input())
a = list(map(int, input().split()))

# 环形区间dp ——> 普通区间dp
a = [0] + a * 2

# dp[i][j]：区间[i, j]合并成一个值的最大分数
dp = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]

# res[i][j]：区间[i, j]合并得到的结果
res = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
for i in range(2 * n + 1):
  res[i][i] = a[i]


for length in range(2, n + 1):
  for i in range(1, 2 * n - length + 2):
    j = i + length - 1
    for k in range(i, j):
      res[i][j] = (res[i][j - 1] * a[j]) % 10
      dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + res[i][k] * res[k + 1][j] // 10)

ans = 0
for i in range(1, n + 1):
  ans = max(ans, dp[i][i + n - 1])

print(ans)