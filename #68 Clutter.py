# import os
# newpath=r"P:\python programs\Cluttered exp"
# if not (os.path.exists(newpath)):
#     os.mkdir(newpath)
# for i in range (1,101):
#     file=os.path.join(newpath,f"Exp{i}.txt")
#     with open(file,"w") as p:
#         pass
# o=os.path.join(newpath,"Exp1.txt")
# with open(o,"r") as p:
#     print(p.read())
# with open(o,"w") as p:
#     p.write("Hey There Am i Sucessfully loaded")
# o=os.path.join(newpath,"Exp2.txt")
# with open(o,"w") as r:
#     r.write("Main bhi aa gya")
#     r.close()

# import os
# files=os.listdir("Cluttered exp")
# print(files)
# i=1
# for u in files:
#     if u.endswith(".txt"):
#         print(u)
#         os.rename(f"Cluttered Exp\\{u}",f"Cluttered Exp\\{i}.png")
#         i=i+1

import os
files=os.listdir("Cluttered exp")
i=1
for p in files:
    if p.endswith(".png"):
        os.rename(f"Cluttered exp\\{p}",f"Cluttered exp\\{i}.txt")
        i=i+1