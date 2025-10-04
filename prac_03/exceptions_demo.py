"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    #Question 3 change
    while denominator <= 0:
        print("Denominator must be greater than zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# When will a ValueError occur?
# It will occur when the value entered in numerator or denominator is not a valid integer

# When will a ZeroDivisionError occur?
# It will occur when denominator is zero

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, you can change is by looping getting the input of denominator until user enters a valid denominator (>0)