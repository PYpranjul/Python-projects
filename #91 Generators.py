def Raftaar():
    for i in range(5):
        yield i
    
p=Raftaar()
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
for i in p:
    print(i)