# Q1: Ask the user for their name and write it to a file called name.txt
name = input("Enter your name: ")
file_out = open("name.txt", 'w')  # Open the file for writing
file_out.write(name + "\n")       # Write the name and a newline
file_out.close()                  # Always close the file

# Q2: Read the name back from the file and print it in a greeting
file_in = open("name.txt", 'r')   # Open the file for reading
stored_name = file_in.read().strip()  # Read and strip the newline
file_in.close()
print(f"Hi {stored_name}!")
# Q3: Create a file numbers.txt with the numbers:
#     17
#     42
#     400
# You should do this manually or with a text editor (not in code here).
# Q4: Open numbers.txt, read only the first two numbers, add them, and print the result
with open("numbers.txt", 'r') as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
    total = first_number + second_number
    print(total)  # Expected output: 59
# Q5: Sum all numbers in numbers.txt, regardless of how many
total = 0
with open("numbers.txt", 'r') as numbers_file:
    for line in numbers_file:        # 'for line in file' is great for reading line-by-line
        number = int(line.strip())   # Remove newline and convert to int
        total += number
print(total)  # Expected output with 17, 42, 400: 459
