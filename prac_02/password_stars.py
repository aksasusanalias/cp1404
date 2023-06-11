def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    word_len = len(password)
    for i in range(1, word_len + 1):
        print("*", end='')
    print("\n")


def get_password():
    password = input("Enter password : ")
    return password


main()
