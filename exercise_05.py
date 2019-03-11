def convert_millis(millis):
    seconds = millis // 1000
    hours = seconds // 3600

    seconds %= 3600
    minutes = seconds // 60

    seconds %= 60

    return f"{hours}:{minutes}:{seconds}"


def main():
    number = eval(input("Enter a number: "))
    print(convert_millis(number))


if __name__ == "__main__":
    main()
