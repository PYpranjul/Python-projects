class Employee:
    company="Google"
    employee_NO=0
    def __init__(self):
        self.name=(input("Enter your name:"))
        self.age=(input("Enter your age:"))
        self.employee_NO +=1
    def intro(self):
        print(f"Hi Employee No. {self.employee_NO} Mr/Ms. {self.name},You are {self.age} years old,You are welcome to {self.company}")
p=Employee()
# p.biodata()
p.intro()
a=Employee()
a.company="Microsoft"
a.name="Bill Gates"
a.intro()