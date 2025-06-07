import random

# Constants for customization
MAX_INCREASE = 0.175   # 17.5%
MAX_DECREASE = 0.05    # 5%
MIN_PRICE = 1.0        # Minimum valid stock price
MAX_PRICE = 100.0      # Maximum valid stock price
INITIAL_PRICE = 10.0   # Starting stock price
FILENAME = "output.txt"


def simulate_price(start_price, min_price, max_price, max_increase, max_decrease):
    """Simulate the stock price changes and return a list of prices per day."""
    prices = [start_price]
    current_price = start_price

    while min_price <= current_price <= max_price:
        change_direction = random.randint(0, 1)
        if change_direction == 1:
            price_change = random.uniform(0, max_increase)
        else:
            price_change = -random.uniform(0, max_decrease)

        current_price *= (1 + price_change)
        if min_price <= current_price <= max_price:
            prices.append(current_price)

    return prices


def write_prices_to_file(prices, filename):
    """Write the price log to a file with formatted output."""
    with open(filename, 'w') as out_file:
        print(f"Starting price: ${prices[0]:,.2f}", file=out_file)
        for day, price in enumerate(prices[1:], start=1):
            print(f"On day {day} price is: ${price:,.2f}", file=out_file)


def main():
    prices = simulate_price(INITIAL_PRICE, MIN_PRICE, MAX_PRICE, MAX_INCREASE, MAX_DECREASE)
    write_prices_to_file(prices, FILENAME)


if __name__ == "__main__":
    main()

