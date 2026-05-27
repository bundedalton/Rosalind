import re
import requests

def get_uniprot_sequence(uniprot_id):
    """Fetches the FASTA sequence from UniProt and strips out the header."""
    # Ensure we use the raw ID for the URL API endpoint
    # Stripping out any sub-entity naming like _TRBM_HUMAN if present for the URL
    accession = uniprot_id.split('_')[0]
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    
    response = requests.get(url)
    if response.status_code != 200:
        return ""
    
    # Split lines, ignore the header line starting with '>', join the rest
    lines = response.text.strip().split('\n')
    sequence = "".join(lines[1:])
    return sequence

def find_glycosylation_motifs(uniprot_ids):
    """Finds 1-based locations of the N-glycosylation motif in a list of IDs."""
    # Pattern explanation:
    # N = Asparagine
    # [^P] = Any amino acid except Proline
    # [ST] = Either Serine or Threonine
    # [^P] = Any amino acid except Proline
    # (?= ... ) handles overlapping instances like NNST smoothly
    motif_regex = r"(?=(N[^P][ST][^P]))"
    
    for uniprot_id in uniprot_ids:
        sequence = get_uniprot_sequence(uniprot_id)
        if not sequence:
            continue
            
        # finditer scans the string. match.start() + 1 converts to 1-based indexing
        locations = [match.start() + 1 for match in re.finditer(motif_regex, sequence)]
        
        # Output exactly in the Rosalind-required format
        if locations:
            print(uniprot_id)
            print(" ".join(map(str, locations)))

# --- Example Run ---
# 
if __name__ == "__main__":
    # Sample Dataset containing at most 15 IDs 
    f = open(r"E:\Rosalind\A2Z669.txt").read()
    uniport_ids = [line.strip() for line in f.splitlines() if line.strip()]
    for i in range(len(uniport_ids)):
        cln_uniport_code = uniport_ids
        cln_uniport_code = uniport_ids[ :6]
    find_glycosylation_motifs(uniport_ids)

