class BankAccount():
  def __init__(self, first_name, last_name, account_id, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.pin = pin
    self.balance = balance
  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance
  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance
  def display_balance(self):
    print(self.balance)
account = BankAccount("Oageng", "Maphutha", 15151212, 1234, 10000)
account.deposit(2000)
account.withdraw(5000)
account.display_balance()


