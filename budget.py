class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.printout = ""
        self.stars = int(((30 - len(category))/ 2))* "*"
        self.title = self.stars + self.category + self.stars + "\n"
        self.printout += self.title

    def __str__(self):
        for item in self.ledger:
            description = self.ledger[self.ledger.index(item)]["description"]
            print("description: " + description + "\n")
            amount = self.ledger[self.ledger.index(item)]["amount"]
            print("amount: "+ str(amount) + "\n")
            item_line = ""
            if len(description) > 23:
                item_line = description[0:23] +  (30 - 23 - len(str(amount))) *" " +str(amount) + "\n"
                self.printout += item_line
            else:
                item_line = description +  (30 - len(description) - len(str(amount))) *" " +str(amount) + "\n"
                self.printout += item_line            
        return(self.printout)

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
