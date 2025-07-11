"""Project data class."""

from datetime import datetime

class Project:
    def __init__(self, name, start_date_str, priority, cost, percent):
        self.name = name
        self.start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost = float(cost)
        self.percent = int(percent)

    def is_complete(self):
        return self.percent == 100

    def __lt__(self, other):
        return self.priority < other.priority

    def started_after(self, date_obj):
        return self.start_date > date_obj

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.percent}%")
