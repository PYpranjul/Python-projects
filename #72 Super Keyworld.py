class Employee:
    def __init__(self):
        self.name=input("Enter your Name: ")
        self.age=input("Enter your Age: " )
class Programmer(Employee):
    def __init__(self):
        self.program=input("Enter the Lan Program: ")
        super().__init__()

# a=Employee()
# print(a.name)
p=Programmer()
print(p.program)
print(p.name)