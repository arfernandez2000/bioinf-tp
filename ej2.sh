#!/bin/bash
Help()
{
    # Display Help
    echo "Usage: ej2.sh [-h] [-i I] [-o O] [-r]"
    echo
    echo "Ejercicio 2. Protein Fasta -> BLAST Report"
    echo
    echo "optional arguments:"
    echo " -h        Show this help message and exit"
    echo " -i I      Input Fasta file (default = results/secuencias.fasta)"
    echo " -o O      Output BLAST Report file (default = results/blast.out)"
    echo " -r        Remote run. If not present, run locally"
    echo " -f F      Input Fasta file for nucleotides (default = results/AY792511.1/sequence.fas)"
    echo " -n        Compares nucleotides agains ncbi database"
}

input="results/secuencias.fasta"
nucleotideInput="results/secuencias_n.fasta"
output="results/blast.out"
remote=false
update=true
remoteNucleotides=false
while getopts ":h :s :r :n i: o: f:" flag
do
    case "${flag}" in
        i) input=${OPTARG} ;;
        o) output=${OPTARG} ;;
        r) remote=true ;;
        s) update=false ;;
        f) nucleotideInput=${OPTARG} ;;
        n) remoteNucleotides=true ;;
        *)
            Help
            exit ;;
    esac
done

if $remoteNucleotides
then
    echo "Compares nucleotides agains remote BLAST..."
    echo "$output"
    blastn -db nt -query "$nucleotideInput" -out "$output" -outfmt 5 -remote
    echo "Done"
elif "$remote"
then
    echo "Running remote BLAST..."
    blastp -db swissprot -query "$input" -out "$output" -outfmt 5 -remote
    echo "Done"
else
    echo "Running local BLAST..."
    blastp -db swissprot -query "$input" -out "$output" -outfmt 5
    echo "Done"
fi
