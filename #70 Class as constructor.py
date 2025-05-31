class Employee:
    def __init__(self,name=None,age=None):
        if name is None and age is None:
            self.name=input("Enter your name: ")
            self.age=input("Enter your age: ")
        else:
            self.name=name
            self.age=age

    @classmethod
    def fromstring(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
a=Employee()
print(a.name)
data="Myst-29"
p=Employee.fromstring(data)
print(p.name)
print(p.age)