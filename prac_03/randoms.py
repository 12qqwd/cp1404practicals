import random

def random_int_5_20():
    return random.randint(5, 20)

def random_odd_3_9():
    return random.randrange(3, 10, 2)

def random_float_2_5_5_5():
    return random.uniform(2.5, 5.5)

def random_int_1_100():
    return random.randint(1, 100)

def main():
    print(random_int_5_20())
    print(random_odd_3_9())
    print(random_float_2_5_5_5())
    print(f"Random number between 1 and 100: {random_int_1_100()}")

if __name__ == "__main__":
    main()


