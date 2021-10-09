#Authored by Kyle Larson 10-5-21
import random as rand

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#The Above Courtesy of https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
index_of_new_word = rand.randint(0, len(words))
HANGI = 0
hangman_wordish = words[index_of_new_word]
letter_index = 0
num_correct_letters =0
while(HANGI<len(HANGMANPICS)):
    guess = input("Enter guess ")
    output=[]
    letter_index=0
    for letter in hangman_wordish:
        if letter==guess:
            output.append(" "+guess+ " ")
            letter_index = letter_index +1
            num_correct_letters = num_correct_letters+1
        else: 
            output.append(' _ ')
    if letter_index>0:
        out =""
        out = out.join(output)
        print(out)
    else:
        HANGI=HANGI+1
        print(HANGMANPICS[HANGI])
        
    if HANGI == len(HANGMANPICS) or num_correct_letters == len(hangman_wordish):
        break
if num_correct_letters == len(hangman_wordish):
    print("Congradulations!")
else:
    print("Game over. You lose.")