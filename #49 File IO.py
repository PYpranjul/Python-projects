# o=open("file io.txt", "r")
# print(o.read())
# o.close()
o=open("file io.txt","w")
o.write("Common change the text")
o.close()
o=open("file io.txt","a")
o.write("\nnew text")
o=open("file io.txt","r")
print(o.read())
o.close()


#"with open file " we dont need to close the file
with open ("file io.txt","a") as p:
    p.write(" Start again")
with open ("file io.txt","r") as p:
    print(p.read())
