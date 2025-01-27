# Day 12 Task: Division with Exception Handling
# Task Details
# Write a program that:

# Prompts the user to enter two numbers.
# Attempts to divide the first number by the second.
# Handles the following exceptions:
# Division by zero.
# Invalid input (non-numeric values).
# Always prints a message indicating that the program has finished execution (using the finally block).



def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    
    finally:
        print("Program execution finished.")

divide_numbers()
