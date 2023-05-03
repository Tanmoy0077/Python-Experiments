class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class My_Linked_List:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)

    def __str__(self):
        if self.is_empty():
            return "The Linked list is empty"
        else:
            temp = self.head
            out = "The Linked list is : "
            while temp:
                out = out + str(temp.val) + " "
                temp = temp.next
            return out + "\n"
    
    def pop(self):
        if self.is_empty():
            print("The Linked List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            temp = prev = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            prev.next = None

    def del_begin(self):
        if self.is_empty():
            print("The Linked list is empty")
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
    
    def add_begin(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
    

if __name__ == '__main__':
    obj = My_Linked_List()
    obj.append(23)
    obj.append(12)
    obj.append(89)
    obj.append(90)
    print(obj)
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    obj.pop()
    print(obj)
    obj.append(667)
    print(obj)
    # obj.pop()