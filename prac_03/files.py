# Question 1
FILENAME = "name.txt"
name = input("What is your name? ")
in_file = open(FILENAME, "w")
print(name, file=in_file)
in_file.close()