class Shape:
    def __init__(self):
        self.x=int(input("Enter the length: "))
        self.y=int(input("Enter the width: "))
    def area(self):
        return self.x*self.y
class Circle(Shape):
    # def __init__(self):
    def area2(self):
        # super().__init__()
        return 3.14*super().area()
p=Circle()
print(p.area2())