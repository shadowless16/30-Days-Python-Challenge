#opening a file
file = open("Additonal Challenges.py", "r")

print(file)

#reading a file

file1 = open("Day 1.py", "r")
content = file.read() #reads the whole
# line = file.readline() #reads line by line
print(content)

file2 = open("file.txt", "w")
file2.write("Hello, Ak!")
file2.close()

# Using the with Statement
# Instead of manually opening and closing files, you can use the with statement. It automatically closes the file for you.

with open("file.txt", "r") as file:
    file_content = file.read()
    print(file_content)

# Example 2: Writing to a File
# python
# Copy code

# with open("file.txt")
