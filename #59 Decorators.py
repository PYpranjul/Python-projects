def greet(cls):
    def wrapped(*args,**kwargs):
        print("It's a pleasure to meet you")
        result=cls(*args,**kwargs)
        print("Welcome to the world of Python")
        return result
    return wrapped

def fungreet(fx):
    def wrap():
        print("Hey there!")
        fx()
        print("Fixed the issue")
    return wrap

@greet
class Person:
    def __init__(self):
        Name =input("Enter Your Name: ")
        Age = int(input("Enter Your Age: "))
        # work = input("Enter Your Work: ")
        self.Name = Name
        self.Age = Age
        # self.work = work
    def intro(self):
        print(f"Hey My name is {self.Name},I am {self.Age} year old and I work for ")
a=Person()
a.intro()

# @greet
# def Add(a,b):
#     print(a+b)
# Add(9,8)


@fungreet
def hello():
    print("Hello World")

hello()