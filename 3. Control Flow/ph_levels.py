ph_variable = int(input('Please enter a value between 0 and 14: '))
if ph_variable > 7:
  print("Basic")
elif ph_variable < 7:
  print("Acidic")
else:
  print("Neutral")    
