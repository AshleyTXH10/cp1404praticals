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