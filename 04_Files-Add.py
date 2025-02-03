"""
Lesson 4: Adding to Files
Learn how to add new content to existing files.
"""

# Create a daily log file
with open("daily_log.txt", "w") as file:
    file.write("Monday: Learned about file reading\n")

# Show the original content
print("Original file contents:")
with open("daily_log.txt", "r") as file:
    print(file.read())

# Append new content to the file
print("\nAppending new content...")
with open("daily_log.txt", "a") as file:
    file.write("Tuesday: Learned about file writing\n")
    file.write("Wednesday: Learned about appending\n")

# Show the updated content
print("\nUpdated file contents:")
with open("daily_log.txt", "r") as file:
    print(file.read())

# Practice Exercise:
input("\nPress Enter to practice appending...")

print("\nYour turn! Try to:")
print("1. Open daily_log.txt in append mode ('a')")
print("2. Add an entry for Thursday")
print("3. Close the file")
print("4. Open and read the file to see your changes") 