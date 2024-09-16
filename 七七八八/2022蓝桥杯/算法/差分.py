import os
import sys

# 输入测试用例的数量 n 和操作数量 q
n, q = map(int, input().split())

# 初始化一个长度为 n+2 的数组 nums，其中 nums[0] 和 nums[n+1] 都是 0，用于处理边界情况
nums = [0] * (n + 2)
# 读取初始的球数，并将它们存储在 nums 数组的相应位置中（跳过 nums[0]）
nums[1:n + 1] = list(map(int, input().split()))

# 初始化一个长度为 n+2 的差分数组 D_nums，所有元素初始化为 0
D_nums = [0] * (n + 2)

# 构建差分数组
# 注意：这里的循环从 1 开始到 n+1，因为 nums[0] 和 nums[n+1] 都是 0，不参与计算
for i in range(1, n + 1):
    # 差分数组的定义是 D_nums[i] = nums[i] - nums[i-1]
    D_nums[i] = nums[i] - nums[i - 1]

# 执行 q 次操作
for _ in range(q):
    # 读取每次操作的 l, r, c 值
    l, r, c = map(int, input().split())
    # 在差分数组的 l 位置加上 c
    D_nums[l] += c
    # 在差分数组的 r+1 位置减去 c，以确保区间 [l, r] 内增加了 c，其他位置不变
    D_nums[r + 1] -= c

# 使用差分数组更新 nums 数组以得到最终状态
# 注意：这里的循环从 1 开始到 n+1，因为我们要得到的是最终的 nums 数组
for i in range(1, n + 1):
    # 更新 nums 数组，nums[i] 现在是它之前所有差分数组元素的累加和
    nums[i] = nums[i - 1] + D_nums[i]
    # 打印当前框的球数，并在每个数字后添加一个空格
    print(nums[i], end=' ')

# 在所有操作完成后打印一个换行符，以分隔不同的测试用例（如果有的话）
print()