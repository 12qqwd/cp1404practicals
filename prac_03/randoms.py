import random

# Line 1: Random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))
# Possible values: 5 to 20 (inclusive)
# Smallest number: 5
# Largest number: 20

# Line 2: Random odd number between 3 and 9 (range(3, 10, 2))
print(random.randrange(3, 10, 2))
# Possible values: 3, 5, 7, 9
# Smallest number: 3
# Largest number: 9
# Could it produce a 4? No, because step=2 and starts at 3 → only odd numbers

# Line 3: Random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))
# Possible values: Any float between 2.5 and 5.5 (inclusive on both ends)
# Smallest number: 2.5
# Largest number: 5.5

# Generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
