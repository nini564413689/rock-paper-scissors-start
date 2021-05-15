rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

uchoose = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
types = [rock, paper, scissors]

print(f"You choose {types[uchoose]}")
# computer_choose = random.choice(types)  
rand_inx = random.randint(0,2)
computer_choose = types [rand_inx]
print(f"Computer choose {computer_choose}")

if uchoose == rand_inx:
    print("Draw")
elif uchoose == 0:
    if rand_inx == 1:
        print("You lose")
    else:
        print("You Win!!!")

elif uchoose == 1:
    if rand_inx == 2:
        print("You lose")
    else:
        print("You Win!!!")

elif uchoose == 2:
    if rand_inx == 0:
        print("You lose")
    else:
        print("You Win!!!")
