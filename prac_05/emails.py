def get_name_from_email(email):
    """Extract a guessed name from the email address."""
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name


def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        guessed_name = get_name_from_email(email)
        confirmation = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()

        if confirmation != "" and confirmation != "y":
            actual_name = input("Name: ").strip()
        else:
            actual_name = guessed_name

        email_to_name[email] = actual_name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
