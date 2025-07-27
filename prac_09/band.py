class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"
