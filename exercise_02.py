def reverse(number):
    return int(str(number)[::-1])


def is_palindrome(number):
    return reverse(number) == number


def main():
    number = eval(input("Enter a number: "))
    if is_palindrome(number):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome.")


if __name__ == "__main__":
    main()
