# import argparse

# parser = argparse.ArgumentParser(description='Ejercicio 1. Nucleotide GenBank -> Protein FASTA')
# parser.add_argument('-i', help='Input GenBank file (default = inputs/ej1/NM_001385125.gbk)', default='inputs/ej1/NM_001385125.gbk')
# parser.add_argument('-o', help='Output Fatsa file (default = outputs/ej1/protein.fas)', default='outputs/ej1/protein.fas')
# args = parser.parse_args()

# gb_file = args.i
# out_path = args.o

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

input_file = "sequence.gb"

output_file = "secuencias.fasta"

with open(input_file, "r") as in_handle, open(output_file, "w") as out_handle:
    records = SeqIO.parse(in_handle, "genbank")

    # Itera a través de las secuencias
    for record in records:
        for frame in range(1):
            nucleotide_sequence = record.seq[frame:]
            
            print(nucleotide_sequence)
        
            amino_acid_sequence = nucleotide_sequence.translate()
            
            print(amino_acid_sequence)
            fasta_record = SeqRecord(amino_acid_sequence, id=f"{record.id}_Frame{frame+1}", description=f"Translated from {record.id} Frame {frame+1}", letter_annotations={"phred_quality": [40]*len(amino_acid_sequence)})

            print(fasta_record)
            
            SeqIO.write(fasta_record, out_handle, "fasta")

print(f"Secuencias traducidas y guardadas en '{output_file}'")