class TreeNode:
    def __init__(self):
        self.nodes = {}
        self.cnt = 0    # 当前点添加的次数

    # 将字符串s添加到字典树中
    def insert(self, s, value):
        curr = self
        for c in s:
            # 若c边不在当前节点的下一节点，则新创建
            if c not in curr.nodes.keys():
                curr.nodes[c] = TreeNode()
            # 移动到当前节点的下一点
            curr = curr.nodes[c]
            curr.cnt += value

    # 查找字符串t的最长公共前缀的长度
    def common_prex(self, t):
        curr = self
        res = 0
        for c in t:
            curr = curr.nodes[c]
            # 若该点添加的次数为0（未添加或已被删除)
            if curr.cnt == 0:
                return res
            res += 1
        return res


# 请在此输入您的代码
N = int(input())
S = []
root = TreeNode()
for _ in range(N):
    S.append(input().strip())
    root.insert(S[-1], 1)

for s in S:
    # 删除自身
    root.insert(s, -1)
    print(root.common_prex(s))
    # 将自身添加回去
    root.insert(s, 1)