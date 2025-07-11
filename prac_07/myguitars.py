"""Manage guitars: load, add, sort, save, display."""

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
        print(f"Warning: '{filename}' not found. Starting empty.")
    return guitars

def save_guitars(filename, guitars):
    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for g in guitars:
            writer.writerow([g.name, g.year, g.cost])

def display_guitars(guitars, current_year):
    for i, g in enumerate(guitars, 1):
        vintage_mark = " (vintage)" if g.is_vintage(current_year) else ""
        print(f"{i}. {g}{vintage_mark}")

def get_user_guitars():
    guitars = []
    print("Enter new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    return guitars

def manage_guitars():
    filename = "guitars.csv"
    current_year = 2025
    guitars = load_guitars(filename)
    print("Current guitars:")
    display_guitars(guitars, current_year)

    new_list = get_user_guitars()
    guitars.extend(new_list)
    guitars.sort()

    print("\nSorted guitars:")
    display_guitars(guitars, current_year)
    save_guitars(filename, guitars)

if __name__ == "__main__":
    manage_guitars()
