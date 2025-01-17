# Day 4: Lists
# Today's Focus
# Creating and modifying lists.
# List methods (append(), remove(), sort(), etc.).
# Slicing and iterating through list

# Tasks
# Sum of a List
# Write a program that calculates the sum of all numbers in a list.
# Example Input: [2, 4, 6, 8]
# Example Output: 20

list_number = [2, 4, 6, 8, 10]

print(sum(list_number))

# Largest and Smallest Numbers
# Write a program that finds the largest and smallest numbers in a list.
# Example Input: [15, 28, 3, 9, 42]
# Example Output:

# Largest: 42
# Smallest: 3

list_number2 = [15, 28, 3, 9, 42]

max_no = max(list_number2)
min_no = min(list_number2)

print(f"The max no. is: {max_no}")
print(f"The min no. is: {min_no}")

# Count Occurrences
# Write a program to count how many times a specific value appears in a list.
# Example Input: List: [2, 4, 6, 4, 9, 4], Value: 4
# Example Output: 4 appears 3 times

list_number3 = [2, 4, 6, 4, 9, 4].count(4)

print(f"4 appears {list_number3} times")

# Remove Duplicates
# Write a program to remove all duplicate values from a list.
# Example Input: [1, 2, 3, 2, 4, 1, 5]
# Example Output: [1, 2, 3, 4, 5]

list_number4 = [1, 2, 3, 2, 4, 1, 5]

list_number4 = list(set(list_number4))

print(list_number4)

# OR
a = list(dict.fromkeys(list_number4))
print(list_number4)

# Sort a List
# Write a program to sort a list in ascending order.
# Example Input: [3, 1, 4, 1, 5, 9]
# Example Output: [1, 1, 3, 4, 5, 9]

list_number5 = [3, 1, 4, 1, 5, 9]

list_number5.sort()

print(list_number5)