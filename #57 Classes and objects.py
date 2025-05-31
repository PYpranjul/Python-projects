class person:
        Name = "Rahul"
        Age = 20
        work = "Student"
        def intro(self):
            print(f"Hey My Name is {self.Name} , I am {self.Age} year Old And i Work for {self.work}")

Name =input("Enter Your Name: ")
Age = int(input("Enter Your Age: "))
work = input("Enter Your Work: ")
a=person()
a.Name = Name
a.Age = Age
a.work = work
a.intro()
b=person()
b.intro()





# class person:
#     def intro(self):
#         Name = self.Name
#         Age = self.Age
#         work =self.work
#         return print(f"Hey My Name is {Name} , I am {Age} year Old And i Work for {work}")
# Name=input("Enter Your Name: ")
# Age=input("Enter Your Age: ")
# work=input("Enter Your Work: ")
# p1=person()
# p1.Name = Name
# p1.Age = Age
# p1.work = work
# p1.intro()