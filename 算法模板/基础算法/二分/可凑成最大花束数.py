# 请在此输入您的代码
n,k =map(int,input().split(' '))
# 每一个元素代表一种颜色的花
ls = list(map(int,input().split(' ')))
def check(mid):
    # cnt表示能够打包的花朵数
    cnt=0
    for i in range(n):
        # 因为要取每一种颜色的花组成，所以只用考虑最少颜色的花，它有几朵就能捆几束
        cnt += min(mid, ls[i])
    # 如果能够打包的花朵数大于等于当前能打包的花朵数就返回TRUE
    return cnt >= mid * k

left ,right = 1,2*10**14
ans = 0
while left <= right:
    mid = (left+right)//2
    if check(mid):
        ans = mid
        left = mid+1
    else:
        right = mid -1
print(ans)