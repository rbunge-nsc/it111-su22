#Elf class example 2
class Elf:
   def __init__(self, name, race):
      self.name = name
      self.race = race
 

#Test code
test1 = Elf("Rydel", "wood")

print(test1.name)

test2 = Elf("Jassin", "moon")

test3 = Elf("Klaern", "valley")

print(test2.name)

print(test3.name)