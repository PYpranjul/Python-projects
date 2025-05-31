#Public Access:

class Person:
    def __init__(self):
        self.name =input ("Enter your name:")

a=Person()
print(a.name) #public access

#Private Access:
class Employee:
    def __init__(self):
        self.__name =input("Enter your name:")
b=Employee()
# print(b.__name) #private access
print(b._Employee__name) #This is called Name Mangling

#protected access:
class Protected:
    def __init__(self):
        self._name =input("Enter your name:") #protected access
c=Protected()
print(c._name)