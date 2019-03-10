def feet_to_meters(feet):
    return feet * 0.305


def meters_to_feet(meters):
    return meters / 0.305


def print_table(n):
    print(f"{'Feet':<10}{'Meter':<10}{'|':<6}{'Meter':<10}{'Feet':<10}")
    foot_range = range(1, n + 1)
    meter_range = range(20, 20 + 5 * (n - 1) + 1, 5)

    for feet, meters in zip(foot_range, meter_range):
        foot_str = f'{feet_to_meters(feet):.3f}'
        meter_str = f'{meters_to_feet(meters):.3f}'

        print(f"{feet:<10}{foot_str:<10}", end='')
        print(f'{"|":<6}', end='')
        print(f'{meters:<10}{meter_str:<10}')


def main():
    print_table(10)


if __name__ == "__main__":
    main()
