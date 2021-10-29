class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == False:
            return(False)
        else:
            self.ledger.append({"amount": float(-amount), "description": description})
            return(True)

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance = balance + self.ledger[self.ledger.index(item)]["amount"]
        return(balance)
    
    def transfer(self, amount, category):
        if self.check_funds(amount) == False:
            return(False)
        else:
            self.withdraw(amount)
            category.deposit(amount)
            return(True)
    
    def check_funds(self, amount):
        if float(amount) > self.get_balance():
            return(False)
        else:
            return(True)

#def create_spend_chart(categories):
