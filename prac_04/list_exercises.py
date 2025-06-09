# Part 1: Basic list operations

# Prompt the user for 5 numbers and store them in a list
numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Output the required statistics
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Part 2: Woefully inadequate security checker

usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
]

# Ask the user for their username
entered_username = input("Username: ")

# Check if the entered username is in the list
if entered_username in usernames:
    print("Access granted")
else:
    print("Access denied")
