def factorial(n):
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    elif n == 0 or n == 1:
        return 1  # Base case
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Test the function
number = int(input("Enter a number to calculate its factorial: "))
fact = factorial(number)
if fact is not None:
    print(f"The factorial of {number} is {fact}.")
