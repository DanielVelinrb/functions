def convert_millis(millis):
    to_use = (millis // 1000)
    hours = to_use // 3600
    to_use %=  3600

    return f"{hours}:{to_use // 60}:{to_use % 60}"

input = eval(input("Enter a number: "))

def main():
    if __name__ == "__main__":
        print(convert_millis(input))


main()
