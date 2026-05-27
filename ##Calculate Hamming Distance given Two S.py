##Calculate Hamming Distance given Two Strings
def hamming_distance(string1,string2):
    distance = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            distance += 1
    return distance

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    distance = hamming_distance(string1, string2)
    print("Hamming Distance: ", distance)
if __name__ == "__main__":
    main()
    