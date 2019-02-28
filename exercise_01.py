def displayPattern(n):
    n_to_print = ""
    total = ""
    for i in range(1, n + 1):
        n_to_print = "{} {}".format(i, n_to_print)
        space = "  " * (n - i)

        total =  "{}\n{}{}".format(total, space, n_to_print)

    return total

input = eval(input("Enter a number: "))


print(displayPattern(input))
