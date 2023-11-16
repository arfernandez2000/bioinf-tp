from Bio.Align.Applications import MafftCommandline

import argparse

import dir_helper as dirh

parser = argparse.ArgumentParser(
    description="Ejercicio 3. Proteins Fasta -> MultiSequence Alignment"
)
parser.add_argument(
    "-i",
    metavar="FASTA_FILE",
    help="Input Fatsa file (default = inputs/msa_input.fas)",
    default="inputs/msa_input.fasta",
)
parser.add_argument(
    "-o",
    metavar="MSA_FILE",
    help="Output MultiSequence Alignment file (TXT) (default = results/msa.txt)",
    default="results/msa.txt",
)
args = parser.parse_args()

input_file = args.i
output_file = args.o

dirh.create_output_dirs_from_file_path(output_file)


mafft_cline = MafftCommandline(
    thread=8, reorder=True, treeout=True, maxiterate=2, amino=True, input=input_file
)

stdout, stderr = mafft_cline()
open(output_file, "w").write(stdout)
