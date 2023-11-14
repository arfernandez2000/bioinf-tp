from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse
import os


parser = argparse.ArgumentParser(description='Ejercicio 1. Nucleotide GenBank -> Protein FASTA')
parser.add_argument('-i', help='Input GenBank file (default = inputs/sequence.gb)', default='inputs/sequence.gb')
parser.add_argument('-o', help='Output Fatsa file (default = results/secuencias_a.fas)', default='results/secuencias_a.fasta')
args = parser.parse_args()

def translate_and_save(orfs, record, out_handle):
    for orf in orfs:
        amino_acid_sequence = Seq(orf).translate(cds=True)
        fasta_record = SeqRecord(amino_acid_sequence, id=f"{record.id}_ORF",
                                description=f"ORF from {record.id}",
                                letter_annotations={"phred_quality": [40]*len(amino_acid_sequence)})
        SeqIO.write(fasta_record, out_handle, "fasta")

def save_orfs_to_file(record, orfs, output_directory):
    # Create a directory for the record if it doesn't exist
    record_directory = os.path.join(output_directory, record.id)
    os.makedirs(record_directory, exist_ok=True)

    # Save all ORFs to a single file for the record
    file_path = os.path.join(record_directory, f"sequence.fas")
    with open(file_path, "w") as file:
        file.write(f">Length {len(orfs)}\n")
        for i, orf_sequence in enumerate(orfs):
            file.write(orf_sequence)

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
            orfs = []
            sequence = str(record.seq)
            for i in range(3):
                orfs.extend(search_orfs(sequence[i:]))
            sequence = sequence[::-1] 
            for i in range(3):
                orfs.extend(search_orfs(sequence[i:]))
            translate_and_save(orfs,record,out_handle)
            save_orfs_to_file(record,orfs,"results")
    print(f"Secuencias traducidas y guardadas en '{output_file}'")

if __name__ == "__main__":
    input_file = args.i
    output_file = args.o

    translate_and_save_sequences(input_file, output_file)
