def find_pi(number):
    formula = 0

    for i in range(1, number + 1):
        formula += (-1) ** ( i + 1) / (2 * i - 1)
        pi = 4 * formula

    return f"{pi:.4f}"


def print_pi_values_table(n):
    table = ""
    for i in range(1, n + 1, 100):
        table += f"\n{i:<25}{find_pi(i)}"
        
    print(table)


def main():
    print(f"{'i':<25}m(i)")
    print_pi_values_table(901)
    
  
if __name__ == "__main__":
    main()
