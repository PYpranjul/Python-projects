##average by tuple method
##def Avg(*numbers):
##    sum=0
##    for i in numbers:
##        sum=sum+i
##    print("the Avg is ",sum/len(numbers))
##Avg(2,4,66,87)

##avg def 
##def Avg(a,b,c,d=7):
##    print((a+b+c+d)/4)
##Avg(b=40,c=5,a=9,d=0)

##return statement store in call function

##def Avg(*numbers):
##    sum=0
##    for i in numbers:
##        sum=sum+i
####    print("the avg is: ",sum/len(numbers))
##    return sum/len(numbers)
##c=Avg(4,5,6,7,8)
##print(c)

def name(**name):
    print("Hello",name["firstname"],name["secondname"],name["lastname"])
firstname=input("Enter the first name: ")
secondname=input("Enter the second name: ")
lastname=input("Enter the last name: ")
print(name)
name(firstname="pranjul",secondname="",lastname="sharma")

