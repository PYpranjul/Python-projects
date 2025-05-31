##i=int(input("Enter the Num: "))
##for k in range(1,11):
##    if k==5:
##        continue
##    print (i,"x",k,"=",i*k)
##print("Try to put One")
##i=int(input("Enter the Num: "))
##for k in range(1,11):
##    if i>=2:
##        print (i,"x",k,"=",i*k)
##    if i<2:
##        print("Try Again")
##        break
##    i want to make a loop where if num is less than 2 then it will ask again to input the number and it will go inside the loop of table maker
i=int(input("enter a num: "))
if i>2:
    for k in range(1,11):
        print(i,"x",k,"=",i*k)
if not i>2:
    for k in range(1,11):
        print(i,"x",k,"=",i*k)
        break
print("Do while loop successfully executed")
