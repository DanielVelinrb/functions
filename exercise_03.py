def foot_to_meters(foot):
    return f"{foot * 0.305:.3f}"


def meters_to_foot(meter):
    return f"{meter / 0.305:.3f}"


def print_table(n):
    print(f"{'Feet':<10}{'Meter':<10}{'|':<10}{'Meter':<10}{'Feet':<10}")
    for i in range(1, n + 1):
        j = 20 + 5 * (i - 1)
        table = f"{i:<10}{foot_to_meters(i):<10}{'|':<10}{j:<10}{meters_to_foot(j):<10}"
        print(table)
    return table


def main():  
    print_table(10)
            

if __name__ == "__main__":
    main()
