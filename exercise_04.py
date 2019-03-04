def found_pi(number):
    formula = 0

    for i in range(1, number + 1):
        formula += (-1) ** ( i + 1) / (2 * i - 1)
        pi = 4 * formula

    return "{0:.4f}".format(pi)


def main():
    print(f"{'i':<25}m(i)\n")
    for i in range(1, 902, 100):
        to_print = f"{i:<25}{found_pi(i)}"
        print(to_print)


if __name__ == "__main__":
    main()
