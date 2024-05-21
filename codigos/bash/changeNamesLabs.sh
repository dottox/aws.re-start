#!/bin/bash
# Cambiar los nombres de archivos en un directorio.
# Colocar acá la ruta con: ruta=nombreRuta
listaArchivos=$(ls $ruta)

for word in $listaArchivos
do
  numero=${word:4:3}
  tamano=${#word}
  if [ $tamano -ge 15 ]
  then
    mv $ruta/$word $ruta/"${numero}-lab-notUploaded.pdf"
  else
    mv $ruta/$word $ruta/"${numero}-lab.pdf"
  fi
done

echo "Finished"
