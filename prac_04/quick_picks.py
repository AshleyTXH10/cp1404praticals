import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

amount_of_quick_picks = int(input("How many quick picks? "))
for i in range(amount_of_quick_picks):
    random_numbers = []
    while len(random_numbers) < amount_of_quick_picks:
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    random_numbers.sort()

    for num in random_numbers:
        print(f"{num:2}" ,end=" ")
    print()