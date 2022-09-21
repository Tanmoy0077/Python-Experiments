from math import sqrt
class point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def addpoint(self, delx, dely):
        self.x += delx
        self.y += dely
    def odistance(self):
        return (sqrt((self.x * self.x) + (self.y * self.y)))
    # When we use + it implicitly call __add__ function
    def __add__(self, p):
        return (point(self.x + p.x, self.y + p.y))

p1 = point(4, 3)
p2 = point(2, 3)
print("The first point is :", end=" ")
print("(",p1.x,",", p1.y,")")
# p1.addpoint(5, 4)
print("The second point is :", end=" ")
print("(",p2.x,",", p2.y,")")
print("The distance of the first point from origin is :", end=" ")
print(p1.odistance())
# print(p1.__str__())
p3 = p1 + p2    # We can also write p3 = p1.__add__(p2)
print("If we add these two points we will get :", end=" ")
print("(",p3.x,",", p3.y,")")