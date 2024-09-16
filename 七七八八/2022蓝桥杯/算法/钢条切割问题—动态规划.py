# p = [0,1,5,8,9,10,17,17,20,21,23,24,26,27,27,28,30,33,36,39,40]
p = [0,1,5,8,9,10,17,17,20,24,30]
def cut_rod_recurision(p,n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1,n):
            res = max(res,cut_rod_recurision(p,i)+cut_rod_recurision(p,n-i))
        return res

def cut_rod_recurision_2(p,n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1,n+1):
            res = max(res,p[i] + cut_rod_recurision_2(p,n-i))
        return res

def cut_rod_dp(p,n):
    r = [0]
    s = [0]
    for i in range(1,n+1):
        res_r = 0
        res_s = 0
        for j in range(1,i+1):
            if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n],s
def cut_rod_solution(p,n):
    r, s = cut_rod_dp(p,n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans
print(cut_rod_solution(p,7))