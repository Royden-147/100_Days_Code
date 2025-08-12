class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = second = dummy

    for _ in range(n + 1):
        first = first.next
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy.next