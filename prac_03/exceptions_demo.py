try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print(f"{numerator} / {denominator} is {result}")
# Answers to the questions:
# Q1: When will a ValueError occur?
# A ValueError occurs if the user enters something that cannot be converted to an integer,
# such as a string like "abc" or a blank input.

# Q2: When will a ZeroDivisionError occur?
# A ZeroDivisionError happens if the user enters 0 as the denominator,
# because dividing by zero is not allowed in mathematics or Python.

# Q3: Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, you can check if the denominator is zero before attempting the division.
# Updated version with ZeroDivisionError prevention:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero.")
    else:
        result = numerator / denominator
        print(f"{numerator} / {denominator} is {result}")
except ValueError:
    print("You must enter a valid integer.")
