"""
CP1404/CP5632 - Practical
Broken program to determine score status
get score
    if score is less than 0 or greater than 100 "display score"
    if score is greater than 49 or less than 90 display "Passable"
    if score is less than 50 display "bad"
or display "excellent"
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 50 and score <= 89:
        print("Passable")
    elif score < 50:
        print("Bad")
    else:
        print("Excellent")
