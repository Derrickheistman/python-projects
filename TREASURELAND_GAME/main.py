print('''
 *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************   
''')
print("Welcome to Treasure Land.")
print("Your mission is to find the treasure.")

# First choice
Choice1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right": ').lower()
if Choice1 == "left":
    # Second choice
    Choice2 = input('You are at the river side. Do you want to "swim" or "wait" for a boat? ').lower()
    if Choice2 == "wait":
        # Third choice
        Choice3 = input(
            'You arrive safely at the island. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? ').lower()
        if Choice3 == "red":
            print("Burned by fire. Game Over.")
        elif Choice3 == "yellow":
            print("Congratulations! You found the treasure and won the game!")
        elif Choice3 == "blue":
            print("Eaten by a beast. Game Over.")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("You got attacked by a hungry shark. Game Over!")
else:
    print("You fell into a pit. Game Over.")
