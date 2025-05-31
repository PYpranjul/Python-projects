class Person:
    def __init__(self):
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))

    def intro(self):
        print(f"Hey My name is {self.name},and my age is {self.age}")
    
class Programmer(Person):
        def __init__(self):
            self.code=input("Enter in which language you code: ")
        def intro(self):
            print(f"I code in {self.code}")
a=Person()
a.intro()
a=Programmer()
a.intro()
