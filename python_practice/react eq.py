class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

    def __eq__(self,other):
        return self.a==other.a and self.b==other.b
        
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1==rect_2)