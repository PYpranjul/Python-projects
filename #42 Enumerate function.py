# a=("Pranjul","Raj" ,"Harry",90,10,50)
# b=0
# for i in a:
#     print(i)
#     if b==2:
#         print(i,"Teacher")
#     b=b+1

a=("Pranjul","Raj" ,"Harry",90,10,50)
for i,b in enumerate(a):
    if i==2:
        print(i,b,"Teacher")
        continue
    print(i,b)
