from Bio.pairwise2 import format_alignment 
from Bio import pairwise2

from Bio import SeqIO
import argparse

import dir_helper as dirh

parser = argparse.ArgumentParser(description='Ejercicio 3. Proteins Fasta -> MultiSequence Alignment')
parser.add_argument('-i', metavar='FASTA_FILE', help='Input Fatsa file (default = inputs/msa_input.fas)', default='msa_input.fasta')
parser.add_argument('-o', metavar='MSA_FILE', help='Output MultiSequence Alignment file (TXT) (default = results/msa.txt)', default='results/msa.txt')
args = parser.parse_args()

input_file = args.i
output_file = args.o

dirh.create_output_dirs_from_file_path(output_file)

sequences = list(SeqIO.parse(open(input_file,'r'), 'fasta'))
original_seq = sequences[0].seq
with open(output_file, 'w') as save_file: 
    for i in range(1,len(sequences)):
        sequence = sequences[i].seq
        alignment = pairwise2.align.globalxx(original_seq, sequence)
        save_file.write(format_alignment(*alignment[-1]))
        save_file.write('\n')
