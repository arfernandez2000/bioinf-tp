import argparse

parser = argparse.ArgumentParser(description='Ejercicio 1. Nucleotide GenBank -> Protein FASTA')
parser.add_argument('-i', help='Input GenBank file (default = inputs/ej1/NM_001385125.gbk)', default='inputs/ej1/NM_001385125.gbk')
parser.add_argument('-o', help='Output Fatsa file (default = outputs/ej1/protein.fas)', default='outputs/ej1/protein.fas')
args = parser.parse_args()

gb_file = args.i
out_path = args.o