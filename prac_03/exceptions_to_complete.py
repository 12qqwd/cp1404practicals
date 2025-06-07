# exceptions_to_complete.py

# Loop until the user enters a valid integer
is_valid_input = False

while not is_valid_input:
    try:
        result = int(input("Enter a valid integer: "))  # Try to get and convert input
        is_valid_input = True  # If successful, exit loop
    except ValueError:  # If input is not a valid integer
        print("Please enter a valid integer.")  # Error message

# Print the result after valid input is received
print(f"Valid result is: {result}")
