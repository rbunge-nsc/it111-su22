filename = input("Enter a file name:")

# dirpathway must be complete and explicit
# example: C:/Users/Bob/Desktop/IT111Files/IT111-Exercises/Week2/testdir
dirpathway = input("Enter a directory pathway: ")
fullname = dirpathway + filename

f = open(fullname, "x")
print("File name " + filename + " has been created.")
textinput = input("Enter some text:")
f = open(fullname, "a")
f.write(textinput)
f.close()