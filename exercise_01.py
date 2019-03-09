def pyramid_of_numbers(n):
    n_to_print = ""
    total = ""
    for i in range(1, n + 1):
        #d_bet_numbers is the spaces that exist between each number
        d_bet_numbers = int(len(str(i))) + 1
        n_to_print = f"{i:{d_bet_numbers}}{n_to_print}"
        space = "  " * (n - i)
        if total == "":
            total +=  f"{space}{n_to_print}"
        else:
            total +=  f"\n{space}{n_to_print}"

    return total


def main():
    number = eval(input("Enter a number: "))
    print(pyramid_of_numbers(number))


if __name__ == "__main__":
    main()
