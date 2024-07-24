# Treasure Island
# learn nested if conditions

# Welcome
print("Welcome to Treasure Island")
print("Your mission is to find the treasure", end="\n")

# Condition Part 1
choice1 = input("You\'re at a crossroad, where do you want to go? Left path looks dangererous. Right path looks safe. L or R?. ").lower()
if choice1 == "l":
    choice2 = input("Treasure is in sight, would you like to get it? Y or N? ").lower()
    if choice2 == "n":
        choice3 = input("Path on the left looks slippery. Path on the right looks stable. L or R? ").lower()
        if choice3 == 'l':
            print("Very good, you are still on the correct path.")
            choice4 = input("You\'re now at a crossroad, step forward (Y) or backward? (N) ").lower()
            if choice4 == "y":
                print("You have found Treasure Island!")
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
        else:
            print("Game Over.") 
    else:
        print("Game Over.")      
else:
    print("Game Over.")