# Day 6 Tasks: Strings & File Handling
# Today, let’s explore strings and basic file handling! Here are your tasks, gradually increasing in complexity

# Task 1: Count Words in a String
# Write a Python function that takes a string and counts how many words it contains.

# Hint: Use the split() method to break the string into a list of words.

def word_counter():
    string = "Hppy day bro how have you been"
    splited_word = string.split()

    print(len(splited_word))

word_counter()

# Task 1: Count Word Occurrences in a Sentence
# Write a program that:

# Accepts a sentence from the user.
# Counts how many times each word appears.
# Outputs the results in a dictionary where the keys are words and the values are their counts.
# Hint: Use the split() method to split the sentence into words, then loop through the words to count them.

from collections import Counter

word_list = []

sentence = input("Enter the sentence: ").split()

for word in sentence:
    word_list = sentence
print(word_list)

freq_word = Counter(word_list)

print(freq_word)

# Task 2: Merge Two Dictionaries
# Write a program that:

# Creates two dictionaries with some sample key-value pairs.
# Merges them into a single dictionary.
# Hint: Use the update() method to combine dictionaries.

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'e': 5, 'f': 6, 'g': 7, 'h': 8}

dict1.update(dict2)

print(dict1)

# Task 3: Nested Dictionary
# Create a program that stores information about 3 students in a dictionary. Each student should have:

# Name

# Age

# A dictionary of their scores in 3 subjects.

students = {
    "Student1": {"Name": "Alice", "Age": 15, "Scores": {"Math": 80, "English": 75, "Science": 90}},
    "Student2": {"Name": "Bob", "Age": 16, "Scores": {"Math": 85, "English": 70, "Science": 80}},
    "Student3": {"Name": "Charlie", "Age": 15, "Scores": {"Math": 78, "English": 88, "Science": 85}}
}

for student_key, student_details in students.items():
    print(f"Student: {student_key}")
    print(f"Name: {student_details['Name']}")
    print(f"Age: {student_details['Age']}")
    print(f"Scores: {student_details['Scores']}") 
    print()


# Task 4: Invert a Dictionary
# Write a program that takes a dictionary where the keys are unique, inverts it, and creates a new dictionary where the values become the keys.

# Example: Input: {"a": 1, "b": 2, "c": 3}
# Output: {1: "a", 2: "b", 3: "c"}

normal_dict = {"a": 1, "b": 2, "c": 3}

inverted_dict = {value: key for key, value in normal_dict.items()}
print("Original Dictionary:", normal_dict)
print("Inverted Dictionary:", inverted_dict)

# Task 5: Frequency Counter
# Write a function that takes a list of numbers and returns a dictionary where:

# Keys are the unique numbers in the list.

# Values are their frequency of occurrence.

# Example: Input: [1, 2, 2, 3, 3, 3, 4]
# Output: {1: 1, 2: 2, 3: 3, 4: 1}

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency_dict = {}
for num in numbers:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1

# Printing the result
print("Input List:", numbers)
print("Frequency Dictionary:", frequency_dict)
