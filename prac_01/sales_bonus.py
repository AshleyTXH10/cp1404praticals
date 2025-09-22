"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SMALL_BONUS = 0.1
BIG_BONUS = 0.15
BIG_BONUS_REQUIREMENT = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BIG_BONUS_REQUIREMENT:
        bonus = sales * SMALL_BONUS
    else:
        bonus = sales * BIG_BONUS
    print(f"Your bonus is: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

