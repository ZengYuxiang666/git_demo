from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)
t = int(input())
n = 0
s = ''
@lru_cache(maxsize=None)
def dfs(i, limit, is_num, cnt):
    if i == n:
        if cnt <= 3:
            return int(is_num)
        return 0

    if cnt > 3:
        return 0

    ans = 0
    if not is_num:
        ans = dfs(i + 1, False, False, 0)
    up = int(s[i]) if limit else 9

    for d in range(1 - int(is_num), up + 1):
        if d != 0:
            ans += dfs(i + 1, limit and d == up, True, cnt + 1)
        else:
            ans += dfs(i + 1, limit and d == up, True, cnt)
    return ans


for _ in range(t):
    l, r = map(int, input().split())
    s = str(r)
    n = len(s)
    rnum = dfs(0, True, False, 0)
    dfs.cache_clear()
    s = str(l - 1)
    n = len(s)
    lnum = dfs(0, True, False, 0)
    dfs.cache_clear()
    print(rnum - lnum)
