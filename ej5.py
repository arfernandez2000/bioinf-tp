import json
import argparse

from Bio import SeqIO
from Bio.SeqUtils import GC, MeltingTemp

def parse_args(): 
    parser = argparse.ArgumentParser(description='Ejercicio 5. Secuencia -> 5 Primers')
    parser.add_argument('-i', help='Input GenBank file (default = alzheimer.gb)', default='alzheimer.gb')
    parser.add_argument('-o', help='Output Primers file (default = outputs/ej5/primers.out)', default='outputs/ej5/primers.out')
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
    for i in range(config["num_primers"]):
        primer_length = config["primer_length"]
        gc_min = config["gc_min"]
        gc_max = config["gc_max"]
        tm_max = config["tm_max"]

        # Diseñar el primer
        start_index = i * (len(transcript_sequence) // config["num_primers"])
        end_index = start_index + primer_length
        primer_candidate = transcript_sequence[start_index:end_index]

        # Ajustar la GC del primer
        while GC(primer_candidate) < gc_min or GC(primer_candidate) > gc_max:
            start_index += 1
            end_index += 1
            primer_candidate = transcript_sequence[start_index:end_index]

        # Ajustar la temperatura de melting del primer
        # TODO: Fijarse que metodo para calcular la temperatura de melting usar
        while MeltingTemp.Tm_Wallace(primer_candidate) > tm_max:
            end_index -= 1
            primer_candidate = transcript_sequence[start_index:end_index]

        primer_list.append(primer_candidate)

    return primer_list

def main():
    # Parsear argumentos
    genbank_file, out_path, config_file = parse_args()

    # Cargar configuración desde el archivo JSON
    config = load_config(config_file)

    # Leer la secuencia del transcripto desde el archivo GenBank
    transcript_sequence = read_transcript_sequence(genbank_file)

    # Diseñar primers
    primers = design_primers(transcript_sequence, config)

    # Imprimir los primers diseñados
    for i, primer in enumerate(primers, 1):
        print(f"Primer {i}: {primer}")

if __name__ == "__main__":
    main()