##def ADD(n1,n2):
##    '''In this Function there is addition
##of twon numbers which is given by user of this program'''
##    print(n1+n2)
##n1=int(input("enter the first number: "))
##n2=int(input("enter the second number: "))
##ADD(n1,n2)
##print(ADD.__doc__)
def ADD(*n):
    sum=0
    for i in n:
        sum=sum+i
    print(sum)

##n=input("enter the numbers: ")
(ADD(9,7,75,8))



##pip 8
import this

