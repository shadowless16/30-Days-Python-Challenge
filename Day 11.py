# Day 11: File Handling
# Challenge Breakdown
# Objective: Write a Python program to read a text file and count:
# Number of lines.
# Number of words.
# Number of characters.

with open("Day 2.py", "r") as file:
    lines = len(file.readlines())
    print(lines)

number_of_words = 0

with open("Day 5.py", "r") as file2:
    words = file2.read()
    lines2 = words.split()
    number_of_words += len(lines2)
print(number_of_words)

def counter(fname):
    number_of_character = 0

    with open(fname, "r") as file3:
        for i in file3:
            if(i != " " and  i != "\n"):
                number_of_character += 1

    print('Number of characters in text file: ', {number_of_character})

# Driver Code:
if __name__ == '__main__':
    fname = 'Day 3.py'
    try:
        counter(fname)
    except FileNotFoundError:
        print('File not found')