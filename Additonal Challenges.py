# Challenge: Word Scramble Game
# Task
# Create a simple word scramble game using Python. The program should:

# Randomly select a word from a predefined list of words.
# Scramble the letters of the word.
# Display the scrambled word to the user.
# Allow the user to guess the original word.
# Provide feedback if the guess is correct or incorrect.
# Keep track of the number of attempts the user makes.

import random

word_list = ["python", "developer", "challenge", "algorithm", "programming"]

random_word = random.choice(word_list)
print(random_word)

shuffle = random.sample(random_word, 3)
shuffle2 = "".join(random.sample(random_word, len(random_word)))
print(shuffle2)

print(f"This the is the Scramble word {shuffle2} \nTry to unscramble it")

while True:
    attempt_counter = 0

    attempt_counter += 1

    guess_word = input("Enter you guess: ")

    if guess_word == random_word:
        print("Wow u guessed it")
        print(attempt_counter)
        break
    elif guess_word != random_word:
        print("Incorrect")

