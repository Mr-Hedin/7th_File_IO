"""
Lesson 2: Reading Lines and Removing Whitespace
Learn how to read files line by line and clean up the text.
"""

# Create a sample file with multiple lines
# Some of the lines have extra spaces
with open("grocery_list.txt", "w") as file:
    file.write("Apples   \n")
    file.write("  Bananas\n")
    file.write("Oranges  \n")
    file.write("  Milk   \n")

# Read the file line by line
print("Reading lines with extra spaces:")
file = open("grocery_list.txt", "r")

# Use a for loop to read each line
for line in file:
    print(f"Original: '{line}'")
    clean_line = line.strip()
    print(f"Cleaned: '{clean_line}'")
    print()

file.close()

# Practice Exercise:
input("\nPress Enter to practice reading lines...")

print("\nTo read a file line by line, you can use a for loop:")
print("1. Open the grocery_list.txt file")
print("2. Read each line")
print("3. Remove extra spaces with strip()")
print("4. Print the clean lines")
print("5. Close the file") 