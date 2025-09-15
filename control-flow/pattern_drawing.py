# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while) for rows
while row < size:
    # Inner loop (for) for columns
    for col in range(size):
        print("*", end="")  # Print stars on the same line
    print()  # Move to the next line after each row
    row += 1
