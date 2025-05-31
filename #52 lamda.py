# def sum(a,b):
#     return (a + b)
# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# print(sum(a,b))
# sum = lambda a,b: (a+b)
# print(sum(2,9))
# a=int(input("Enter the number: "))
# # def cube(x):
# #     return x*x*x
# cube =lambda x: x*x*x
# # print(cube(lambda a:(a*a),a))
# print(cube(a))


def why(fx,value):
    return fx(value) +10
x=int(input("Enter the number:  ")  )
print(why(lambda x: x*x*x ,x))