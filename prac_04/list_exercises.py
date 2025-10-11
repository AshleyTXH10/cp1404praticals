AMOUNT_OF_NUMBERS = 5
numbers = []

for i in range(AMOUNT_OF_NUMBERS):
    numbers.append(int(input(f"Enter number {i + 1}: ")))

# print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/AMOUNT_OF_NUMBERS}")

