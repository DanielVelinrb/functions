def reverse(number):
    n_list = list(str(number))
    number = ""
    for i in range(1, len(n_list) + 1):
        number += n_list[-i]

    return int(number)


def is_palindrome(number):
    n_to_check = reverse(number)

    return n_to_check == number   


def main():
    number = eval(input("Enter a number: "))
    if is_palindrome(number):
        print("It's a palindrome")
    else:
        print("Sorry it's not a palindrome.")


if __name__ == "__main__":  
    main()
