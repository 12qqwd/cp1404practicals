"""Menu-driven project management without while True or globals."""

import csv
from datetime import datetime
from project import Project

def load_from_file(filename):
    projects = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            projects.append(Project(
                row["Name"], row["Start Date"], row["Priority"],
                row["Cost Estimate"], row["Completion Percentage"]))
    return projects

def save_to_file(filename, projects):
    with open(filename, "w", newline='', encoding='utf-8') as file:
        fieldnames = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for p in projects:
            writer.writerow({
                "Name": p.name,
                "Start Date": p.start_date.strftime("%d/%m/%Y"),
                "Priority": p.priority,
                "Cost Estimate": f"{p.cost:.2f}",
                "Completion Percentage": p.percent
            })

def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete:")
    for p in incomplete:
        print("  ", p)
    print("Complete:")
    for p in complete:
        print("  ", p)

def filter_projects(projects, date_str):
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.started_after(date)]
    for p in sorted(filtered, key=lambda p: p.start_date):
        print(p)

def add_project():
    name = input("Name: ")
    start = input("Start Date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    percent = input("Percent complete: ")
    return Project(name, start, priority, cost, percent)

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i}: {p}")
    idx = int(input("Select project index: "))
    p = projects[idx]
    new_percent = input("New percent (leave blank to keep): ")
    new_priority = input("New priority (leave blank to keep): ")
    if new_percent:
        p.percent = int(new_percent)
    if new_priority:
        p.priority = int(new_priority)

def menu_loop():
    filename = "projects.txt"
    projects = load_from_file(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    options = {
        'l': lambda: load_from_file(input("Load filename: ")),
        's': lambda: save_to_file(input("Save filename: "), projects),
        'd': lambda: display_projects(projects),
        'f': lambda: filter_projects(projects, input("After date (dd/mm/yyyy): ")),
        'a': lambda: projects.append(add_project()),
        'u': lambda: update_project(projects),
    }

    def get_choice():
        prompt = "\n(L)oad, (S)ave, (D)isplay, (F)ilter, (A)dd, (U)pdate, (Q)uit: "
        choice = input(prompt).lower()
        return choice if choice in options or choice == 'q' else None

    choice = get_choice()
    while choice != 'q':
        if choice:
            action = options.get(choice)
            result = action()
            if choice == 'l':
                projects[:] = result  # replace list content
        else:
            print("Invalid choice.")
        choice = get_choice()

    if input("Save on exit? (y/n): ").lower().startswith('y'):
        save_to_file(filename, projects)
    print("Goodbye!")

if __name__ == "__main__":
    menu_loop()
