MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit
"""
import score


def main():
    print(MENU)
    choice = input(">>> ").upper()
    scores = -1
    while choice != "Q":
        if choice == "G":
            try:
                scores = int(input("Enter score: "))
                score.find_result(scores)
                while scores < 0 or scores > 100:
                    print("Invalid Score! Enter score between 0 to 100")
                    scores = int(input("Enter score: "))
            except ValueError:
                print("Invalid input. Enter score between 0 to 100.")
        elif choice == "P":
            print(score.find_result(scores))
        elif choice == "S":
            if scores == -1:
                print("Invalid Score! Enter score between 0 to 100")
            asterisks = print_asterisks(scores)
            print(asterisks)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def print_asterisks(marks):
    asterisks = '*' * marks
    return "\n" + asterisks


if __name__ == "__main__":
    main()
