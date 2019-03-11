def compute_m(i):
    return 4 * (-1) ** (i + 1) / (2 * i - 1)


def print_pi_values_table(n):
    print(f"{'i':<10}m(i)")
    pi_approx = 0

    for i in range(1, n + 1):
        pi_approx += compute_m(i)
        if (i - 1) % 100 == 0:
            print(f"{i:<10}{pi_approx:.4f}")


def main():
    print_pi_values_table(901)


if __name__ == "__main__":
    main()
