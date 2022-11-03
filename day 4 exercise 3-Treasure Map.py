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

#Write your code below this line 👇
#Users choice
import random 
options = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice1 = int(user_choice)
output = options[user_choice1]
print(output)
#Computers random choice
computer_choice = random.choice(options)
print(computer_choice)
if output == computer_choice:
  print("It is a tie!")
if output == 0:
  if computer_choice == 1:
    print("Computer Wins!")
  elif computer_choice == 2:
    print("Human Wins!")
  else:
    print("What is going on bruh")
if output == 1:
  if computer_choice == 0:
    print("Human Wins!")
  elif computer_choice == 2:
    print("Computer Wins!")
  else:
    print("What is going on bruh")
if output == 2:
  if computer_choice == 0:
    print("Computer Wins!")
  elif computer_choice == 1:
    print("Human Wins")
  else:
    print("What is going on bruh")
    
