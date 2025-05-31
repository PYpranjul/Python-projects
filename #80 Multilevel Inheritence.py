class Human:
    def __init__(self):
        self.species=input("Enter the Species: ")
    def show(self):
        print(f"You are {self.species}")
class Employee(Human):
    def __init__(self):
        super().__init__()
        self.work=input("Enter your work: ")
    def show(self):
        super().show()
        print(f"Hi! You are working in {self.work} field")
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        self.program=input("Enter your working language: ")
    def show(self):
        super().show()
        print(f"Welcome Onboarding of {self.program} ,Congratulation we welccome you to work with us")
p=Programmer()
print(p.show())


# class Human:
#     def __init__(self,species):
#         self.species=species
#     def show(self):
#         print(f"You are {self.species} ")
# class Employee(Human):
#     def __init__(self,work):
#         Human.__init__(self,species="Employee")
#         self.work=work
#     def show(self):
#         Human.show(self)
#         print(f"You are intrested in {self.work} field")
# class Programmer(Employee):
#     def __init__(self,program):
#         Employee.__init__(self,work="Programmer")
#         self.program=program
#     def show(self):
#         Employee.show(self)
#         print(f"Congrats you are selected for {self.program} your package is 36LPA")
# p=Programmer("Python")
# print(p.show())