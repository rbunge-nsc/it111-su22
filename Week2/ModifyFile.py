filename = input("Enter a file name:")
f = open(filename, "a")
print("File name " + filename + " has been opened.")
textinput = input("Enter some text to add to the file:")
f.write(textinput)
f.close()


