import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? - 20
# What was the smallest number you could have seen - 5
# what was the largest - 20


# What did you see on line 2? - 7
# What was the smallest number you could have seen  - 3
# what was the largest? - 9
# Could line 2 have produced a 4? - NO

# What did you see on line 3? - 3.4377969399905846
# What was the smallest number you could have seen - 2.5
# what was the largest? - 5.5

print(random.uniform(1, 100))
