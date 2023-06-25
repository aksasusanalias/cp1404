"""
    if score is less than 0 or greater than 100 "display score"
    if score is greater than 49 or less than 90 display "Passable"
    if score is less than 50 display "bad"
or display "excellent"
"""

import random


def main():
    score = float(input("Enter score: "))
    print(find_result(score))
    score = random.uniform(0, 100)
    print(f"{score:.2f}")
    print(find_result(score))


def find_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 <= score < 90:
        return "Passable"
    elif score < 50:
        return "Bad"
    else:
        return "Excellent"


if __name__ == "__main__":
    main()
