done = "no"
guess = []
while done != "#":
    print ("Solve the puzzle? Enter '#' Otherwise, guess a letter.")
    entry = input()
    if entry == "#":
       done = "#"
    else:
       guess.append(entry)
       for letter in "succotash":
            if letter in guess:
                 print(letter)
            else:
                 print("?")

