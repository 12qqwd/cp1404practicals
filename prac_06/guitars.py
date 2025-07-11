from guitar import Guitar

def main():
    print("My guitars!")
    guitars = get_guitars_from_user()

   if guitars:
      print("\nThese are my guitars:")
      for i, guitar in enumerate(guitars, 1):
          vintage_string = " (vintage)" if guitar.is_vintage() else ""
          print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
                f"worth ${guitar.cost:10,.2f}{vintage_string}")

    else:
        print("No guitars entered.")

def get_guitars_from_user():
    guitars = []
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
   return guitars

if __name__ == "__main__":
    main()