

# Import the 'random' module for generating random character.
import random

# Define character sets for password generation.
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&()[]{}|\;:<>,.?"

# Combine all character sets to form the complete set of characters for the password.
all_characters = lower_case + upper_case + numbers + symbols

# Set the desired length of the password.
length = 10

# Generate a random password by sampling characters from the complete set.
password = "".join(random.sample(all_characters, length))

# Print the generated password.
print(password)


