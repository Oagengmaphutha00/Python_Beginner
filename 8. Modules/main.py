import datetime, bday_messages
today = datetime.date.today()
next_birthday = datetime.date(2025, 8, 17)
days_away = next_birthday - today

if today == next_birthday:
  print(bday_messages.random_message)
else:
  print(f"My next birthday is {days_away} days away")

print(f'next birthday is in {next_birthday}')
