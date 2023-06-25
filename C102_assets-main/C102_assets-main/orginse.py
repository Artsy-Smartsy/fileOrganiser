import os
import shutil

from_dir="C102_assets-main"
to_dir="C102_assets-main"

list_of_files=os.listdir(from_dir)

for file_name in list_of_files:

    name,extention=os.path.splitext(file_name)
    if extention=="":
        continue
    if extention in [".gif", ".png", "jpg", "jpeg", "jfif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"image_file"
        path3=to_dir+"/"+"image_file"+"/"+file_name

        if os.path.exists(path2):
            print("Moving",file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving",file_name+"...")
            shutil.move(path1,path3)
