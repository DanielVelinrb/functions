def print_pyramid_of_numbers(n):
    temp = ""
    for i in range(1, n + 1):
        #sbn refers to the space between 
        sbn = int(len(str(n))) + 1
        temp = f'{i:<{sbn}}' + temp
        print(("   " * (n - i)) + temp)


def main():
    number = eval(input("Enter a number: "))
    print_pyramid_of_numbers(number)


if __name__ == "__main__":
    main()