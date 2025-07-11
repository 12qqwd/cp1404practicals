import csv
from guitar import Guitar

def load_guitars(filename):
    guitars = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for name, year, cost in reader:
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"'{filename}' not found. Starting with empty list.")
    return guitars

def save_guitars(filename, guitars):
    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for g in guitars:
            writer.writerow([g.name, g.year, g.cost])

def display_guitars(guitars, current_year):
    for i, g in enumerate(guitars, 1):
        vintage_label = " (vintage)" if g.is_vintage(current_year) else ""
        print(f"{i}. {g}{vintage_label}")

def get_new_guitars():
    guitars = []
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return guitars

def main():
    filename = "guitars.csv"
    current_year = 2025
    guitars = load_guitars(filename)
    print("These are your guitars:")
    display_guitars(guitars, current_year)

    print("\nEnter new guitars:")
    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)
    guitars.sort()

    print("\nUpdated guitar list:")
    display_guitars(guitars, current_year)

    save_guitars(filename, guitars)

if __name__ == "__main__":
    main()

