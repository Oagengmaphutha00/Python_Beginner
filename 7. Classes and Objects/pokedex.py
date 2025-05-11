class Pokemon():
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.description = description
    self.types = types
    self.is_caught = is_caught
  def speak(self):
    return self.name + self.name
  def display_details(self):
    print("Entry number: ", self.entry)
    print("Name: ", self.name)
    print("Type: ", self.types)
    print("Description: ", self.description)
    print(self.is_caught, "Pikachu has already been caught!" if self.is_caught == True else "Pikachu has not been caught yet!")

pokemon = Pokemon(25, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True)
pokemon.speak()
pokemon.display_details()
