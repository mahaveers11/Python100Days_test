import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# get the user/player input:
player_var = input("Select your choice and input a number: 1. rock or 2. paper or 3. scissors - ")
player_int = int(player_var)

#creat a list of all variable inputs
rps_list = [rock, paper, scissors]

#generate a random input value of Computer
computer_ip = rps_list[random.randint(0,2)]

player_ip = rps_list[player_int-1]

print(f"Your option: \n {player_ip}")
print(f"Computer: \n {computer_ip}")

if player_ip == rock and computer_ip == scissors:
    print("You won!!")
elif player_ip == scissors and computer_ip == paper:
    print("You won!!")
elif player_ip == paper and computer_ip == rock:
    print("You won!!")
elif player_ip == scissors and computer_ip == rock:
    print("You lost!!")
elif player_ip == paper and computer_ip == scissors:
    print("You lost!!")
elif player_ip == rock and computer_ip == paper:
    print("You lost!!")
else:
    print("its a tie!!")




