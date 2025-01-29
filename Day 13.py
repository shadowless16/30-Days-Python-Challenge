# ### **Day 13: List Comprehensions**
# - Syntax and examples.
# - Nested list comprehensions.
# - **Task:** Write a program to generate a list of squares for numbers 1–20 using list comprehensions.


squares = [x**2 for x in range(1, 21)]

# Print the result
print(squares)


# 1. Filtering Even Numbers
# Create a list of even numbers from 1 to 20:
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)


# 2. Squares of Even Numbers
# Square only the even numbers from 1 to 10:

squared_evens = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squared_evens)

# 3. Nested List Comprehension
# Generate a matrix with 3 rows, where each row contains the squares of numbers from 1 to 3:
matrix = [[x**2 for x in range(1, 4)] for _ in range(3)]
print(matrix)