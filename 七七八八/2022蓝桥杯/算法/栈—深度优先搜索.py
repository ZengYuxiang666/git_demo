maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1)
]
def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curnode = stack[-1]
        if curnode[0] == x2 and curnode[1] == y2:
            for x in stack:
                print(x)
            return True
        for dir in dirs:
            nextnode = dir(curnode[0], curnode[1])
            if maze[nextnode[0]][nextnode[1]] == 0:
                stack.append(nextnode)
                maze[nextnode[0]][nextnode[1]] = 2
                break
            else:
                maze[nextnode[0]][nextnode[1]] = 2
                stack.pop()
        else:
            print("没有路")
            return False
maze_path(1,1,7,1)
