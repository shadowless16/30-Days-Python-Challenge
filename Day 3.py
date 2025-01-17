# 1. String Manipulation
# Write a program that:

# Takes a sentence as input.
# Converts it to uppercase.
# Replaces all spaces with hyphens (-).
# Prints the final result.

sentence = "python is fun"
sentence_upper = sentence.upper()

print(sentence_upper.replace(" ", "-"))

# 2. Palindrome Checker
# Write a program that:

# Asks the user for a word.
# Checks if the word is a palindrome (a word that reads the same backward as forward).
# Prints True or False.

word = input("Enter word: ")

# check word against it's reverse
if word == word[::-1]:
    print(f"{word} is a Palindrome")
else:
    print(f"{word} isn't a Palindrome")

# 3. Word Counter
# Write a program that:

# Accepts a sentence from the user.
# Counts the number of words in the sentence.

sentence2 = input("Enter the sentence: ")

print(f"Number of words: {len(sentence2.split())}")

# 4. Vowel and Consonant Counter
# Write a program that:

# Accepts a sentence from the user.
# Counts and prints the number of vowels (a, e, i, o, u) and consonants in the sentence.

sentence3 = input("Enter sentence: ")

vowels =  "aeiouAEIOU"
vowel_counter = 0
consonant_counter = 0

for char in sentence3:
    if char.isalpha():
        if char in vowels:
            vowel_counter += 1
        else:
            consonant_counter += 1
print(f"The are {vowel_counter} vowels")
print(f"The are {consonant_counter} consonants")


# Challenge 2: Word Frequency Counter
# Write a program that counts the frequency of each word in a user-inputted sentence.

# Steps:
# Get a sentence input from the user.
# Split the sentence into words.
# Use a dictionary to count occurrences of each word.
# Display the frequency of each word
from collections import Counter

word_list = []

sentence4 = input("Enter sentence: ").split()

for i in sentence4:
    word_list = sentence4
print(word_list)


a  = Counter(word_list)

print(a)

# Question 1: Find the Longest Word
# Write a program that asks the user to input a sentence and determines the longest word in the sentence.

word_list2 = []

word = input("Enter word: ").split()

longest = max(word, key=len)

print(f"The longest word is: '{longest}'")
print(f"Its length is: {len(longest)} characters.")


# print(len(max(word_list2)))