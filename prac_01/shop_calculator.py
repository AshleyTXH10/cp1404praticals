"""
CP1404 Pratical 1 - Shop calculator
"""
DISCOUNT_REQUIREMENT = 100
DISCOUNT_RATE = 0.9
total_price = 0
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))
for i in range(1,number_of_items + 1):
    total_price += float(input(f"Enter item {i} price: $"))
if total_price > DISCOUNT_REQUIREMENT:
    total_price *= DISCOUNT_RATE
print(f"Total price for {number_of_items} items is ${total_price:.2f}")