import os
newpath =r"P:\python programs\os module"
if not (os.path.exists(newpath)):
    os.mkdir(newpath)
# os.mkdir("os module\Day 100")
os.rename("P:\python programs\os module","P:\python programs\OS Module")
# for i in range (1,100):
#     os.rename(f"os module\day {i}",f"os module\Day {i}")
folders =os.listdir("OS Module")
print(folders)
for i in folders:
    # print(i)
    print(os.listdir(f"OS Module\{i}"))
print(os.getcwd())