d=input("Enter the first num: ")
c=input("enter the second num: ")
def g(a,b):
    print(a) if a>b else print("equal") if a==b else print(b)
g(c,d)
e=9 if c>d else 0
print(e)