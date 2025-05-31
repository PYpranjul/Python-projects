l=[5,8,9,10,1,3,6]
def cube(x):
    return x*x*x
# newl=[]
# for i in l:
#     newl.append(cube(i))
# print(newl)

cl=list(map(cube,l))
print(cl)
sl=list(map(lambda x:x*x,l))
print(sl)

def filter_fun(x):
    return x>5 
# fl=list(filter(filter_fun,l))
fl=list(filter(filter_fun,l))
print(fl)

from functools import reduce
# def add(x,y):
#     return x+y
rl=reduce(lambda x,y:x+y,l)
print(rl)