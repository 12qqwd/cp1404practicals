def main():
    state_names = {
        "QLD": "Queensland",
        "NSW": "New South Wales",
        "NT": "Northern Territory",
        "WA": "Western Australia",
        "SA": "South Australia",
        "VIC": "Victoria",
        "TAS": "Tasmania"
    }

    # Display all states and their full names
    print("All states and their names:")
    for abbr, name in state_names.items():
        print(f"{abbr:3} is {name}")

    user_input = input("Enter short state: ").upper()
    try:
        print(f"{user_input} is {state_names[user_input]}")
    except KeyError:
        print("Invalid short state")


if __name__ == "__main__":
    main()

