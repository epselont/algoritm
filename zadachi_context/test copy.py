class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def solution(node):
    while node:
        print(node.value)
        node = node.next
    print("None")


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
