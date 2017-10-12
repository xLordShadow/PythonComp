"""
This repository simulates a vending machine
"""
items = {"A1":"Lays Classic", "A2":"Lays BBQ", "A3":"Lays Dill Pickle", "A4":"Lays Flaming Hot", "A5":"Lays Salt & Vinegiar",
        "B1":"Trident Splashing Mint", "B2":"Trident Splashing Fruit", "B3":"Trident Wintergreen", "B4":"Trident Passionberry Twist", "B5":"Trident Original Flavor",
        "C1":"Kit Kat", "C2":"Hershey's Milk Chocolate Bar", "C3":"WHATCHAMACALLIT", "C4":"Toblerone", "C5":"Reese's Peanut Butter Cups"}

money = 0

using = True

def enterMoney():
  amount = input("Enter the amount of money you want to put in the machine: ")
  if amount == "":
    using = False
  if amount.isdigit():
    if int(amount) == 0:
      print "You didnt put any money in!"
      enterMoney()
    else:
      global money
      money = money + int(amount)
      print "You balance is $" + str(money)
  else:
    print "Please enter a valid amount (Exp: 2, 5, 10)"
    enterMoney()
    
enterMoney()
    
while using == True:
  q = input("Enter the letter and number to the item you want\n" + "(A-E and 1-5)")
  if q[0].isdigit():
    print "Please make sure you do a letter and number (Exp: C3, A4, B1)"
    continue
  elif q[1].isdigit():
    print "You received your " + items[q] + "!"
    money = money - 1
    print "Your new balance is $" + str(money)
    if money < 1:
      print "Enter nothing to quit"
      enterMoney()
      break;
    else:
      continue
  else:
    print "Please make sure you do a letter and number (Exp: C3, A4, B1)"
    continue
  
print "Enjoy :D"
