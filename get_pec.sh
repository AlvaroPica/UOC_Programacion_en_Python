#!/bin/bash

PEC_PATH=/home/alvaro/Escritorio/UOC/Curso_Python

echo -ne "Por favor, indica el número de PEC que quieres descargar: "
read input
if [ $input -eq $input 2>/dev/null ]
then
    echo "Se va a proceder a descargar la PEC $input..."
    cd $PEC_PATH
    if [ ! -d "$PEC_PATH/prog_datasci_${input}" ]; then
        git clone https://eimtgit.uoc.edu/prog_datasci/prog_datasci_${input}.git    
        echo "Descarga realizada en $PEC_PATH/prog_datasci_${input}"
    else
        echo "Error: el directorio $PEC_PATH/prog_datasci_${input} ya existe."
    fi
else
    echo "Error: $input no es un número válido de PEC"
fi
