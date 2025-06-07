def get_valid_integer():
    is_valid_input = False
    while not is_valid_input:
        try:
            result = int(input("Enter a valid integer: "))
            is_valid_input = True
        except ValueError:
            print("Please enter a valid integer.")
    return result

def main():
    result = get_valid_integer()
    print(f"Valid result is: {result}")

if __name__ == "__main__":
    main()


