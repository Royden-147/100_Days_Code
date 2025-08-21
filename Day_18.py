# Stack implementation using Linkedlist

class NodeS:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self,val):
        new_node = NodeS(val)
        new_node.next = self.top
        self.top = new_node
        print(f"pushed {val} into stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty!")
            return
        popped = self.top.data
        self.top = self.top.next
        print(f"{popped} popped from stack.")

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return
        return self.top.data

    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return
        cur = self.top
        while cur:
            print(cur.data,end=" -> ")
            cur = cur.next
        print("None")


# Node for linked list
class NodeQ:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = NodeQ(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        return self.front.data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")

