n, m, q = map(int, input().split())
a = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  a[i] = [0] + list(map(int, input().split()))

# 求差分数组
diff_a = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
  for j in range(1, m + 1):
    diff_a[i][j] = a[i][j] - a[i - 1][j] - a[i][j - 1] + a[i - 1][j - 1]

for _ in range(q):
  x1, y1, x2, y2, c = map(int, input().split())

  # 差分数组，(x1,y1)处+c，相当于原数组从(x1,y1)到右下角全部+c
  diff_a[x1][y1] += c
  diff_a[x2 + 1][y2 + 1] += c
  diff_a[x1][y2 + 1] -= c
  diff_a[x2 + 1][y1] -= c

# 还原原数组
for i in range(1, n + 1):
  for j in range(1, m + 1):
    a[i][j] = a[i][j - 1] + a[i - 1][j] - a[i - 1][j - 1] + diff_a[i][j]

for i in range(1, n + 1):
  print(' '.join(map(str, a[i][1:])))