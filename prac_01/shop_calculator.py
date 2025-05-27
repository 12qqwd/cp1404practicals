# shop_calculator.py
# CP1404 - Practical 01 - Shop Calculator

def calculate_total_price():
    # Constants for discount threshold and rate inside the function
    DISCOUNT_THRESHOLD = 100
    DISCOUNT_RATE = 0.10

    # Input and validate the number of items
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total_price = 0

    # Input the price for each item and accumulate the total
    for i in range(number_of_items):
        price = float(input("Price of item: "))
        total_price += price

    # Apply discount if the total exceeds the threshold
    if total_price > DISCOUNT_THRESHOLD:
        total_price *= (1 - DISCOUNT_RATE)

    # Display the final total price with two decimal places
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")

# Run the function
calculate_total_price()

