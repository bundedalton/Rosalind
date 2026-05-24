##Recieve DNA ID and string from user and store in a list of tuples
##calculate gc content of each string and store the results with their ID in a list of tuples

# Function to receive DNA strings in FASTA format and store them in a list of tuples and checking valid input
def receive_dna_strings_FASTA(strings):
    dna = []
    id = []
    user_input = input("Enter DNA ID in the format '>Rosalind_xxxx' followed by the DNA string, separated by commas: ")
    for item in user_input.split(","):
        item = item.strip()
        if item.startswith(">"):
            id.append(item)
        else:
            dna.append(item)
  
    DNA_ID_PAIRS = list(zip(id, dna))
    print("DNA ID and String Pairs: ", DNA_ID_PAIRS)  
    return dna, id

# Function to calculate GC content of each DNA string
def calculate_gc_content(dna):
    gc_content = []
    for string in dna:
        if len(string) == 0:
            gc_content.append(0)
            continue
        gc_count = 0
        for char in string:
            if char == "G" or char == "C":
                gc_count += 1
        gc_content.append((gc_count / len(string))*100)
    rounded_gc_content = [round(val, 5) for val in gc_content]
    print("GC Content: ", rounded_gc_content, "%")
    return rounded_gc_content


# Function to store GC content with their corresponding IDs in a list of tuples
def store_gc_content_with_id(id, gc_content):
    gc_content_with_id = list(zip(id, gc_content))
    return gc_content_with_id


def main():
    dna, id = receive_dna_strings_FASTA([])
    gc_content = calculate_gc_content(dna)
    gc_content_with_id = store_gc_content_with_id(id, gc_content)
    ordered_by_GC_content = sorted(gc_content_with_id, key=lambda x: x[1], reverse=True)
    print("Ordered by GC Content: ", ordered_by_GC_content)
 
if __name__ == "__main__":
    main()
