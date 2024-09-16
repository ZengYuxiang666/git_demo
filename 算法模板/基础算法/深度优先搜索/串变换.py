# 读取输入
n = int(input())  # 读取字符串的长度n
s = [int(i) for i in input()]  # 读取初始字符串S,并转换为整数列表
t = [int(i) for i in input()]  # 读取目标字符串T,并转换为整数列表
k = int(input())  # 读取操作的数量k
cao = []  # 用于存储所有的操作
for i in range(k):
    cao.append(list(map(int, input().split())))  # 读取每一个操作,并存储到cao列表中

fin = False  # 用于标记是否找到了满足条件的操作序列
vis = [0] * k  # 用于标记每个操作是否被使用过

def dfs():
    global fin, s  # 声明全局变量fin和s,以便在函数内部修改
    if s == t:  # 如果当前字符串s已经等于目标字符串t
        fin = True  # 将fin标记为True,表示找到了满足条件的操作序列
        return  # 返回,结束当前分支的搜索
    if fin:  # 如果已经找到了满足条件的操作序列
        return  # 直接返回,不再继续搜索
    for i in range(k):  # 遍历所有的操作
        if vis[i] == 0:  # 如果当前操作还没有被使用过
            op, x, y = cao[i]  # 取出当前操作的类型和参数
            vis[i] = 1  # 将当前操作标记为已使用
            if op == 1:  # 如果当前操作是加法操作
                s[x] = (s[x] + y) % 10  # 将s[x]加上y,并对10取模
                dfs()  # 递归搜索下一层
                s[x] = (s[x] - y + 10) % 10  # 还原s[x]的值,确保回溯时状态正确
            else:  # 如果当前操作是交换操作
                s[x], s[y] = s[y], s[x]  # 交换s[x]和s[y]的值
                dfs()  # 递归搜索下一层
                s[x], s[y] = s[y], s[x]  # 还原s[x]和s[y]的值,确保回溯时状态正确
            vis[i] = 0  # 将当前操作标记为未使用,回溯到上一层

dfs()  # 从初始状态开始搜索
print('Yes' if fin else 'No')  # 如果找到了满足条件的操作序列,输出Yes,否则输出No

