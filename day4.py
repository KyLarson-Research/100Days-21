#Authored By Kyle Larson 10-2-21
import random
computer_choice = random.randrange(3)
user_choice = input("Rock, Paper, Scisors")
if computer_choice == user_choice +1:
	print("computer wins")
else:
	print("user wins")