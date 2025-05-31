#Hybrid
class Animal:
    def __init__(self):
        self.Animal=input("Which type oF Animal you are? ")
        self.show()
    def show(self):
        print(f"You are {self.Animal}")
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.gender= input("Enter The gender: ")
        self.show()
    def show(self):
        print (f"Hi Human your gender is {self.gender}")
class Men(Animal):
    def __init__(self):
        super().__init__()
        self.male=input("Enter Your name: ")
        self.show()
    def show(self):
        print(f"You are {self.male}")
class Insaan(Human,Men):
    def __init__(self):
        super().__init__()
    def Result(self):
        print(f"{self.Animal},{self.gender}")
p=Insaan()
p.Result()