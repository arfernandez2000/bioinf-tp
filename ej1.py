from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse

parser = argparse.ArgumentParser(description='Ejercicio 1. Nucleotide GenBank -> Protein FASTA')
parser.add_argument('-i', help='Input GenBank file (default = inputs/sequence.gb)', default='inputs/sequence.gb')
parser.add_argument('-o', help='Output Fatsa file (default = results/secuencias.fasta)', default='results/secuencias.fasta')
args = parser.parse_args()

def search_orfs(sequence):
    orfs = []
    
    start_codons = {"ATG", "AUG"}
    stop_codons = {"TAA", "TAG", "TGA"}
    
    i = 0
    while i < len(sequence):
        codon = sequence[i:i+3]
        
        if codon in start_codons:
            orf = codon
            for j in range(i + 3, len(sequence), 3):
                codon = sequence[j:j+3]
                orf += codon
                if codon in stop_codons:
                    orfs.append(orf)
                    i = j + 3
                    break
        else:
            i += 3
    
    return orfs

def translate_and_save_sequences(input_file, output_file):
    with open(input_file, "r") as in_handle, open(output_file, "w") as out_handle:
        records = SeqIO.parse(in_handle, "genbank")

        for record in records:
            for frame in range(3):
                nucleotide_sequence = record.seq[frame:]
                nucleotide_sequence_rev = record.seq.reverse_complement()[frame:]

                orfs = search_orfs(nucleotide_sequence)
                orfs_rev = search_orfs(nucleotide_sequence_rev)

                for orf in orfs + orfs_rev:
                    amino_acid_sequence = orf.translate(cds=True)
                    fasta_record = SeqRecord(amino_acid_sequence, id=f"{record.id}_ORF",
                                            description=f"ORF from {record.id}",
                                            letter_annotations={"phred_quality": [40]*len(amino_acid_sequence)})
                    SeqIO.write(fasta_record, out_handle, "fasta")

    print(f"Secuencias traducidas y guardadas en '{output_file}'")

input_file = "sequence.gb"
output_file = "secuencias.fasta"

input_file = args.i
output_file = args.o

translate_and_save_sequences(input_file, output_file)
