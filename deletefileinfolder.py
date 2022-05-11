import os
import shutil

#Target folder to clear
working_folder = r'C:\Path'
 
for files in os.listdir(working_folder):
    path = os.path.join(working_folder, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
        print("content deleted")
