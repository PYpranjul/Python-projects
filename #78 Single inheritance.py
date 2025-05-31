class Animal:
    def __init__(self):
        Ani=input("Which type of animal you are?: ").strip().lower()
        if Ani=="human":
            print("Yes!")
        else:
            print("Hello cat!!")
    def intro(self):
        name=input("Enter your name: ")
        print(f"Hi Human {name}")
    def cat_name(self):
        r=input("Enter Cat Name: ")
class Cat(Animal):
    def intro(self):
        Nam=input("Hi Cat what's up! ")
        return (f"Okay i like whatever {Nam}n you are doing")
    def cat_name(self):
        real=input("Enter your real name: ")


a=Cat()
a.cat_name()
print(a.intro())
print(a.cat_name())