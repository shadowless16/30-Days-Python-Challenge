# Task
# Given an integer,n , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# n = 24

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2025))
print(calendar.isleap(2025))

import calendar

date_input = input()  

month, day, year = map(int, date_input.split())

day_of_week = calendar.weekday(year, month, day)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[day_of_week].upper())

import random
import time

while True:
    random_number = random.randint(1, 10)

    user_number = int(input("Enter ur number: "))

    if random_number > user_number:
        print("High")
        print(f"Random number: {random_number} \nUser number: {user_number}")
        time.sleep(1)
    elif random_number < user_number:
        print("Low")
        print(f"Random number: {random_number} \nUser number: {user_number}")
        time.sleep(1)
    elif random_number == user_number:
        print("Correct")
        print(f"Random number: {random_number} \nUser number: {user_number}")
        time.sleep(1)
        break