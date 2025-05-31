x=5 
y=4
z=10
def pranjul():
    x=7
    global y
    y="Testing"
    print(x)
    print(y)
    print(z)
pranjul()
print(x)
print(y)