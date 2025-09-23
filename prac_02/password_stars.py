MINIMUM_PASSWORD_LENGTH = 10

def main():
    password = get_password()

    print_asteriks(password)


def print_asteriks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password does not meet minimum password length!")
        password = input("Enter password: ")
    return password


main()