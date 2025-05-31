# f=open("file io.txt","r")
# i=0
# while True:
#    i=1+i 
#    line = f.readline()
#    if not line:
#       break
#    m1=int(line.split(",")[0])
#    m2=int(line.split(",")[1])
#    m3=int(line.split(",")[2])
#    print(f"the Marks of student {i} is in sub Math {m1}")
#    print(f"the Marks of student {i} is in sub Eng {m2}")
#    print(f"the Marks of student {i} is in sub Eng {m3}")
f=open("file io.txt","w")
# line=("1\n","2\n","3\n","4\n","5\n")
f.writelines(["1\n","2\n","3\n"])
f.close()

#    print(line))
# for i in f:
#     print(i)