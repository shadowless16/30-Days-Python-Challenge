# Day 2 Challenge
# 1. Reverse a String
# Write a program that:

# Takes a string input from the user.
# Reverses the string and prints it.

word = input("Enter the word: ")

reversed_string = ''.join(reversed(word))

print(reversed_string)

# 2. Find the Largest Number
# Write a program that:

# Takes three numbers as input.
# Determines and prints the largest number.

group_number = {}


while True:
    choice = input("Pres A to input /n B to stop: ")

    if choice == "a":
        group_number = input("Enter number: ")
    elif choice == "b":
        break

for digits in group_number:
    print(max(digits))


# 3. Check if a Number is Even or Odd
# Write a program that:

# Takes an integer as input.
# Checks whether the number is even or odd and prints the result.

number = int(input("Enter number: "))

if number % 2 == 0:
    print("even number")
elif number % 2 == 1:
    print(f"{number} odd number")

# 4. Generate Multiplication Table
# Write a program that:

# Accepts an integer input.
# Prints the multiplication table for that number from 1 to 10.

multiplication_number = int(input("Enter number: "))

for multiplication_number_digit in range(1, 13):
    print(f"{multiplication_number} x {multiplication_number_digit} = {multiplication_number * multiplication_number_digit}")

# 5. Basic Calculator
# Write a program that:

# Asks the user for two numbers.
# Asks the user to choose an operation: +, -, *, or /.
# Performs the chosen operation and displays the result.

print("======== Welcome to the basic calculator program =========")

while True:
    
    choice2 = input("Would you like to use \n A to continue \n B to stop: \n ").upper()

    if choice2 == "A":
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))

        operator = input("Which operation would like to perform: ")

        if operator == "+":
            print(f"{first_number} + {second_number} = {first_number + second_number}")
        elif operator == "-":
            print(f"{first_number} - {second_number} = {first_number - second_number}")
        elif operator == "x":
            print(f"{first_number} x {second_number} = {first_number * second_number}")
        elif operator == "/":
            print(f"{first_number} / {second_number} = {first_number + second_number}")
        else:
            print("Invalid Operator")

        # print(f"{first_number} {operator} {second_number}")

    elif choice2 == "B":
        break


