user_height = int(input("What is your height ? "))
user_credit = int(input("How many credits do you have ? "))
if user_height >= 137 and user_credit >= 10:
  print('Enjoy the Ride')
elif user_height < 137 and user_credit >= 10:
  print('You are not tall enough to ride')
elif user_height >= 137 and user_credit < 10:
  print("You do not have enough credits")
else:
  print('Did not meet the requirements')    
