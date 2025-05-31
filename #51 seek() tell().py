with open("For #51.txt","w") as p:
    p.write("This is only for Testing purpose")
    p.truncate(2)   # only reamin 2 char in the file
    p.writelines(["\n","In the Second line i want to see waht happens"]) # it will write the line in the file
with open("For #51.txt","r") as p:
    p.seek(3)       # it will start reading from 3rd char
    print(p.tell()) # it will how much seek is done
    a=p.read(5)     # it will read 5 char from the file
    print(a)
# with open("requirement.txt","r") as p:
#     # p.seek(1)
#     # print(p.tell())
#     print(p.read(8))