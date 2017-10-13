"""
This repository simulates a vending machine
"""
items = {"A1":"Lays Classic", "A2":"Lays BBQ", "A3":"Lays Dill Pickle", "A4":"Lays Flaming Hot", "A5":"Lays Salt & Vinegiar",
        "B1":"Trident Splashing Mint", "B2":"Trident Splashing Fruit", "B3":"Trident Wintergreen", "B4":"Trident Passionberry Twist", "B5":"Trident Original Flavor",
        "C1":"Kit Kat", "C2":"Hershey's Milk Chocolate Bar", "C3":"WHATCHAMACALLIT", "C4":"Toblerone", "C5":"Reese's Peanut Butter Cups"}
aitems = {"1":"Lays Classic", "2":"Lays BBQ", "3":"Lays Dill Pickle", "4":"Lays Flaming Hot", "5":"Lays Salt & Vinegiar"}
alist = "1: Lays Classic\n2: Lays BBQ\n3: Lays Dill Pickle\n4: Lays Flaming Hot\n5: Lays Salt & Vinegiar"

money = 0
letter = ""
using = True
number = ""

def enterMoney():
  amount = input("Enter the amount of money you want to put in the machine: ")
  if amount == "":
    using = False
    return
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
    
def getLetter():
  ll = input("Enter the letter to the item you wish to get: ")
  l = ll.lower()
  global letter
  if l[0] == "a":
    letter = "a"
    print alist
    return
  elif l[0] == "b":
    letter = "b"
    print blist
    return
  elif l[0] == "c":
    letter = "c"
    print clist
    return
  elif l[0] == "d":
    letter = "d"
    print dlist
    return
  elif l[0] == "e":
    letter = "e"
    print elist
    return
  else:
    print "Please input a valid letter. (A-E)"
    getLetter()

    
def getNumber():
  n = input("Please enter the number to the item you want")
  if n.isdigit():
    if int(n) >= 1 and int(n) <= 5:
      global number
      number = n
    else:
      print "Please input a valid number to the item you want (1-5)"
      getNumber()
      
  
    
enterMoney()
    
while using == True:
  getLetter()
  getNumber()
  if letter == "a":
    print "You received your " + aitems[number] + "!"
    money = money - 1
    print "Your new balance is $" + str(money)
    if money < 1:
      print "Enter nothing to quit"
      enterMoney()
      break;
    else:
      continue
  
print "Enjoy :D"
