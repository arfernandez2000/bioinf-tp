#!/bin/bash
Help()
{
   # Display Help
   echo "Usage: ej2.sh [-h] [-i FASTA_FILE] [-o OUTPUT_BLAST_FILE] [-r] [-s]"
   echo
   echo "Ejercicio 2. Protein Fasta -> BLAST Report"
   echo
   echo "optional arguments:"
   echo " -h        Show this help message and exit"
   echo " -i I      Input Fasta file (default = outputs/ej1/protein.fas)"
   echo " -o O      Output BLAST Report file (default = outputs/ej2/blast.out)"
   echo " -r        Remote run. If not present, run locally"
}

input="secuencias.fasta"
output="blast.out"
remote=false
update=true
while getopts ":h :s :r i: o:" flag
do
    case "${flag}" in
        h)
            Help
            exit;;
        i) input=${OPTARG};;
        o) output=${OPTARG};;
        r) remote=true;;
        s) update=false;;
        
    esac
done

if $remote
then
    echo "Running remote BLAST..."
    blastp -db swissprot -query $input -out $output -outfmt 5 -remote
    echo "Done"
else
    echo "Running local BLAST..."
    blastp -db swissprot -query $input -out $output -outfmt 5
    echo "Done"
fi