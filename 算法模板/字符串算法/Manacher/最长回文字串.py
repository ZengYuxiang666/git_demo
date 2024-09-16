s = input()
# 预处理 '#'
s = '#' + '#'.join(list(s)) + '#'
n = len(s)
# dp[i]：以i为中心的可扩展的长度(单向)
dp = [0] * (n + 1)
# 维护最右回文子串
center, right = 0, 0
# 对于字符串s，从l、r向两端拓展
def expand(s, l, r):
  while l >= 0 and r < n and s[l] == s[r]:
    l -= 1
    r += 1
  return (r - l - 2) // 2

# 枚举每个点作为中心
for i in range(1, n - 1):
  if i > right:
    dp[i] = expand(s, i, i)
  else:
    i_sym = 2 * center - i
    min_len = min(dp[i_sym], right - i)
    dp[i] = expand(s, i - min_len, i + min_len)
  # 更新最右回文子串
  if i + dp[i] > right:
    center, right = i, i + dp[i]

print(max(dp))