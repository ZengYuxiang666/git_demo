s = input()
def func(s):
    n = len(s)
    char_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                   'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                   'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    dp = [0]*(n+1) #dp[i]为序列长为i时的最大价值
    for x in range(1,n+1):
        dp[x] = char_values[s[x-1]]
    for i in range(1,n+1):
        for j in range(1,i):
            if i-j >= 2:
                dp[i] = max(dp[i],dp[j]+char_values[s[i-1]])
    return max(dp)
print(func(s))




