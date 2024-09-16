from functools import lru_cache
import sys
sys.setrecursionlimit(10000000)
l, r = input().split()

@lru_cache(maxsize=None)
def dfs(i, limit, p1, p2, p3, p4, cnt):
    global tmp
    if (p2 == 1 and p1 == 4) or (p4 == 2 and p3 == 0 and p2 == 2 and p1 == 3):
        cnt = 1
    if i == len(tmp):
        return cnt

    ans = 0
    up = int(tmp[i]) if limit else 9
    for d in range(up+1):
        ans += dfs(i+1, limit and d == up, d, p1, p2, p3, cnt)
    return ans

tmp = r
ans_r = dfs(0, True, -1,-1,-1,-1, 0)
dfs.cache_clear()
tmp = str(int(l)-1)
ans_l = dfs(0, True, -1,-1,-1,-1, 0)
print(ans_r - ans_l)