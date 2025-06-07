def get_integer(prompt):
    """Prompt user until they enter a valid integer."""
    value = None
    valid = False
    while not valid:
        try:
            value = int(input(prompt))
            valid = True
        except ValueError:
            print("You must enter a valid integer.")
    return value


def perform_division():
    numerator = get_integer("Enter the numerator: ")
    denominator = get_integer("Enter the denominator: ")

    if denominator == 0:
        print("Denominator cannot be zero.")
        return  # exit the function early

    result = numerator / denominator
    print(f"{numerator} / {denominator} is {result}")


def main():
    perform_division()


if __name__ == "__main__":
    main()

