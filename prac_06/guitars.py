from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ").title()
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name: ").title()