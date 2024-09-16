import os
"""
利用二分找到了mid，那么mid-1也满足，这样可以找到一个最大值。
先枚举洛洛，再求另一个的最大值，然后相加求最大值。
假设洛洛通过了x关，晶晶通过了y关，我们可以先枚举x，
并利用二分法来找到洛洛剩下的能源水晶能够让晶晶通过的最多关数y，即求y的最大值。
然后在所有情况下求出x+y的最大值。
可以利用前缀和快速求出能通过的所有关卡O(1)。
O(nlogn)
"""

import sys
from bisect import *
input = sys.stdin.readline


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# 求前缀和
def pre_sum(li):
    l = len(li)
    pre = [0] * (l + 1)
    for i in range(1, l + 1):
        pre[i] = pre[i - 1] + li[i - 1]
    return pre


# 下标从1开始，0代表一个关卡都没有
a = pre_sum(a)
b = pre_sum(b)


ans = 0
# 枚举洛洛，0代表一个关卡都没有
for x in range(n + 1):
    # ax代表x之前的所有关卡的水晶（包括x），如果超过了，后面都不用计算
    if a[x] > k:
        break
    res = k - a[x]
    # 利用二分法
    # 例如：b：1 2 4，res：3 ==> bisect_right=4的下标，4不满足所有要减一
    # 例如：b：1 3 4，res：3 ==> bisect_right=3的下标+1，+1所有要减一
    y = bisect_right(b, res) - 1
    ans = max(ans, x + y)

print(ans)