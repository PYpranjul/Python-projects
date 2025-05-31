class Employee:
    company="HDFC Bank"
    def __init__(self):
        self.name=input("Enter your name:")
        self.age=input("Enter your age:")
    def intro(self):
        print(f"Hi Mr/Ms. {self.name},You are {self.age} years old,You are welcome to {self.company}")
    @classmethod
    def change_company(tinde):
        tinde.com=input("Enter the name of the company:")
        Employee.company=tinde.com
# p=Employee()
# p.intro()
# p.company="ICICI Bank"
# p.intro()
# print(p.company)
# a=Employee()
# a.intro()
# print(a.company)
m=Employee()
m.change_company()
m.intro()
m.company="Axis Bank"
m.intro()
print(m.company)
a=Employee()
a.intro()
