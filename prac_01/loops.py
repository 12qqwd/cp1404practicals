# loops.py
# CP1404 - Practical 01 - Loops Exercises

# Original Example: Print odd numbers between 1 and 20
print("Original: Print odd numbers between 1 and 20")
for i in range(1, 21, 2):
    print(i, end=' ')
print()  # move to next line


# a. Count in 10s from 0 to 100
print("\na. Count in 10s from 0 to 100")
for i in range(0, 101, 10):
    print(i, end=' ')
print()


# b. Count down from 20 to 1
print("\nb. Count down from 20 to 1")
for i in range(20, 0, -1):
    print(i, end=' ')
print()


# c. Print n stars on one line
print("\nc. Print n stars on one line")
num_stars = int(input("Number of stars: "))
for i in range(num_stars):
    print("*", end='')
print()


# d. Print n lines of increasing stars
print("\nd. Print n lines of increasing stars")
for i in range(1, num_stars + 1):
    print("*" * i)
