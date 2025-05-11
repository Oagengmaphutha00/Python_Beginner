symbols = ['🍒',' 🍇', '🍉', '7️⃣']
import random

def play():
  while True:
      results = random.choices(symbols, k=3)
      print(results)
      user = input("Keep Playing? (Y/N) ")
      if user == "Y" or user == "y":
          results = random.choices(symbols, k=3)
          print(results)
          if results == ['7️⃣', '7️⃣', '7️⃣']:
              print("JACKPOT!")

              break
          else:
              print("Keep playing, almost close")
      else:
          print("Thanks for playing!")
          break

play()
