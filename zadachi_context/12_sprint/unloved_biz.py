def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(head, index) -> None:
    if index == 0:
        head = head.next_item
        return head
    previous_node = get_node_by_index(head, index-1)
    next_node = get_node_by_index(head, index+1)
    previous_node.next_item = next_node
    return head
