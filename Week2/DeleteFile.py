import os

filename = input("Enter a file name:")
if os.path.exists(filename):
  os.remove(filename)
else:
  print("The file does not exist")
