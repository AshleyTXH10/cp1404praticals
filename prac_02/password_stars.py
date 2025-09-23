MINIMUM_PASSWORD_LENGTH = 10

def main():
    "simple password program"
    password = get_password()
    print_asteriks(password)

def print_asteriks(password):
    "Print amount of asteriks of password length"
    print("*" * len(password))

def get_password():
    "Get user password"
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password does not meet minimum password length!")
        password = input("Enter password: ")
    return password


main()