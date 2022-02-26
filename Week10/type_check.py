print("Enter a number")
answer = input()
if not type(answer) is int:
  raise Exception("Hey, you need to enter a number!")