import json
import argparse
import random

from Bio import SeqIO
from Bio.SeqUtils import GC, MeltingTemp
from Bio.SeqUtils import nt_search

def parse_args(): 
    parser = argparse.ArgumentParser(description='Ejercicio 5. Secuencia -> 5 Primers')
    parser.add_argument('-i', help='Input GenBank file (default = inputs/sequence.gb)', default='inputs/sequence.gb')
    parser.add_argument('-o', help='Output Primers file (default = primers.out)', default='primers.out')
    parser.add_argument('-c', help='Configuration file (default = config.json)', default='config.json')
    args = parser.parse_args()

    genbank_file = args.i
    out_path = args.o
    config_file = args.c

    return genbank_file, out_path, config_file

def load_config(config_file):
    with open(config_file, "r") as f:
        config = json.load(f)
    return config

# Lee la secuencia del transcripto desde un archivo GenBank
def read_transcript_sequence(genbank_file):
    record = SeqIO.read(genbank_file, "genbank")
    return str(record.seq)

def design_primers(transcript_sequence, config):
    primer_list = []

    num_primers = config["num_primers"]
    primer_length_min = config["primer_length_min"]
    primer_length_max = config["primer_length_max"]
    gc_min = config["gc_min"]
    gc_max = config["gc_max"]
    tm_max = config["tm_max"]
    gc_lock_length = 2


    while len(primer_list) < num_primers:
        # Calculo tamaño del primer y el índice de inicio y fin
        primer_length = random.randint(primer_length_min, primer_length_max)
        start_index = random.randint(0, len(transcript_sequence) - primer_length)
        end_index = start_index + primer_length

        # Obtengo el primer candidato
        primer_candidate = transcript_sequence[start_index:end_index]

        # Calculo porcentaje de GC
        gc_content = GC(primer_candidate)

        # Calculo temperatura de melting
        melting_temp = MeltingTemp.Tm_Wallace(primer_candidate)

        # Obtengo los ultimos 2 nucleotidos del primer
        last_nucleotides = primer_candidate[-gc_lock_length:]

        # Verifico que cumpla con las condiciones
        if (
            gc_content >= gc_min
            and gc_content <= gc_max
            and melting_temp <= tm_max
            and last_nucleotides.count("G") + last_nucleotides.count("C") == gc_lock_length
        ):
            primer_list.append(primer_candidate)

    return primer_list

def verify_primer():
     # Parsear argumentos
    genbank_file, out_path, config_file = parse_args()

    # Cargar configuración desde el archivo JSON
    config = load_config(config_file)

    # Leer la secuencia del transcripto
    transcript_sequence = read_transcript_sequence(genbank_file)

    # Leer del archivo por linea
    with open(out_path, "r") as f:
        for i in range(config["num_primers"]):
            primer = f.readline()
            primer = primer[0:len(primer)-1]

            occurrences = nt_search(transcript_sequence, primer)
            
            tm = MeltingTemp.Tm_GC(primer)
            
            gc_content = GC(primer)

            print("Primer: \n Ocurrencias: " + str(occurrences) + "\t Tm: " + str(tm) + "\t GC: " + str(gc_content))

def main():
    # Parsear argumentos
    genbank_file, out_path, config_file = parse_args()

    # Cargar configuración desde el archivo JSON
    config = load_config(config_file)

    # Leer la secuencia del transcripto
    transcript_sequence = read_transcript_sequence(genbank_file)

    # Diseñar primers
    primers = design_primers(transcript_sequence, config)

    # Guardar los primers en el archivo de salida
    f = open(out_path, "w")
    for primer in primers:
        f.write(str(primer) + "\n")
    f.close()

if __name__ == "__main__":
    main()