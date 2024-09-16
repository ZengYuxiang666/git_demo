# 定长窗口滑动从第二步开始就只需要判断首尾元素,
# 看到求一段，应该想到滑动窗口，前缀和，差分
# 定长窗口注意边界条件，0下标初始化，从1下标开始遍历，到len(arr)-k+1结束，下标为i时窗口的最后一位元素是arr[i+k-1]
# https://leetcode.cn/problems/sliding-subarray-beauty/  值域小可以参考计数排序
#