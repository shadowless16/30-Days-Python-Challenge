# Task 1: Number Classification
# Write a program to classify a number as positive, negative, or zero using if, elif, and else.

number = -3

if number == 0:
    print("This is 0")
elif number > 0:
    print("Positive")
else:
    print("Negative")

# Task 2: Age Checker
# Write a program that:

# Takes a person's age as input.
# Prints:
# "Child" if the age is less than 13.
# "Teenager" if the age is between 13 and 19.
# "Adult" if the age is 20 or above.

person_age = 15

if person_age < 13:
    print("You are still a child")
elif person_age >= 13 and person_age <= 19:
    print("You are a Teenager")
else:
    print("You are an adult")

# Task: Nested Conditionals with Age and Exam Eligibility
# Write a program that determines whether a person is eligible to sit for an exam based on these conditions:

# The person must be at least 18 years old.
# If they are 18–25 years old, they must provide a valid ID to be eligible.
# If they are above 25 years old:
# If their age is 26–30, they must have a previous exam score of 60% or higher to qualify.
# If they are above 30, they are automatically eligible regardless of previous scores.
# For ages below 18, print: "You are too young to take the exam."

age = 29
if age >= 18:
    if age < 26:
        print("You are welcome")
        print("Please provide your ID")
        print("You are qualified")
    elif age < 31:
        exam_score = int(input("Please enter your previous exam score: "))
        if exam_score > 60:
            print("You are qualified")
        else:
            print("You are not qualified")
    else:
        if age >= 30:
            print("Automatically eligible")   
else:
    print("You are too young to take the exam")
   
# Task: Grading System with Bonus Points
# Write a program to calculate a student's final grade based on their score and bonus points. Use the following conditions:

# If the score is 90 or above:

# Add 5 bonus points.
# If the final score exceeds 100, cap it at 100.
# If the score is between 70 and 89:

# Add 3 bonus points.
# If the score is between 50 and 69:

# Add 2 bonus points.
# If the score is below 50:

# No bonus points are added.
# Print "Failed."
# Finally, print the student's final grade.

score = 97

if score >= 90:
    score += 5
    if score > 100:
        score = 100
    else:
        pass
    print(score)
    print(f"Final score {score}")
elif score >= 70 and score <= 89:
    score += 3 
    print(score)
    print(f"Final score {score}")
elif score >= 50 and score <= 60:
    score += 2
    print(score)
    print(f"Final score {score}")
else:
    print("No bonus points are added.")
    print("Failed")
    print(f"Final score {score}")