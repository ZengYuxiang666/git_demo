N, M = 32, 15
n, m = map(int, input().split())
# 最大状态 11...11: m个1
upper_limit = (1 << m) - 1

# 将输入的每一行转换为二进制数 0 1 0 1 —> （右为高位）10
rows = [0] * N
for i in range(n):
  l = list(map(int, input().split()))
  for idx, j in enumerate(l):
    if j:
      rows[i] |= 1 << idx

# 判断状态00..00 ~ 11..111是否合法
valid = [False] * (1 << M)
for i in range(upper_limit + 1):
  # 没有相邻的1
  if (i & (i >> 1)) == 0:
    valid[i] = True

# dp[i][j]：前i-1行已经选好，第i行的选宠状态为j的最大宠物数
dp = [[0] * (1 << M) for _ in range(N)]

def count_1(x):
  # 返回二进制x中1的个数
  cnt = 0
  while(x):
    if x & 1:
      cnt += 1
    x = x >> 1
  return cnt

# 枚举第i行
for i in range(n):
  # 枚举第i行的选宠状态
  for j in range(upper_limit + 1):
    # 判断该状态j是否可选：合法、与第i行原状态不重叠
    if valid[j] and (j & rows[i]) == 0:
      # 枚举上一行选宠状态
      for k in range(upper_limit + 1):
        # 判断合法、与第i行选宠状态不重叠
        if valid[k] and (k & j) == 0:
          dp[i][j] = max(dp[i][j], dp[i - 1][k] + count_1(j))

print(max(dp[n - 1]))