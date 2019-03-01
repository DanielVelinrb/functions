def convertMillis(millis):
    to_use = (millis // 1000)
    hours = to_use // 3600
    to_use %=  3600

    return f"{hours}:{to_use // 60}:{to_use % 60}"

input = eval(input("Enter a number: "))

def main():
    print(convertMillis(input))

if __name__ == "__main__":
    main()
