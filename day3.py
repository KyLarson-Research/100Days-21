#Authored on 9-30-21 by Kyle Larson
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
road = input("Two roads diverge in a yellow wood, and you cannot not travel both. You look down one to where it bends in the undergrowth. Do you take the well worn road or grassy road?")
if(road != "grassy"):
    print("you fall into a pit of spikes/aligators/parahnas/sharks/electric eels/snapping turtles/angy hippos/naked nuclear fuel cells/spinning blades and mines. Game Over.")
else:
    lake = input("You come to a lake. There are hundreds of dead bodies in the lake and dumbeldoor gives you the option to swim or take the boat. Do you swim or boat?")
    if(lake != "swim"):
        print("the lady of the lake orders the hundreds of dead bodies to attack you! you are slowly drowned and become another of the zombies serving the aurthurian lady of the lake. Game Over.")
    else:
        island = input("you arrive at an island. Just inside the treeline is a massive glass dome filled with what look to be vastly diverse arrays of flowering trees and vegitation. Next to a broken pannel, a chrome door and a garage seem to be ways of getting inside. How do you chose to enter the dome?")
        if(island != "broken pannel"):
            print("You enter and notice a spicy sweet smell. Being hungry you take a few steps to trace its origin and you find that your feet are sticking to the ground. you look down to see roots growing out of the bottoms of your shoes. Your scream cuts off as your entire body transforms into a tree.")
        else:
            print("inside the dome you ignore the temptation to inhale unsure of the shining fog which hovers. you hold your breath long enough to glimpse a laptop with the image of the above chest set to the wallpaper. You scoop up the laptop and run. Once home you find the hard drive filled with all the music. ")                                   
            


#https://www.draw.io/?#lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2#F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload