"""
emails
Estimate: 15 minutes
Actual:
"""
def main():
    """Ask user for email, extract and confirm name, print the user's name and their email"""
    name_to_email = {}

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        is_name_correct = input(f"is your name {name}? (y/n) ").lower()

        if is_name_correct == "n":
            name = input("Name: ")
        name_to_email[name] = email

        email = input("Email: ")

    for name, email in name_to_email.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extract potential name from email"""
    email_prefix = email.split("@")[0]
    name = email_prefix.replace('.', ' ').split()
    # name = ' '.join(parts).title()
    return " ".join(name).title()

main()