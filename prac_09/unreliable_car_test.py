from unreliable_car import UnreliableCar

def main():
    unreliable = UnreliableCar("CrapCar", 100, 50)
    for i in range(10):
        distance = unreliable.drive(10)
        print(f"Attempt {i + 1}: Drove {distance}km")

main()
