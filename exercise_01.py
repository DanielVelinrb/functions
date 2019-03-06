def pyramid_of_numbers(n):
    n_to_print = ""
    total = ""
    for i in range(1, n + 1):
        n_to_print = f"{i} {n_to_print}"
        space = "  " * (n - i)

        total =  f"{total}\n{space}{n_to_print}"

    return total


def main():
    number = eval(input("Enter a number: "))
    print(pyramid_of_numbers(number))


if __name__ == "__main__":
    main()
