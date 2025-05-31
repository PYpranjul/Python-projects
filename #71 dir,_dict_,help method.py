p=[1,"harry",None,True,]
print(dir(p))
l=[5,10]
print(p.__add__(l))


class Person:
    def __init__(self):
        self.name=input("Enter your name: ")
        self.age=input("Enter your age: ")
p=Person()
print(p.__dict__)

print(help(str))