import os
import subprocess

def run_emboss_getorf(input_fasta, output_aa):
    subprocess.run(["getorf", "-sequence", input_fasta, "-outseq", output_aa], check=True)

def run_emboss_prosit(input_fasta, output):
    os.system(f"patmatmotifs -sequence {input_fasta} -outfile {output}.patmatmotifs")  
def change_file_permissions(file_path, mode):
    os.chmod(file_path, mode)

def main():
    new_mode = 0o755
    
    input_fasta = "results/sequence.fas"
    output_aa = "sequence.orf"
    #change_file_permissions(input_fasta, new_mode)
    #run_emboss_getorf(input_fasta, output_aa)
    run_emboss_prosit(input_fasta,"output")
    

if __name__ == "__main__":
    main()
