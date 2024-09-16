from collections import deque
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
def print_f(path):
    curnode = path[-1]
    realpath = []
    while curnode[2] == -1:
        realpath.append(curnode[0:2])
        curnode = path[curnode[2]]
    realpath.append(curnode[0:2])
    realpath.reverse()
    for node in realpath:
        print(node)

def maze_math_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while len(queue) > 0:
        curnode = queue.pop()
        path.append(curnode)
        if curnode[0] == x2 and curnode[1] == y2 :
            print_f(path)
            return True
        for dir in dirs:
            nextnode = dir(curnode[0],curnode[1])
            if maze[nextnode[0]][nextnode[1]] == 0:
                queue.append((nextnode[0],nextnode[1],len(path)-1))
                maze[nextnode[0]][nextnode[1]] = 2
    else:
        print("没有路")
        return False

maze_math_queue(1,1,7,7)

