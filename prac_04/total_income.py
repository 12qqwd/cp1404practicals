def main():
    months = int(input("How many months? "))
    incomes = [float(input(f"Enter income for month {month + 1}: ")) for month in range(months)]

    print("\nIncome Report")
    print_report(incomes)

def print_report(incomes):
    """Prints the income report using enumerate."""
    total = 0
    for i, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {i}: ${income:.2f}   Total: ${total:.2f}")

if __name__ == "__main__":
    main()
