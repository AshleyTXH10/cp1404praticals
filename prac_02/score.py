"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    determine_score_category(score)

    random_score = random.randint(1,100)
    determine_score_category(random_score)

def determine_score_category(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()