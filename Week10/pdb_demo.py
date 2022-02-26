


import pdb
import re

pdb.set_trace()
text = "Search me now!"
# Searching for the character "m" in the text. 
# For a different search, replace "m" with a different search target in the text below.
found = re.search("m", text)

if found:
  print("Found it!")
else:
  print("Nope")
