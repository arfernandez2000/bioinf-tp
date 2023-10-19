import argparse

parser = argparse.ArgumentParser(description='Ejercicio 2. Protein Fasta -> BLAST Report')
parser.add_argument('-i', help='Input Fasta file (default = outputs/ej1/protein.fas)', default='outputs/ej1/protein.fas')
parser.add_argument('-o', help='Output BLAST Report file (default = outputs/ej2/blast.out)', default='outputs/ej2/blast.out')
args = parser.parse_args()

fas_file = args.i
out_path = args.o