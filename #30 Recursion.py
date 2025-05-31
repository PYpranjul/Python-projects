n=int(input("Enter the num: "))
def Fibonacci_sequence(n):
    '''this is Fibonacci sequence f(n)=(n-1)+(n-2)'''
    if n==0 or n==1:
        return 1
    else:
        return  (n-1)+(n-2)
n=print(Fibonacci_sequence(n))
print(Fibonacci_sequence.__doc__)
#Factorial
a=int(input("Enter the num: "))
def factorial(p):
    if p==0 or p==1:
        return 1
    else:
        return p*factorial(p-1)
print(factorial(a))
