##a=input("Enter the num: ")
##try:
##    for i in range(1,11):
##        print(f"{int(a)} X {i}={int(a)*(i)}")
##except Exception as e:
##    print(e)
##    print("invalid input")
##print("This code is still running after the Error")
##




print("[8,9,9,,7,33,3524,35,4532,4242]")
try:
    a=[8,9,9,7,33,3524,35,4532,4242]
    c=int(input("Enter the Index value you want to print: "))
    print(a[c])
except ValueError:
    print("It's not a valid num")
except IndexError:
    print("Out of Range")
