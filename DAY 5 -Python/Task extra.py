# Ask for user's name
name = input("Please enter your name: ")
# Calculate the number of letters in the name
num_letters = len(name)
# Print the number of letters
print("Your name has", num_letters, "letters.")
# Create a dictionary to store the count of each letter
letter_counts = {}
# Count the number of occurrences of each letter
for letter in name:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1
# Check if any letters have duplicates
has_duplicate = False
for letter, count in letter_counts.items():
    if count > 1:
        has_duplicate = True
        print("The letter '{}' appears {} times.".format(letter, count))
# Print the result of the check for duplicate letters
if has_duplicate:
    print("Your name has duplicate letters.")
else:
    print("Your name does not have any duplicate letters.")
    print("Your name does not have any duplicate letters.")