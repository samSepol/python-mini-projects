import random
from guess import logo
print("Welcome to the Number Guessing Game! ")
print("Think of a number between 1 and 100")

number = random.randint(1, 100)
print(number)

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game():
    print(logo)

    if game_level == 'easy':
        no_of_lives = 10
        print(f"You have {no_of_lives} lives")
    else:
        no_of_lives = 5
        print(f"You have {no_of_lives} lives")

    game_over = False
    while not game_over and no_of_lives != 0:
        guess_number = int(input("Guess the number! "))
        if guess_number == number:
            print(
                f"You guess the number! with {no_of_lives} remaining lives. ")
            game_over = True
        elif guess_number < number:
            no_of_lives -= 1
            print(
                f"Your guess is low ! your no of lives remains {no_of_lives} ")

        elif guess_number > number:
            no_of_lives -= 1
            print(
                f"Your guess is high ! your no of lives remains {no_of_lives}")
        elif no_of_lives == 0:
            game_over = True
            print("No of lives over! You loose the game.")
    print(f"The number was {number}")


game()

while input("Do you want to restart the game: Type 'y' or type 'n' to quit: ") == 'y':
    game()


''' TODO:
1 : Add medium functionality
2 : make UI 
'''
