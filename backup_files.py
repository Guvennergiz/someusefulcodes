import os
import shutil
result_file_types=[]
#Working folder and files to backup
working_folder = r'C:\Path'
backup_folder = r'C:\Path'
result_file_types =["filenamewithextension.CATPart",
                    "filenamewithextension.x_t",
                    "filenamewithextension.l",
                    "filenamewithextension.fph",
                    "filenamewithextension.pph",
                    "filenamewithextension.bdf",
                    "filenamewithextension.f04",
                    "filenamewithextension.f06",
                    "filenamewithextension.h5",
                    "filenamewithextension.log"]

file_count=len(result_file_types)

#folder naming and numbering
index=0 #index for numbering, you can close it if you want
result_folder="\Radom-0"+str(int(index))
target_folder = backup_folder + result_folder
os.makedirs(target_folder)

result_files=[]
target_files=[]

for k in range(file_count):
    file=working_folder + "\\" + result_file_types[k]
    result_files.append(file)
    target = target_folder + "\\" + result_file_types[k]
    target_files.append(target)
    shutil.copyfile(result_files[k],target_files[k])

print("Backup done")

