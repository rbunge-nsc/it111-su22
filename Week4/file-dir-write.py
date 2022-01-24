import os

save_path = 'C:\\Users\\Bob\\Desktop\\IT111Files\\IT111-Exercises\\Week5\\home'
file_name = "test.txt"

completeName = os.path.join(save_path, file_name)
print(completeName)
#OUTPUT
#/home/test.txt

file1 = open(completeName, "w")
file1.write("file information")
file1.close()