import re

# Select a file
filename = "auth.log"

# Select a search term
txt = "Invalid"

# Check the file for the search term line by line
with open(filename) as f:
    for line in f:
        match = re.search(txt, line)
        if match:
            print(match.string)
