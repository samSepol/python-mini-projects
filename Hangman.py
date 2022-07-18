# Step 1
import random
from logo import logo, stages
from words import word_list
# word_list = ["bmw", "tesla", "ferrari", "audi",
#              "steve", "bill", "mark", "elon", "jeff"]

print(logo)


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

ChosenWord = random.choice(word_list)
# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
# word_length = len(ChosenWord)
for _ in ChosenWord:
    display += "_"
# print(display)
# print(ChosenWord)

game_over = False
no_of_lives = 6
while game_over != True and no_of_lives != 0:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess_letter = input("Guess the letter ! ").lower()
    if guess_letter not in ChosenWord:
        no_of_lives -= 1
        print(f'remaining chances are {no_of_lives}')


# for position in range(word_length):
# display grid of list
    for position in range(len(ChosenWord)):
        letter = ChosenWord[position]
        if letter == guess_letter:
            display[position] = letter
    print(display)

    if "_" not in display:
        game_over = True
        print(f"You Win ! The word is {ChosenWord}")
    elif no_of_lives == 0:
        print(f'You loose ! The word was {ChosenWord}')
    print(stages[no_of_lives])
