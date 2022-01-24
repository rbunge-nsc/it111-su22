guess = []
guess.append("s")
guess.append("c")
for letter in "succotash":
  if letter in guess:
   print(letter)
  else:
   print("?")