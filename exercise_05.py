def convertMillis(millis):
    to_use = (millis // 1000)
    hours = to_use // 3600
    to_use %=  3600

    return f"{hours}:{to_use // 60}:{to_use % 60}"

input = eval(input("Enter a number: "))

print(convertMillis(input))
