
def translate_dna_to_protein(dna_sequence):
    # Define the standard genetic code
    genetic_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }

    protein_sequence = ""

    # Check if the DNA sequence length is a multiple of 3
    if len(dna_sequence) % 3 != 0:
        raise ValueError("DNA sequence length is not a multiple of 3")

    # Iterate over the DNA sequence in steps of 3 (codons)
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if codon in genetic_code:
            protein_sequence += genetic_code[codon]
        else:
            raise ValueError(f"Invalid codon: {codon}")

    return protein_sequence

# Example usage:
dna_seq = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
protein_seq = translate_dna_to_protein(dna_seq)
print(f"Protein sequence: {protein_seq}")
