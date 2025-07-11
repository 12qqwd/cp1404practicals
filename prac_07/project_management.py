import csv
from datetime import datetime
from project import Project

FILENAME = "projects.txt"

def load_projects(filename):
    projects = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            projects.append(Project(
                row["Name"], row["Start Date"],
                row["Priority"], row["Cost Estimate"],
                row["Completion Percentage"]
            ))
    return projects

def save_projects(filename, projects):
    with open(filename, "w", newline='', encoding='utf-8') as file:
        fieldnames = ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for p in projects:
            writer.writerow({
                "Name": p.name,
                "Start Date": p.start_date.strftime("%d/%m/%Y"),
                "Priority": p.priority,
                "Cost Estimate": f"{p.cost_estimate:.2f}",
                "Completion Percentage": p.completion
            })

def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

def filter_projects(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.started_after(date_obj)], key=lambda p: p.start_date)
    for p in filtered:
        print(p)

def add_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: ")
    completion = input("Percent complete: ")
    return Project(name, start_date, priority, cost, completion)

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_completion = input("New % completion (leave blank to keep current): ")
    new_priority = input("New priority (leave blank to keep current): ")
    if new_completion:
        project.completion = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)

def main():
    projects = load_projects(FILENAME)
    menu = "\n(L)oad  (S)ave  (D)isplay  (F)ilter  (A)dd  (U)pdate  (Q)uit\n>>> "
    choice = input(menu).lower()

    while choice != 'q':
        if choice == 'l':
            file = input("Filename: ")
            projects = load_projects(file)
        elif choice == 's':
            file = input("Save as: ")
            save_projects(file, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects(projects)
        elif choice == 'a':
            projects.append(add_project())
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(menu).lower()

    save_projects(FILENAME, projects)
    print("Projects saved. Goodbye!")

if __name__ == "__main__":
    main()
