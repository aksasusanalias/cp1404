def main():
    password = get_password()
    asterisks = print_asterisks(password)
    print(asterisks)


def print_asterisks(password):
    word_len = len(password)

    asterisks = '*' * word_len
    return "\n" + asterisks


def get_password():
    password = input("Enter password : ")
    return password


main()
