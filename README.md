# Trabajo Parctico - Introducción a la Bioinformática

Implementación de los ejercicios para el Trabajo Práctico de la materia. 

## Prerequisitos
Para el correcto funcionamiento del codgio se necesita:
- Instalar Python 3
- Instalar mafft

### Instalar mafft

En MacOS:

```bash
brew install mafft
```

En Ubuntu:

```bash
sudo apt-get update
sudo apt-get install mafft
```

## Ejercicios 1
Para ejecutar el ejercicio 1, se debe correr el siguiente comando:

```bash
./ej1.py [-h] [-i I] [-o O]
```

Donde:
- h: Muestra el menú de ayuda.
- i: Especifica el archivo de entrada. Debe ser en formato .gb o .gbk y ser una secuencia de nucleótidos
- o: Especifica el archivo de salida en formato fasta.

### Ejercicio 2

Para ejecutar el ejercicio 2, se debe correr el siguiente comando:

```bash
./ej2.sh [-h] [-i I] [-o O] [-r] [-n] [-f F]
```

Donde:
- h: Muestra el menú de ayuda.
- i: Especifica el archivo de entrada. Debe ser en formato .fasta o .fas y ser una secuencia de aminoácidos
- o: Especifica el archivo de salida.
- r: Es un flag para correr BLAST remoto. De no estar, se corre localmente
- n: Es un flag para correr BLAST remoto pero con la base de datos de NCBI
- f: Especifica el archivo de entrada cuando se corre con el tag *n*. Debe ser en formato .fasta o .fas y ser una secuencia de nucleótidos

**Explicación**

Para ejecutar los comandos de BLAST, se reciben argumentos, que si están vacíos, se utilizan los archivos predeterminados. Se utiliza el comando ``blastp`` tanto para la ejecución local como remota, ya que se están comparando secuencias de aminoácidos. Se especifica que utilice la base de datos swissprot proporcionada por la cátedra, lo que implica comparar la secuencia del archivo de entrada con cada secuencia en la base de datos.

Al ejecutar con el flag ``-n``, se realiza la ejecución remota contra la base de datos NCBI utilizando el archivo especificado después del tag ``-f``. Además, al tratarse de secuencias de nucleótidos, se utiliza el comando ``blastn``.

El archivo de salida es un archivo XML que contiene toda la información de los resultados encontrados por BLAST. Los resultados se ordenan desde las mejores comparaciones hasta las peores, teniendo en cuenta el E-value del alineamiento. 


### Ejercicio 3

Para ejecutar el ejercicio 3, se debe correr el siguiente comando:

```bash
python ej3.py [-h] [-i I] [-o O]
```

Donde:
- h: Muestra el menú de ayuda.
- i: Especifica el archivo de entrada. Debe ser en formato .fasta o .fas
- o: Especifica el archivo de salida.

**Explicación**

A partir de los resultados obtenidos en el Ejercicio 2, se seleccionaron los 10 mejores y se generó un archivo llamado **msa_input.fasta** dentro de la carpeta *inputs*. En caso de no especificarse otra entrada, este archivo se utiliza como predeterminado.

El código emplea la función ``MafftCommandline()`` de Biopython, que actúa como un envoltorio para MAFFT (Multiple Alignment using Fast Fourier Transform). Este comando no solo realiza el alineamiento, sino que también, al incluir el parámetro ``treeout=True``, genera un archivo llamado **msa_input.fasta.tree** que contiene el árbol filogenético calculado por el programa. 

## Ejercicios 4
Para ejecutar el ejercicio 4, se debe correr el siguiente comando:

```bash
./ej2.py [-h] [-i I] [-o O] [-opc OPC]
```

Donde:
- h: Muestra el menú de ayuda.
- i: Especifica el archivo de entrada. Debe ser en formato .gb o .gbk y ser una secuencia de nucleótidos
- o: Especifica el archivo de salida en formato fasta.
- opc: Especifica la opcion de analisis - calcular orf: orf - analisis de dominio de datos con la bd de PROSITE: domain 

### Ejercicio 5

Para ejecutar el ejercicio 5, se debe correr el siguiente comando:

```bash
python ej5.py [-i I] [-o O] [-c C]
```

Donde:
- i: Especifica el archivo de entrada. Debe ser en formato .fasta o .fas
- o: Especifica el archivo de salida.
- c: Especifica el archivo de configuración. Debe ser en formato .gb

**Explicación**
A partir de una secuencia, se diseña primers. Los criterios tomados en cuenta para este diseño son la cantidad de pares de bases, el porcentaje de GC, la temperatura de melting y el GC-lock.

Para su implementación, se utilizaron funciones de la librería de BioPython.