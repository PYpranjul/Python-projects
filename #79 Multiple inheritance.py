class Employee:
    def __init__(self):
        self.name=input("Enter Your name: ")
    def __str__(self):
        return (f"Hi! {self.name}")
    def show(self):
        return "I am Employee"
class dance:
    def __init__(self):
        self.dance=input("which type of dance you like: ")
    def __str__(self):
        return (f"you like {self.dance}")
    def show(self):
        return "I am Dancing"
class ED(dance,Employee):
    def __init__(self):
        self.name=input("enter your name: ")
        self.dance=input("Which dance: ")
    def __str__(self):
        return "i am ED"
    # def show(self):
    #     return "I am class ED"

p=ED()
print(p.name)
print(p)
print(p.show())
a=dance()
print(a.show())
print(p.show())
print(ED.mro())