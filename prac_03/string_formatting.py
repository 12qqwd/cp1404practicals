# String formatting examples
# Author: Wang Xu
# File: string_formatting.py

# Example using .format()
name = "Gibson L-5 CES"
year = 1922
cost = 16035.99

# Using .format() method
print("My guitar: {} {}".format(year, name))
print("My guitar: {1} {0}".format(name, year))
print("My guitar: {0} {0} {1}".format(name, year))
print("My guitar: {} for about ${:,.2f}!".format(name, cost))

# Using f-string formatting
print(f"My guitar: {year} {name}")
print(f"My guitar: {name} for about ${cost:,.2f}!")

# Aligning numbers using formatting in a loop
print("\nExponents of 2:")
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
