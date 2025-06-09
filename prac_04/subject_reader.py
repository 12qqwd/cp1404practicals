FILENAME = "subject_data.txt"

def main():
    subjects = get_subjects()
    display_subjects(subjects)

def get_subjects():
    subjects = []
    with open(FILENAME) as file:
        for line in file:
            parts = line.strip().split(',')
            subject_name = parts[0]
            lecturer = parts[1]
            student_count = int(parts[2])
            subjects.append((subject_name, lecturer, student_count))
    return subjects

def display_subjects(subjects):
    for subject_name, lecturer, student_count in subjects:
        print(f"{subject_name} is taught by {lecturer} and has {student_count} students")

if __name__ == "__main__":
    main()
