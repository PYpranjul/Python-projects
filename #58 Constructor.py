# class Person():
#     def __init__(self):   #Constructor
#         Name =input("Enter Your Name: ")
#         Age = int(input("Enter Your Age: "))   
#         work = input("Enter Your Work: ")
#         self.Name = Name
#         self.Age = Age
#         self.work = work
#     def intro(self):
#         print(f"Hey My name is {self.Name},I am {self.Age} year old and I work for {self.work  }")
# a=Person()
# a.intro()


class Person():
    def __init__(self): #Default constructor because it has no parameter
        print("Hello")
    def __init__(self,Name,Age,work):   #Parameterized constructor because it has parameter
        # Name =input("Enter Your Name: ")
        # Age = int(input("Enter Your Age: "))   
        # work = input("Enter Your Work: ")
        self.Name = Name
        self.Age = Age
        self.work = work
    def intro(self):
        print(f"Hey My name is {self.Name},I am {self.Age} year old and I work for {self.work  }")
a=Person("Rahul",20,"Student")
a.intro()
# b=Person()
# b.intro()