import random

MIN_NUMBER = 1
MAX_NUMBER = 45
AMOUNT_OF_NUMBERS_PER_QUICK_PICK = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    number = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), AMOUNT_OF_NUMBERS_PER_QUICK_PICK)
    numbers = sorted(number)
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*numbers))
