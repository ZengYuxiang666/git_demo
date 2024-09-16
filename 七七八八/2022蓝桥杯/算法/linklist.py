class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
def creat_link(list):
    head = Node(list[0])
    for x in list[1:]:
        node = Node(x)
        node.next = head
        head = node
    return head

link = creat_link([1,2,3,4,5])
print(link.item)

