s = input()
n = len(s)
s = '0' + s  # 添加一个前缀'0'以简化边界条件

# dp[i][j]：涂色[i, j]为目标颜色的最少次数
dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1  # 单个字符需要1次涂色

for length in range(2, n + 1):
    for i in range(1, n + 2 - length):
        j = i + length - 1
        if s[i] == s[j]:
            # 如果首尾字符相同，那么不需要额外的涂色（继承子问题的解）
            dp[i][j] = dp[i][j - 1]
        else:
            # 否则，在[i, j)范围内寻找一个分割点k
            for k in range(i, j):
                # 分割成[i, k]和[k+1, j]，并取涂色次数的最小值
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

print(dp[1][n])  # 输出涂色整个字符串s的最少次数