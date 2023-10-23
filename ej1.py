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
start_codons = ["ATG", "AUG"]
stop_codons = ["TAA", "TAG", "TGA"]

def search_orfs(sequence):
    orfs = []

    for start_codon in start_codons:
        for stop_codon in stop_codons:
            inside_orf = False
            orf = ""
            for i in range(0, len(sequence), 3):
                codon = sequence[i:i+3]
                if codon == start_codon:
                    orf += codon
                    inside_orf = True
                elif codon == stop_codon and inside_orf:
                    orf += codon
                    orfs.append(orf)
                    orf = ""
                    inside_orf = False
                elif set(stop_codons).isdisjoint(codon) and inside_orf: 
                    break
                elif inside_orf:
                    orf += codon
                elif orf != "" and not inside_orf:
                    break

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
translate_and_save_sequences(input_file, output_file)

