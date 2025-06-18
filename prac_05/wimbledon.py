import csv


def load_wimbledon_data(filename):
    """Read Wimbledon data from a CSV file and return a list of rows."""
    with open(filename, mode="r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        return list(reader)


def count_champions(data):
    """Return a dictionary of champion names to win counts."""
    champion_to_count = {}
    for row in data:
        champion = row[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count


def get_unique_countries(data):
    """Return a sorted set of unique countries."""
    countries = {row[1] for row in data}
    return sorted(countries)


def main():
    filename = "wimbledon.csv"
    data = load_wimbledon_data(filename)

    champion_to_count = count_champions(data)
    countries = get_unique_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
