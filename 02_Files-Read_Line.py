"""
Lesson 2: Reading Lines and Removing Whitespace
Learn how to read files line by line and clean up the text.
"""
with open("grocery_list.txt", "w") as file:
    file.write("Apples   \n")
    file.write("  Bananas\n")
    file.write("Oranges  \n")
    file.write("  Milk   \n")

# Read the file line by line
print("Reading lines with extra spaces:")

with open("grocery_list.txt", "r") as file:
    # Use a for loop to read each line
    for line in file:
        print("Original: ", line)
    # Reset the file pointer to the beginning!
    # The .seek() method is used to move the file pointer to a specific position in the file.   
    # In this case, we move the file pointer to the beginning of the file.
    file.seek(0)
    for line in file:
        clean_line = line.strip()
        print("Cleaned: ", clean_line)


# Try writing a function that uses .reverse() instead of .strip() and print the output!

# Practice Exercise:
input("\nPress Enter to practice reading lines...")

print("\nTo read a file line by line, you can use a for loop")
print("To output the text in a readable format we can use several string methods like .strip()")
print(".strip() removes extra spaces or newline characters at the end of a string, this can be extremely useful for formatting!")
print("Instructions:")
print("1. Open the grocery_list.txt file")
print("2. Read each line and print it")
print("3. Seek the start of the file to reset where we're at in the file")
print("4. Remove extra spaces and newlines with .strip()")
print("5. Print the clean lines")
