import csv
from programming_language import ProgrammingLanguage

def load_languages(filename):
    languages = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            languages.append(ProgrammingLanguage(
                row["Name"],
                row["Typing"],
                row["Reflection"] == "True",
                int(row["Year"]),
                row["PointerArithmetic"] == "True"
            ))
    return languages

def main():
    languages = load_languages("languages.csv")
    for lang in languages:
        print(lang)

if __name__ == "__main__":
    main()


