"""
CP1404- Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

def main():
   my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven}km")
    print(limo)


main()