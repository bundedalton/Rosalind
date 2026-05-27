codon_aas = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", }

def rna_to_protein(rna):
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        aa = codon_aas[codon]
        if (aa == 'Stop'):
            return protein
        protein = protein + aa
    return protein


def main():
    rna = input("Enter an RNA string: ")
    protein_string = rna_to_protein(rna)
    print("Corresponding Protein String:", protein_string)
    f = open("gene_to_aa.txt", "w")
    f.write(protein_string)
    f.close()
if __name__ == "__main__":    main()

