def get_item(par1):
  if par1 == 1:
    return '🍔 Cheeseburger'
  elif par1 == 2:
    return '🍟 Fries'
  elif par1 == 3:
    return  '🥤 Soda'
  elif par1 == 4:
    return  '🍦 Ice Cream'
  elif par1 == 5:
    return  '🍪 Cookie' 
  par1 == option   

def welcome():
  print(" Here is your menu: ")
  print("1 - 🍔 Cheeseburger")
  print("2 - 🍟 Fries ")
  print("3 - 🥤 Soda ")
  print("4 - 🍦 Ice Cream")
  print("5 - 🍪 Cookie")
welcome()
option = int(input("What is your option: "))
print(get_item(option))
  
        




