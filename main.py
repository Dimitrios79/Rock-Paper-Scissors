import random

choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice1 == 0:
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
if choice1 == 1:
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
if choice1 == 2:
  print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

print(choice1)
choice2 = random.randint(0,2)
if choice2 == 0:
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
if choice2 == 1:
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
if choice2 == 2:
  print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print(choice2)

if choice1 == 0 and choice2 == 1:
  print("You lose from computer")
elif choice1 == 0 and choice2 == 0:
  print("It is draw.")
elif choice1 == 0 and choice2 == 2:
  print("You win.")
elif choice1 == 1 and choice2 == 1:
  print("It is draw.")
elif choice1 == 1 and choice2 == 2:
  print("You lose from computer.")
elif choice1 == 1 and choice2 == 0:
  print("You win.")
elif choice1 == 2 and choice2 == 2:
  print("It is draw.")
elif choice1 == 2 and choice2 == 0:
  print("You lose from computer.")
elif choice1 == 2 and choice2 == 1:
  print("You win.")