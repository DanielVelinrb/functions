def display_pattern(n):
    n_to_print = ""
    total = ""
    for i in range(1, n + 1):
        n_to_print = "{} {}".format(i, n_to_print)
        space = "  " * (n - i)

        total =  "{}\n{}{}".format(total, space, n_to_print)

    return total


def main():
    number = eval(input("Enter a number: "))
    print(display_pattern(number))


if __name__ == "__main__":
    main()
