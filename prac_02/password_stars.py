def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    pw = input("Enter your password: ")
    while pw == "":
        print("Password cannot be blank.")
        pw = input("Enter your password: ")
    return pw

def print_asterisks(pw):
    print("*" * len(pw))

main()
