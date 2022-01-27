class Character:
   def __init__(self, name, lifespan):
      self.name = name
      self.lifespan = lifespan
      
   def identify(self):
      print("I am " + self.name)

class Elf(Character):
   def setRace(self, race):
      self.race = race
   def claimTribe(self):
      self.identify()
      print("I am a " + self.race + " elf.")
      
class Dwarf(Character):
   def setBeard(self, beard_color):
      self.beard = beard_color
   def confront(self):
      self.identify()
      print(self.beard + "beard!")


test1 = Elf("Rydel", 1000)
test1.setRace("wood")
test1.claimTribe()

test2 = Dwarf("Dwotruk", 500)
test2.setBeard("red")
test2.confront()