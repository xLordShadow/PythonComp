"""
This repository simulates a vending machine
"""
        

#These list out the items and marks out the item with a certain integer
aitems = {"1":"Lays Classic", "2":"Lays BBQ", "3":"Lays Dill Pickle", "4":"Lays Flaming Hot", "5":"Lays Salt & Vinegiar"}
alist = "1: Lays Classic\n2: Lays BBQ\n3: Lays Dill Pickle\n4: Lays Flaming Hot\n5: Lays Salt & Vinegiar"
bitems = {"1":"Trident Splashing Mint", "2":"Trident Splashing Fruit", "3":"Trident Wintergreen", "4":"Trident Passionberry Twist", "5":"Trident Original Flavor"}
blist = "1: Trident Splashing Mint\n2: Trident Splashing Fruit\n3: Trident Wintergreen\n4: Trident Passionberry Twist\n5: Trident Original Flavor"
citems = {"1":"Kit Kat", "2":"Hershey's Milk Chocolate Bar", "3":"WHATCHAMACALLIT", "4":"Toblerone", "5":"Reese's Peanut Butter Cups"}
clist = "1: Kit Kat\n2: Hershey's Milk Chocolate Bar\n3: WHATCHAMACALLIT\n4: Toblerone\n5: Reese's Peanut Butter Cups"
ditems = {"1":"Twinkie", "2":"Cosmic Brownie", "3":"Cookie", "4":"Cinnamon Roll", "5":"First born child"}
dlist = "1: Twinkie\n2: Cosmic Brownie\n3: Cookie\n4: Cinnamon Roll\n5: First born child"
eitems = {"1":"ThinkThin Chocolate Strawberry", "2":"Nature Valley", "3":"ZONE Perfect Nutrition Bar", "4":"EPIC Bar Bacon", "5":"RXBar Coffee Chocolate"}
elist = "1: ThinkThin Chocolate Strawberry\n2: Nature Valley\n3: ZONE Perfect Nutrition Bar\n4: EPIC Bar Bacon\n5: RXBar Coffee Chocolate"


#This list out the basic variables that will be changed in the program
money = 0
letter = ""
using = True
number = ""

#This function defines the amount the money the user inputs
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

#This function defines which letter the user picks
def getLetter():
  print "A: Chips\nB: Gum\nC: Chocolate Bars\nD: Snack Cakes\nE: Protein Bars"
  ll = input("Enter the letter to the item you wish to get: ")
  l = ll.lower()
  global letter
  try:
    if l == "a":
      letter = "a"
      print alist
      return
    elif l == "b":
      letter = "b"
      print blist
      return
    elif l == "c":
      letter = "c"
      print clist
      return
    elif l == "d":
      letter = "d"
      print dlist
      return
    elif l == "e":
      letter = "e"
      print elist
      return
    else:
      print "Please input a valid letter. (A-E)"
      getLetter()
  except IndexError:
    getLetter()


#This function defines the number that the user picks
def getNumber():
  n = input("Please enter the number to the item you want")
  if n[0] == " ":
    print "Please input a valid number to the item you want (1-5)"
    getNumber()
  if n.isdigit():
    if int(n) >= 1 and int(n) <= 5:
      global number
      number = n
    else:
      print "Please input a valid number to the item you want (1-5)"
      getNumber()
  else:
    print "Please input a valid number to the item you want (1-5)"
    getNumber()
      
  
    
enterMoney()
#This is the program running to string it all together
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
  if letter == "b":
    print "You received your " + bitems[number] + "!"
    money = money - 1
    print "Your new balance is $" + str(money)
    if money < 1:
      print "Enter nothing to quit"
      enterMoney()
      break;
    else:
      continue
  if letter == "c":
    print "You received your " + citems[number] + "!"
    money = money - 1
    print "Your new balance is $" + str(money)
    if money < 1:
      print "Enter nothing to quit"
      enterMoney()
      break;
    else:
      continue
  if letter == "d":
    print "You received your " + ditems[number] + "!"
    money = money - 1
    print "Your new balance is $" + str(money)
    if money < 1:
      print "Enter nothing to quit"
      enterMoney()
      break;
    else:
      continue
  if letter == "e":
    print "You received your " + eitems[number] + "!"
    money = money - 1
    print "Your new balance is $" + str(money)
    if money < 1:
      print "Enter nothing to quit"
      enterMoney()
      break;
    else:
      continue
  
print "Enjoy :D"
