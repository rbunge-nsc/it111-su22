class Costume:
   def __init__(self, color, material):
      self.color = color
      self.material = material

class Elf:
   def __init__(self, name, race):
      self.name = name
      self.race = race
      if self.race == "wood":
         self.dress = Costume("green", "leather")
      elif self.race == "wild":
         self.dress = Costume("gray", "chainmail")
      else:
         self.dress = Costume("unknown", "unknown")
         
   def identify(self):
      print("Here stands " + self.name + " born of the " + self.race + " elves wearing " + self.dress.color + ".") 

test1 = Elf("Rydel", "wood")
test1.identify()
test2 = Elf("Ilthuryn", "wild")
test2.identify()