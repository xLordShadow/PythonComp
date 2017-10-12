"""
This repository simulates a vending machine
"""
items = {"A1":"Lays Classic", "A2":"Lays BBQ", "A3":"Lays Dill Pickle", "A4":"Lays Flaming Hot", "A5":"Lays Salt & Vinegiar",
        "B1":"Trident Splashing Mint", "B2":"Trident Splashing Fruit", "B3":"Trident Wintergreen", "B4":"Trident Passionberry Twist", "B5":"Trident Original Flavor",
        "C1":"Kit Kat", "C2":"Hershey's Milk Chocolate Bar", "C3":"WHATCHAMACALLIT", "C4":"Toblerone", "C5":"Reese's Peanut Butter Cups"}

while True:
  q = input("Enter the letter and number to the item you want: ")
  if q[0].isdigit():
    print "Please make sure you do a letter and number"
    break
  elif q[1].isdigit():
    print items[q]
    break;
  else:
    print "Please make sure you do a letter and number"
    break