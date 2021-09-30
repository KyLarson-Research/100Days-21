#Authored_By_Kyle_"Kale"_Larson_9-29-21 
location =""
#Greeting
print("Welcome to the Band Name Generator! Answer a few questions for your band's name:")
location = input("Where are you from?\n")
print("Oh so you are from "+str(location))
pet = input("What is your pet's name?")
print("your pet is" + pet)
print("... and your band's name is  ")
shuffle_len = min([len(pet), len(location)])
bandName = ''
for i in range(shuffle_len):
    bandName = bandName + pet[i]+location[i]
print(bandName)