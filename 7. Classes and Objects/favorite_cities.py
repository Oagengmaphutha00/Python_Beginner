class City():
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
new_york = City("New york", "America", '10 000', ["The tower"])

print(vars(new_york))
