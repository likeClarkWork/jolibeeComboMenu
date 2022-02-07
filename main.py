"""
Clark Royandoyan
1.31.22
Jollibee Menu Project
"""
import random
import math

input(
    "Hello po, mamser! Welcome to Jollibee self-order! Press \"enter\" to continue. "
)
#First loop asks for what item you want and the accompanying upgrades
while True: #meal order loop#meal order
    print(" ")
    entreeChoice = int(
        input("""What super meal would you like? (Please use 1, 2, or 3)
1. 1pc Chickenjoy w/ Burger Steak & Half Jolly Spaghetti (Comes with rice) [$3.55]
2. 1pc Chickenjoy w/ Half Jolly Spaghetti & Shanghai (Comes with rice) [$3.55]
3. Yumburger, Half Jolly Spaghetti & Small Fries [$2.36]

Make your selection here: """))

    if entreeChoice < 0 or entreeChoice > 3:
        print(" ")
        print("Sorry, po. please try again!")
        continue
    elif entreeChoice == 1 or entreeChoice == 2:
        print(" ")
        riceSize = input(
            "Would you like to upgrade your rice to Adobo fried rice? (Y/N) ")
        if riceSize == "Y" or riceSize == "y":
            print("Adding \"Adobo fried rice\" to order...")
            break
        elif riceSize == "N" or riceSize == "n":
            print(
                "Okay, po! That's fine. You can always add it later to your order."
            )
            break
    elif entreeChoice == 3:
        frySize = input(
            "Would you like to supersize your fries from small to large? (Y/N) "
        )
        if frySize == "Y" or frySize == "y":
            print("Adding \"Large fries\" to order...")
            break
        elif frySize == "N" or frySize == "n":
            print(
                "Okay, po! That's fine.")
            break
            "Would you like to supersize your fries from small to large? (Y/N) "
        if frySize == "Y" or frySize == "y":
            print(" ")
            print("Adding \"Large fries\" to order...")
            break
        elif frySize == "N" or frySize == "n":
            print(
                "Okay, po! That's fine. You can always add it later to your order. "
            )
            break

while True:
    print(" ")
    drinkChoice = input(
        """Now for your drink, would you like soda, water, or a specialty drink? (Please type in the full name of your choice and type N/A if you don't want a drink.)

Selection: """
    )

    if drinkChoice == "soda" or drinkChoice == "water":
        print("Pick up your cup at the counter with your meal!")
    elif drinkChoice == "specialty drink":
      drinkChoice == int(input("""What drink would you like? (Please use 1, 2, 3, or 4)
1. Iced Tea [$1.19]
2. Pineapple Juice []
3. Coffee
4. Soda float

Make your selection here: """))
      if drinkChoice == 1:
        print(" ")
        print("Adding \"Iced Tea\" to order...")
        break
      elif drinkChoice == 2:
        print(" ")
        print("Adding \"Pineapple Juice\" to order...")
        break
      elif drinkChoice == 3:
        print(" ")
        print("Adding \"Coffee\" to order...")
        break
      elif(drinkChoice == 4):
        print(" ")
        floatFlavor = input("What flavor would you like? Royal or Coke?")
        if floatFlavor == "coke" or floatFlavor == "Coke":
          print(" ")
          print("Adding \"Coke Soda Float\" to order...")
          break
        elif floatFlavor == "royal" or floatFlavor == "Royal":
          print(" ")
          print("Adding \"Royal Soda Float\" to order...")
          break
        else:
          print("Please choose a flavor.")
          print(" ")
          continue
      else:
        print("Please choose a flavor or type N/A.")
        print(" ")
        continue
    elif drinkChoice == "N/A" or drinkChoice == "n/a" or drinkChoice == "NA" or drinkChoice == "na":
      break
    else:
      print("Please choose a drink or type N/A.")
      continue

while True:
  print(" ")
  packetType= int(input("""What kind of sauce would you like? (Please type in the name.)
  
- Gravy [$0.55/2oz.]
- Ketchup [$0.25/packet]

Make your selection: """))

  packetAmount= float(input("""How many would you like? 

Make your selection: """))

  
  