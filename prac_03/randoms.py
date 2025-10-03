import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Printing a random number from 5 to 20
# What was the smallest number you could have seen, what was the largest?
# The smallest number that could be seen is 5 and the largest would be 20

# What did you see on line 2?
# printing an odd number between 3 and 10
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# No as it will only produce odd numbers    

# What did you see on line 3?
# prints a random float between 2.5 and 5.5
# What was the smallest number you could have seen, what was the largest?
# the smallest number would be 2.4 while the largest would be 5.5
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,100))
