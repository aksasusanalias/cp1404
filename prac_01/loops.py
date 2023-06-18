"""
For i in range starting from 0 up to 100 with a step size of 10
    Display i with a space
    End the line
For i in range starting from 20 up to 0 with a step size of -1
    Display i with space
    End the line
get number of stars
For i in range starting from 1 up to count + 1 with a step size of 1
    Display "*" repeated i times
    End the line
For i in range starting from 1 up to count+1:
    Display "*" repeated i times in a pattern

"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
count = int(input("Number of stars : "))
for i in range(1, count+1):
    print("*", end=' ')
print("\n")
count = int(input("Number of stars : "))
for i in range(1, count+1):
    print("*" * i)

