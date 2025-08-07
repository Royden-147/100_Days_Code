# Second Biggest with 1 Loop

def SecBig(x):
    a,b = 0,0
    for i in range(len(x)):
        if x[i] > a:
            b = a
            a = x[i]
        elif i > b and i != a:
            b = x[i]
    return b

# reversing words in string
def StringRev(ab):
    ac = ab.split()
    for i in ac[::-1]:
        print(i,end=" ")

# Print Duplicate letters in a string
def dupStr(x):
    a=[]
    for i in x:
        if i in a:
            print(i,end=" ")
        a.append(i)

# Stack
class StacK1:
    def __init__(self,cap):
        self.s = [0]*cap
        self.cap = cap
        self.top = -1
        print(self.s, self.top)

    def isFull(self):
        if self.top == self.cap-1:
            return True
        else:
            return False

    def push(self,ele):
        if self.isFull():
            print("Stack Over Flow")
            return
        self.top += 1
        self.s[self.top] = ele
        print(self.s, self.top)

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("Stack Under Flow")
            return
        self.s[self.top] = 0
        self.top -= 1
        print(self.s,self.top)

    def peek(self):
        if self.isEmpty():
            print("Stack Under Flow")
            return
        print(self.s[self.top])

    def size(self):
        print(self.top + 1)

    def display(self):
        for i in range(self.top+1):
            print(self.s[i],end = ' ')

# Queues
class MyQueue:
    def __init__(self,cap):
        self.queue = [0] * cap
        self.cap = cap
        self.front,self.rear = 0,0

    def enqueue(self,element):
        if self.isFull():
            print("Queue is full")
            return
        self.queue[self.rear]=element
        self.rear += 1
        print(f"Element {element} added successfully")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        # self.queue. pop(self.front)
        element = self.queue[self.front]
        self.front += 1
        print(f"removed {element} successfully")
        return element

    def size(self):
        # return self.rear - self.front
        print(self.rear - self.front)

    def isFull(self):
        if self.rear == self.cap:
            return True
        else:
            return False

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def peek(self):
        return self.queue[self.front]

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        for i in range(self.front,self.rear):
            print(self.queue[i],end= " ")