class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50

    def __lt__(self, other):
        return self.year < other.year

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"
