class Employee:
    def __init__(self):
        self.name=input("Enter your Name: ")
        self.age=input("Enter your Age: ")
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return (f" Hi Mr/Ms. {self.name},You are {self.age} years old")
    def __reper__(self):
        return ()
    def __call__(self):
        return ()
p=Employee()
print(len(p))

