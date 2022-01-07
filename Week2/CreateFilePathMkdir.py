#This one feel clugy! But it works on test. For what it's worth!

import os
filename = input("Enter a file name:")

# dirpathway must be complete and explicit
# example: C:/Users/Bob/Desktop/IT111Files/IT111-Exercises/Week2/
dirpathway = input("Enter a directory pathway: ")
dirname = input("Enter a name for a new directory: ")
path = os.path.join(dirpathway, dirname)
os.mkdir(path)
fullname = path + "/" + filename

f = open(fullname, "x")
print("File name " + filename + " has been created.")
textinput = input("Enter some text:")
f = open(fullname, "a")
f.write(textinput)
f.close()