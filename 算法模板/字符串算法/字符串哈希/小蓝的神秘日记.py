s = input()
n = len(s)

B = 26
MOD = (1 << 64) - 1
# 求s的前缀哈希
Hash = [0] * (n + 1)
Hash_q = [0] * (n + 1)
Hash_q[0] = 1
for i in range(1, n + 1):
  Hash[i] = Hash[i - 1] * B + ord(s[i - 1])
  Hash[i] %= MOD
  Hash_q[i] = Hash_q[i - 1] * B % MOD

def check(mid):
  # 存储指定哈希值的起始索引
  Hash_list = {}
  # 查看长度为mid的子串是否在s中出现两次
  for i in range(1, n + 1):
    if i + mid - 1 > n:
      return False
    j = i + mid - 1
    # 区间[i, j]的哈希值
    Hash_val = (Hash[j] - Hash[i - 1] * Hash_q[mid] % MOD + MOD) % MOD
    # 查询是否出现过
    if Hash_val in Hash_list:
      # 是否重叠
      if Hash_list[Hash_val] + mid - 1 < i:
        return True
    else:
      Hash_list[Hash_val] = i
  return False

# 二分查找最长的两个子串
l, r = 1, n
ans = 0
while l <= r:
  mid = (l + r) // 2
  if check(mid):
    l = mid + 1
    ans = mid
  else:
    r = mid - 1
print(ans)