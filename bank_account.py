 class BankAccount:
    def __init__(self, rate, balance = 0): 
        self.int_rate = (rate * .01)
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
       
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self 

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
       
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
        return self
       
        
