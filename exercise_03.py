def footToMeters(foot):
    meter = foot * 0.305
    return "{0:.3f}".format(meter)

def metersToFoot(meter):
    foot = meter / 0.305
    return "{0:.3f}".format(foot)

beggining = f"{'Feet':<10}{'Meter':<10}{'|':<10}{'Meter':<10}{'Feet':<10}"
print(beggining)

def main():
    print(beggining)
    for i in range(1, 11):
        j = 20 + 5 * (i - 1)

        table = f"{i:<10}{footToMeters(i):<10}{'|':<10}{j:<10}{metersToFoot(j):<10}"

        print(table)

if __name__ == "__main__":
    main()
