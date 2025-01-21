# Base Task: Create a Multiplication Table for Numbers 1–12
# Write a program using nested loops to generate and display a multiplication table for numbers 1–12.

print("    ", end="") 
for i in range(1, 13):
    print(f"{i:4}", end="")
print("\n" + "-" * 52)

for row in range(1, 13):
    print(f"{row:2} |", end="") 
    for col in range(1, 13):  
        print(f"{row * col:4}", end="") 
    print()
