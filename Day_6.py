# Linked List

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert node at nth pos
    def nodeNPos(self,val,pos):
        new = Node(val)
        if pos == 0:
            new.next = self.head
            self.head = new
            return
        cur = self.head
        c = 0
        while c < pos-1:
            cur = cur.next
            c += 1
        new.next = cur.next
        cur.next = new

    # delete nth node
    def deleteN(self,pos):
        if pos == 0:
            self.head = self.head.next
            return
        cur = self.head
        c = 0
        while c < pos-1:
            cur = cur.next
            c += 1
        cur.next = cur.next.next





