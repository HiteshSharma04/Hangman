import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
from words import word_list
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
def Opt():
  Option = input("Want to Play Again?(Y/N): ")
  if Option == "y" or Option == "Y":
    Hangman()
  else:
    print("Game Over!") 

def Hangman():                                                     
  print(logo)
  chosen_word = random.choice(word_list)
  height = len(chosen_word)
  lives = 6
  finish = False

  display = []
  for _ in range(height): 
    display += "_"
    

  while not finish:

    print(display)
    user = input("enter a letter: ").lower()
    clear()
    if user in chosen_word:
      for i in range(height):
        letter = chosen_word[i]
        if letter == user:
          display[i] = letter
    else:
      lives -= 1
      print(f"You have lose one live. now you have only {lives} lives")
    if lives == 0:
      finish = True
      print("You Loose!")
      print(f"Word is {chosen_word}!")
    if "_" not in display:
      finish = True
      print("You Win!")
    print(stages[lives])
  Opt()

        
def menu():
  Start = input("Want To Start Game?(Y/N): ")
  if Start == "y" or Start =="Y":
    Hangman()
  else:
    Print("Closing Game!")
menu()

