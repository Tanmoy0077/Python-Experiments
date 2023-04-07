"""
When we inherit a class in another class and try to access any variable or method it first searches its own 
instance variables then if not found then in parent class's instance varibles if not found then again its own class
variables then if not found it searches in the parent class's class variables.
"""
class A:
    # var1 = "Class variable in A"
    def __init__(self):
        self.var1 = "Instance variable in A"

class B(A):
    pass
    # var1 = "Class variable in B"
    # def __init__(self):
    #     self.var1 = "Instance variable in B"

class C(A):
    pass
    # var1 = "Class variable in C"
    # def __init__(self):
    #     self.var1 = "Instance variable in C"

class D(B, C):
    # pass
    var1 = "Class variable in D"
    # def __init__(self):
    #     self.var1 = "Instance variable in D"

d = D()
print(d.var1)