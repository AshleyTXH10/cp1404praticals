MINIMUM_PASSWORD_LENGTH = 10

password = input("Enter password: ")

while len(password) < MINIMUM_PASSWORD_LENGTH:
    print("Password does not meet minimum password length!")
    password = input("Enter password")

print("*" * len(password))