# tuple for Vegas craps outcomes
first_roll = ("inspect dice", "inspect dice", "house wins", "house wins", "set point number", "set point number", "set point number", "shooter wins", "set point number", "set point number", "set point number", "shooter wins", "house wins")

index = 0;
while index < 13:
  print("Roll total:" + str(index) + ", " + first_roll[index])
  index = index + 1