class Node:
    def __init__(self):
        self.data=None
        self.next=None
class Linkedlist :
    def __init__(self):
        self.head=None
    def add_new(self,data):
        new =  Node(data)
        if self.head is None:
            self.head = new
            