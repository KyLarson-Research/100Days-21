#Authored by Kyle Larson 9-30
print('Welcome to the tip calculator.')
bill =input("What was the total bill?")
people = input("How many people to split the bill?")
percentage = input("WHat percentatge tip would you like to give?")
if int(percentage) < 0 or int(percentage) > 100:
      print("invalid percentage")
else:
      pay = ( float(bill)*(1+int(percentage)/100) )/int(people)
      print("Each person should pay: ", round(pay,2) )
      