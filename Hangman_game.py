import random

word_list = ["cherry","apple",'strawberry']
rnd_wrd = word_list[random.randint(0,2)]
print(rnd_wrd)

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

placeholder = ""
for position in range(len(rnd_wrd)):
    placeholder += "_"
print(placeholder)

#list variable to accumulate the right guesses
correct_list = []

Game_over = 'False'
life = 6
while Game_over=='False':
    #ask your user to guess a letter
    user_guess = input("Guess your letter: ").lower()
    #check the guess letter on your random word with a loop and replace it with the letter with underscore
    check_wrd = ""
    for letter in rnd_wrd:
        if letter == user_guess:
            check_wrd += user_guess
            correct_list.append(user_guess)
        elif letter in correct_list:
            check_wrd += letter
        else:
            check_wrd += "_"
#separate block to check correct word selection and on the life
    if user_guess in correct_list and life != 0:
        Game_over = 'False'
#if not right word then reduce life by 1 and check life is not over
    elif user_guess not in correct_list and life != 0:
        life -= 1
        print(HANGMANPICS[5-life])
#if life is over
    elif life == 0:
        Game_over = 'True'
        print("You lose!")
        print(HANGMANPICS[6])
    else:
        Game_over = 'True'
        print(f"Bravo!!! The word is: {check_wrd}")
    print(check_wrd)
print("Thanks for playing!!")
