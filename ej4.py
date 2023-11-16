import os
import subprocess
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import dir_helper as dirh
import argparse

parser = argparse.ArgumentParser(description='Ejercicio 2. EMBOSS')
parser.add_argument('-i', help='Input Fasta file (default = results/secuencias_n.fasta)', default='results/secuencias_n.fasta')
parser.add_argument('-o', help='Output file (default = results/sequence.orf)', default='results/secuencias.orf')
parser.add_argument('-opc', help='Options orf or domain_analysis(default = orf)', default='orf')
args = parser.parse_args()

def run_emboss_getorf(input_fasta, output_aa):
    subprocess.run(["getorf", "-sequence", input_fasta, "-outseq", output_aa], check=True) 

def run_emboss_prosit(input_fasta, output):
    os.system(f"patmatmotifs -sequence {input_fasta} -outfile {output}")  
def change_file_permissions(file_path, mode):
    os.chmod(file_path, mode)

def main():
    new_mode = 0o755
    
    input_file = args.i
    output_file = args.o
    opc = args.opc
    dirh.create_output_dirs_from_file_path(output_file)
    if opc == "orf":
        change_file_permissions(input_file, new_mode)
        run_emboss_getorf(input_file, output_file)
    else:
        if opc == "domain":
            run_emboss_prosit(input_file,output_file)
    

if __name__ == "__main__":
    main()
