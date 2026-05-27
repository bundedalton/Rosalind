##Permutation Calculator
##given a positive integer n, return number of possible permutations and list them

def calculate_permutations():
    n = int(input("Enter a positive integer n <= 7: "))
    if n < 1:
        return 0, []
    from itertools import permutations
    perm_list = [''.join(p) for p in permutations([str(i) for i in range(1, n + 1)])]
    return len(perm_list), perm_list

def main():
    count, permutations = calculate_permutations()
    print(f"Number of permutations: {count}")
    print("Permutations:")
    with open("permutations.txt", "w") as f:
        for perm in permutations:
            f.write(perm + "\n")
if __name__ == "__main__":
    main()    