import argparse

parser = argparse.ArgumentParser(description='Ejercicio 3. Proteins Fasta -> MultiSequence Alignment')
parser.add_argument('-i', metavar='FASTA_FILE', help='Input Fatsa file (default = inputs/ej3/msa_input.fas)', default='inputs/ej3/msa_input.fas')
parser.add_argument('-o', metavar='MSA_FILE', help='Output MultiSequence Alignment file (TXT) (default = outputs/ej3/msa_results.txt)', default='outputs/ej3/msa_results.txt')
args = parser.parse_args()

fas_file = args.i
out_path = args.o