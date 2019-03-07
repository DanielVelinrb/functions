def found_pi(number):
    formula = 0

    for i in range(1, number + 1):
        formula += (-1) ** ( i + 1) / (2 * i - 1)
        pi = 4 * formula

    return f"{pi:.4f}"


def print_pi_values_table(n):
    print(f"{'i':<25}m(i)")
    to_print = ""
    for i in range(1, n + 1, 100):
        to_print += f"\n{i:<25}{found_pi(i)}"
        
    return to_print

def main():
    print(print_pi_values_table(901))
    

if __name__ == "__main__":
    main()
