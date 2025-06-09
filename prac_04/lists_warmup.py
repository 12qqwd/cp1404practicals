def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    # Example operations
    print(numbers[0])        # 3
    print(numbers[-1])       # 2
    print(numbers[3])        # 1
    print(numbers[:-1])      # [3, 1, 4, 1, 5, 9]
    print(numbers[3:4])      # [1]
    print(5 in numbers)      # True
    print(7 in numbers)      # False
    print("3" in numbers)    # False (string '3' is not in list)
    print(numbers + [6, 5, 3])

    numbers[0] = "ten"
    numbers[-1] = 1
    print(numbers[2:])       # [4, 1, 5, 9, 1]
    print(9 in numbers)      # True

if __name__ == "__main__":
    main()
