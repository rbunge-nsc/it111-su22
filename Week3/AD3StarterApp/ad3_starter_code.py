import re
import os

# Select a file
filename = "auth.log"

# Select a search term
txt = "Invalid"

# Check the file for the search term line by line
#with open(filename) as f:

with open(os.path.join(os.path.dirname(__file__), filename)) as f:
    for line in f:
        match = re.search(txt, line)
        if match:
            print(match.string)
