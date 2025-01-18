# Tasks:
# Tuple Unpacking
# Create a program where you define a tuple with 5 elements and unpack its values into individual variables. Print each variable.
# Example Tuple: (10, 20, 30, 40, 50)

my_turple = (10, 20, 30, 40, 50)

(a, b, c, d, e) = my_turple

print(f"a: {a} ")
print(f"b: {b} ")
print(f"c: {c} ")
print(f"d: {d} ")
print(f"e: {e} ")


# Count Unique Elements in a List
# Write a program that converts a list into a set to count the number of unique elements in the list.
# Example Input: [1, 2, 3, 2, 1, 5, 6, 3]
# Output: Number of unique elements: 5

my_elements = [1, 2, 3, 2, 1, 5, 6, 3]

unique_elements = set(my_elements)

length_of_unique_elements = len(unique_elements)

print(length_of_unique_elements)

print(unique_elements)

print(f"Number of unique elements: {length_of_unique_elements}")

# Set Operations
# Create two sets and perform the following operations:

# Union of the sets.
# Intersection of the sets.
# Difference between the two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"The union between these two set is : {set1 | set2}")
print(f"The Intersection between these two set is : {set1 & set2}")
print(f"The Difference between these two set is : {set1 - set2}")

# Find Common Elements Between Two Lists Using Sets
# Convert two lists into sets and find their common elements using set intersection.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

newset1 = set(list1)
newset2 = set(list2)

print(f"The Intersection between these two set is : {newset1 & newset2}")

# Find All Duplicates in a List Using Sets
# Write a program that identifies and prints all the duplicate elements in a list.
# Example Input: [1, 2, 3, 2, 4, 1, 5]
# Output: Duplicates: {1, 2}

s_set = [1, 2, 3, 2, 4, 1, 5]
seen = set()
duplicate = set()

for item in s_set:
    if item in seen:
        duplicate.add(item)
    else:
        seen.add(item)
print(duplicate)