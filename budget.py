import math
#Classes------------------------------------
class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        total = "Total: " + str(self.get_balance())
        self.printout = ""
        self.stars = int(((30 - len(self.category))/ 2))* "*"
        self.title = self.stars + self.category + self.stars + "\n"
        self.printout += self.title

        for item in self.ledger:
            description = self.ledger[self.ledger.index(item)]["description"]
            amount = format(self.ledger[self.ledger.index(item)]["amount"], ".2f")
            item_line = ""
            item_line = description[0:23] +  (30 - len(description[0:23]) - len(amount)) *" " + amount[0:7] + "\n"
            self.printout += item_line      
        self.printout += total
        return(self.printout)

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": float(amount), "description": description})
        
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
            self.withdraw(amount, ("Transfer to " + category.category))
            category.deposit(amount, ("Transfer from " + self.category))
            return(True)
    
    def check_funds(self, amount):
        if float(amount) > self.get_balance():
            return(False)
        else:
            return(True)


#Functions-------------------------------------------------------
def create_spend_chart(categories):
    wd_list = []
    perc_list = list()
    cat_list = list()
    wd_total = 0
    spend_chart = ""


#dictionary with Categories, withdrawal and percentage
    for category in categories:
        wd_cat = 0
        for item in category.ledger:
            if category.ledger[category.ledger.index(item)]["amount"] < 0:
                wd_cat += category.ledger[category.ledger.index(item)]["amount"] 
                wd_total += wd_cat
        wd_list.append({"Category": category.category, "wd": wd_cat})    
    for item in wd_list:
        wd_list[wd_list.index(item)]["Percentage"] = str((math.floor(wd_list[wd_list.index(item)]["wd"]/wd_total*10))*10)

#creating list with percentages
    for item in wd_list:        
        perc_list.append(wd_list[wd_list.index(item)]["Percentage"])
    for percentage in perc_list:
        for item in wd_list:
            if item["Percentage"] == percentage:
                cat_list.append(item["Category"])
        
#creating lines for title and chart and appending to the list lines
    lines = ["Percentage spent by category"]    
    for i in range(11):
        perc = str((10 - i)* 10)
        x = (3 - len(perc))*" "+ perc + "| "
        for item in perc_list:
            if item == perc or int(item) > int(perc):
                x += "o  "
            else:
                x += "   "
        lines.append("\n" + x)
    lines.append("\n" + "    -" + (len(categories)* "---"))

#deteriming length of longest category
    for item in categories:
        longest_cat = 0
        if longest_cat < len(item.category):
            longest_cat = len(item.category)

#creating lines for category labels and appending to the list lines    
    for i in range(longest_cat):
        x = "\n" + 5*" "
        for cat in cat_list:
            if i < len(cat):
                x += cat[i] + "  "
            else: 
                x += "   "
        lines.append(x)

#concatenating all the lines to a string
    for line in lines:
        spend_chart += line

    return(spend_chart)
#---------------------------------------------------------------------------