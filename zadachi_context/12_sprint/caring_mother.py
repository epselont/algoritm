def solution(head, index) -> None:
    node = head
    count = 0
    while node.value != index:
        node = node.next_item
        count += 1
        if node is None:
            return -1
            break
    return count
