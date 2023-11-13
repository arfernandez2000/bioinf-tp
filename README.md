# Trabajo Parctico - Introducción a la Bioinformática

Implementación de los ejercicios para el Trabajo Práctico de la materia. 

## Prerequisitos
Para el correcto funcionamiento del codgio se necesita:
- Instalar Python 3

## Ejercicios

### Ejercicio 2

Para ejecutar el ejercicio 2, se debe correr el siguiente comando:

```bash
./ej2.sh [-h] [-i I] [-o O] [-r]
```

Donde:
- h: Muestra el menú de ayuda.
- i: Especifica el archivo de entrada. Debe ser en formato .fasta o .fas
- o: Especifica el archivo de salida.
- r: Es un flag para correr BLAST remoto. De no estar, se corre localmente

**Explicación**

Primero se reciben los argumentos, que de estar vacios se usan los archivos defaults. Tanto para la ejecución local como remota se utiliza el comando ``blastp``, ya que se están comparando dos secuencias de aminoácidos. Al comando se le especifica que utilice la base de datos swissprot, que fue proporcionada por la catedra. Esto indica que se comparara la secuancia del archivo de entrada por cada una de las secuancias de la base de datos. Por ultimo, si se ejecuto con ``-r`` el comando se corre con el argumento ``-remote`` para utilice BLAST de manera remoto y no con el BLAST que pordría estar instalado en la computadora. 

El archivo de salida es un xml que tiene los siguientes tags relevantes: 
- ``<Hit>``:
- ``<Hsp_evalue>``:

Los hits estan ordenados de menor E-value a mayor, es decir de la secuancia mas parecida a la menos parecida en las comparaciones. 

### Ejercicio 3

Para ejecutar el ejercicio 3, se debe correr el siguiente comando:

```bash
python ej3.py [-h] [-i I] [-o O]
```

Donde:
- h: Muestra el menú de ayuda.
- i: Especifica el archivo de entrada. Debe ser en formato .fasta o .fas
- o: Especifica el archivo de salida.
