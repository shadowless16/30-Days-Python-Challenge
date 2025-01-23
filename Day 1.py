import time

# Task 1: Age Calculator
# Write a program that:

# Asks the user for their birth year.
# Calculates their age based on the current year.
# Tells them their age and if they’re a minor (under 18) or an adult.

print("========== Welcome The Age Calculator Program ========== ")
user_birth_year = int(input("Enter Your Birth Year: "))

age = 2025 - user_birth_year

if age >= 18:
    print(f"You are {age} years old so you are an adult adult")
else:
    print(f"You are {age} years old so you are still a minor")


time.sleep(2)

# Task 2: Temperature Converter
# Write a program that:

# Asks the user to input a temperature in Celsius.
# Converts it to Fahrenheit using the formula: F = (C × 9/5) + 32.
# Prints the result.

print("========== Welcome The Temperature Converter Program ========== ")
temp_in_celsius = int(input("Enter the temperature in celsius: "))

conversion = (temp_in_celsius * 9/5) + 32

print(f"{temp_in_celsius}° is equal to {conversion}° ")

time.sleep(2)

# Task 3: Tip Calculator
# Write a program that:

# Asks for the total bill amount.
# Asks for the tip percentage (e.g., 10%, 15%).
# Calculates the tip amount and the total amount to be paid.

total_bill_amount = int(input("Enter the total bill: "))
tip_percentage = int(input("Enter the tip amount: "))
tip_amount = total_bill_amount * tip_percentage / 100

print(f"This your receipt \n The Total bill is: {total_bill_amount} and the Tip amount {tip_amount}")

# Task 4: Digit Sum Calculator
# Write a program that:

# Takes a positive integer as input.
# Calculates and prints the sum of its digits.

number = (input("Enter Number: "))
total = 0

for digit in number:
    total += int(digit)
print(f"The sum of the digits is, {total}")

# Task 5: Time Converter
# Write a program that:

# Asks the user for a time in seconds.
# Converts it into hours, minutes, and seconds.

total_seconds = int(input("Enter time in seconds: "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{total_seconds} seconds is equal to {hours} hour(s), {minutes} minute(s), and {seconds} second(s).")