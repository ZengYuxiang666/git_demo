n,q = map(int,input().split())
nums = [0] + list(map(int,input().split())) + [0]
D_nums = [0]*(n+2)
#构建差分数组 d[i] = a[i] - a[i-1]
for i in range(1,n+2):
  D_nums[i] = nums[i] - nums[i-1]
for _ in range(q):
  l,r,c = map(int,input().split())
  D_nums[l] += c
  D_nums[r+1] -= c
#复原原数组 a[i] = a[i-1] + d[i]
for i in range(1,n+1):
  nums[i] = nums[i-1] + D_nums[i]
  print(nums[i],end=' ')
