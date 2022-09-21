class Node:
    def __init__(self,inital = None):
        self.value = inital
        self.next = None
    def isempty(self):
        return (self.value == None)
    def append(self, v):
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            (self.next).append(v)
    def insert(self, v):
        if self.isempty():
            self.value = v
            print("Inserted value is : ",v)
        newnode = Node(v)
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)
        print("Inserted value is : ",v)

