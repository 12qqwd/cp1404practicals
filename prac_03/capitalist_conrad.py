import random

# Constants for customization
MAX_INCREASE = 0.175   # 17.5%
MAX_DECREASE = 0.05    # 5%
MIN_PRICE = 1.0        # Minimum valid stock price
MAX_PRICE = 100.0      # Maximum valid stock price
INITIAL_PRICE = 10.0   # Starting stock price
FILENAME = "output.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, 'w')

# Print initial price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1

    # Decide if the price increases or decreases
    if random.randint(0, 1) == 1:
        # Increase price
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Decrease price
        price_change = -random.uniform(0, MAX_DECREASE)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()
