class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        result = 0
        for i in range(len(nums)-2):
            left = i+1
            right = left+1
            while True:
                try:
                    while nums[i] + nums[left] > nums[right] and right <= len(nums):
                        right+=1
                    print(left, right)
                    result += right-left
                    left += 1
                except:
                    continue
        return result
p = Solution()
print(p.triangleNumber([4,2,3,4]))

