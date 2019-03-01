def reverse(number):
    n_list = list(str(number))
    number = ""
    for i in range(1, len(n_list) + 1):
        number += n_list[-i]

    return number

def isPalindrome(number):
    n_to_check = int(reverse(number))

    if n_to_check == int(number):
        return "It's a palindrome"
    else:
        return "Sorry, it's not a palindrome."


input = eval(input("Enter a number: "))

def main():
    print(isPalindrome(input))

if __name__ == "__main__":
    main()
