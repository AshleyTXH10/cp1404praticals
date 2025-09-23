"""
CP1404/CP5632 - Practical 2
Program for score menu
"""
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    score = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "g":
            score = get_score()

        elif choice == "p":
            determine_score_category(score)

        elif choice == "s":
            print_star(score)

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Farewell!")


def print_star(score):
    """Print as many star as score"""
    print("*" * score)


def get_score():
    """Get valid score"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_score_category(score):
    """Determine score category using score"""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()