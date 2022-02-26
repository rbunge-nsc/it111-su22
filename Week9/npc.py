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