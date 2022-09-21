class Heap:
    def __init__(self, size):
        self.heap = [None] * size
        self.pos = 0
        self.capacity = size
        self.size = 0

    def leaf(self, pos):
        if (self.heap[2*pos+1] == None and self.heap[2*pos+2] == None):
            return True
        else:
            return False

    def emright(self, pos):
        if (self.heap[2*pos+2] == None):
            return True
        else:
            return False

    def isparent(self, pos):
        if(self.heap[2*pos+1] != None and self.heap[2*pos+2] != None):
            return True
        else:
            return False

    def insert(self, val):
        if self.pos == 0 and self.size == 0:
            self.heap[0] = val
            self.size += 1
        elif self.size == self.capacity:
            print("Heap Overflow")
        elif self.leaf(self.pos):
            self.heap[2*(self.pos)+1] = val
            self.size += 1
        elif self.emright(self.pos):
            self.heap[2*(self.pos)+2] = val
            self.size += 1
            self.pos += 1
    
    def display(self):
        for i in range(self.pos+1):
            try:
                if self.leaf(i):
                    continue
                else:
                    print(f"Parent : {self.heap[i]} Left Child : {self.heap[2*i+1]} Right Child : {self.heap[2*i+2]}")
            except:
                pass

H = Heap(15)
H.insert(5)
H.insert(3)
H.insert(17)
H.insert(10)
H.insert(84)
H.insert(19)
H.insert(6)
H.insert(22)
H.insert(9)
H.display()