class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.data, end=" ")

ll = LinkedList()
ll.insertNode(1)
ll.insertNode(2)
ll.insertNode(3)
ll.insertNode(4)
ll.print_reverse(ll.head)
