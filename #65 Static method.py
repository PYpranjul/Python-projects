class Person:
    def __init__(self):
        self.name =input("Enter your name: ")
        self.age =input("Enter your age: ")
    def display(self):
        print(f"Hi Mr/Ms. {self.name},You are {self.age} years old.")
    @staticmethod  
    def addition():
        occupation =input("Enter your occupation: ")
        print(f"Your occupation is {occupation}")
p= Person()
p.display()
p.addition()