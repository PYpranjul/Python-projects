import shutil
import os
newpath=r"P:\python programs\Shutil exp"
os.makedirs(newpath,exist_ok=True)
for i in range(1,101):
    folder_name=f"S{i}"
    folder_path=os.path.join(newpath,folder_name)
    os.makedirs(folder_path,exist_ok =True)
base_path=r"P:\Super Sarah\1x\one last Xsuit.jpg"
if not os.path.isfile(base_path):
    print("Source file not found!")
else:
    print("Source file found.")

for i in range(1,101):
    target_path=os.path.join(newpath,f"S{i}")
    shutil.copy(base_path,target_path)
    print(f"file copiedb to {target_path}")


    
