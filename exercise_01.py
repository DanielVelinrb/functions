def print_pyramid_of_numbers(n):
    temp = ''
    for i in range(1, n + 1):
        spacing = int(len(str(n))) + 1
        temp = f'{i:<{spacing}}' + temp
        print(' ' * spacing * (n - i) + temp)


def main():
    number = eval(input('Enter a number: '))
    print_pyramid_of_numbers(number)


if __name__ == '__main__':
    main()
