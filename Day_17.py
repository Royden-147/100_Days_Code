# Single Linked List
class NodeSL:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLL:
    def __init__(self):
        self.head = None

    def addNewNode(self,val):
        new_node = NodeSL(val)
        if self.head is None:
            self.head = new_node
            print(f"{val} added to the Linked List")
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            print(f"{val} added to the Linked List")

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            cur = self.head
            while cur:
                print(cur.data,end=" -> ")
                cur = cur.next
            print('None')


# Double Linked List
class NodeDL:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def addNode(self,val):
        new_node = NodeDL(val)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> " if cur.next else "")
            cur = cur.next
        print()

# Binary Search Tree
class NodeBT:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class BinaryST:
    def __init__(self):
        self.root = None

    def insertNode(self,node,val):
        n = NodeBT(val)
        if self.root is None:
            self.root = n
            print(f"{val} is the root Node")
            return
        if val < node.data:
            if node.left is None:
                node.left = n
                print(f"{val} is added on the left")
            else:
                self.insertNode(node.left,val)
        else:
            if node.right is None:
                node.right = n
                print(f"{val} is added on the right")
            else:
                self.insertNode(node.right,val)

    def inOrder(self,node):
        if node is not None:
            self.inOrder(node.left)
            print(node.data,end=" ")
            self.inOrder(node.right)

    def preOrder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=" ")

# DFS using recursion
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


# DFS using stack (iterative)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # push neighbors in reverse for correct order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
