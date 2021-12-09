import random

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
print("Rock Paper Scissors")
variable = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if variable <= 3 and variable >= 0:
  choice_one = [rock,paper,scissors]
  print(choice_one[variable])

  print("Computer chose")

  choice_com = random.randrange(0,2)

  print(choice_one[choice_com])
  if variable == 0 :
    if choice_com == 0:
      print("It's Draw")
    elif choice_com == 1:
      print("You Lose")
    else:
      print("You Win")
  if variable == 1 :
    if choice_com == 1:
      print("It's Draw")
    elif choice_com == 2:
      print("You Lose")
    else:
      print("You Win")
  if variable == 2 :
    if choice_com == 2:
      print("It's Draw")
    elif choice_com == 0:
      print("You Lose")
    else:
      print("You Win")
else:
  print("You typed an invalid number, you lose")
