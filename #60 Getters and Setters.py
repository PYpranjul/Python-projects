#Getters

class Person:
    def __init__(self):
        self.Name =input("Enter Your Name: ")
        self.age = int(input("Enter Your Age: "))
    def intro(self):
        print(f"Hey My name is {self.Name},I am {self.age} year old")
    
    @property
    def real_age(self):
        return 10+self.age

    @real_age.setter
    def ageset(self,value):
        self.age=value

        
a=Person()
print(a.real_age)
a.intro()
a.ageset=20
print(a.ageset)
a.intro()