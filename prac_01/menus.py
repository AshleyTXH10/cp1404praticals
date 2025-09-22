"""
CP1404 Pratical 1 - Menus
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
MENU_CHOICES = "hgq"
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").lower()
while choice not in MENU_CHOICES:
    print("Invalid Choice")
    print(MENU)
    choice = input(">>> ").lower()

while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
        print(MENU)
        choice = input(">>> ").lower()
    else:
        print(f"Goodbye {name}")
        print(MENU)
        choice = input(">>> ").lower()
print("Finished.")