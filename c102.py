import os, shutil
src = "C:/Users/skmos/Desktop/C102_assets-main"
dst = "C:/Users/skmos/Desktop"
exts = [".gif",".jfif",".jpg",".png"]
files = os.listdir(src)
#print(files)
for file in files:
    name,ext= os.path.splitext(file)
    print(ext)
    if ext=='':
        continue
    elif ext in exts:
        path1 = src+"/"+file
        path2 = dst+"/images"
        path3 = path2+"/"+file
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)
