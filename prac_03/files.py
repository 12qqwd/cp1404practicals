def write_name():
    name = input("Enter your name: ")
    with open("name.txt", 'w') as file_out:
        file_out.write(name + "\n")

def read_and_greet():
    with open("name.txt", 'r') as file_in:
        stored_name = file_in.read().strip()
    print(f"Hi {stored_name}!")

def sum_first_two_numbers():
    with open("numbers.txt", 'r') as numbers_file:
        first_number = int(numbers_file.readline())
        second_number = int(numbers_file.readline())
    total = first_number + second_number
    print(total)

def sum_all_numbers():
    total = 0
    with open("numbers.txt", 'r') as numbers_file:
        for line in numbers_file:
            number = int(line.strip())
            total += number
    print(total)

def main():
    write_name()
    read_and_greet()
    sum_first_two_numbers()
    sum_all_numbers()

if __name__ == "__main__":
    main()

