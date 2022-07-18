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
images = [rock, paper, scissors]
print('What you want to choose ? press 0 for rock , press 1 for paper , press 2 for scissor .')

print("Choosing of invalid value lets computer wins !")
# user selection for choices

userChoice = int(input('Enter your choice \n'))
if userChoice == 0:
    print("user choose rock.")
    print(rock)
elif userChoice == 1:
    print('user choose paper.')
    print(paper)
elif userChoice == 2:
    print("user choose scissor.")
    print(scissors)
else:
    print("please select form given values !")

# computer random selection of choice
computerChoice = random.randint(0, 2)
if computerChoice == 0:
    print("computer choose rock.")
    print(rock)
elif computerChoice == 1:
    print('computer choose paper.')
    print(paper)
elif computerChoice == 2:
    print("computer choose scissor.")
    print(scissors)


# select the winner

if userChoice == 0 and computerChoice == 2:
    print('You Win !')
    print(images[userChoice])
elif computerChoice == 0 and userChoice == 2:
    print("You loose !")
    print(images[computerChoice])
elif userChoice == 0 and computerChoice == 1:
    print('You Win !')
    print(images[userChoice])
elif userChoice > computerChoice:
    print("You Win !")
    print(images[userChoice])
elif computerChoice > userChoice:
    print('You Loose')
    print(images[computerChoice])
elif userChoice == computerChoice:
    print('Draw')
