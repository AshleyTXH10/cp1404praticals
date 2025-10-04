# Question 1
FILENAME = "name.txt"
name = input("What is your name? ")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

#Question 2
FILENAME = "name.txt"
in_file = open(FILENAME)
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

#Question 3
FILENAME = "numbers.txt"
with open("numbers.txt", "r") as in_file:
    lines = in_file.readlines()

first_number = int(lines[0])
second_number = int(lines[1])
print(f"{first_number + second_number}")

#Question 4
FILENAME = "numbers.txt"
total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        total += int(line.strip())

print(f"{total }")