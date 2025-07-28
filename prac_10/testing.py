def repeat_string(s, n):
    """Repeat string s, n times."""
    return s * n

def is_long_word(word, length=5):
    """
    Return True if the word is longer than length.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    False
    """
    return len(word) > length

def format_sentence(phrase):
    """
    Format phrase as a sentence: start with a capital and end with a single period.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an example')
    'It is an example.'
    >>> format_sentence('This is a test.')
    'This is a test.'
    """
    sentence = phrase.strip()
    if not sentence.endswith('.'):
        sentence += '.'
    sentence = sentence[0].upper() + sentence[1:]
    return sentence

class Car:
    def __init__(self, fuel=0):
        self.fuel = fuel

    def add_fuel(self, amount):
        self.fuel += amount

# Example assertions
car = Car()
car.add_fuel(10)
assert car.fuel == 10, "Fuel should be 10 after adding 10"
car.add_fuel(5)
assert car.fuel == 15, "Fuel should be 15 after adding another 5"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
