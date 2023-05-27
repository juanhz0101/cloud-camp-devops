#!/bin/bash

# Obtener la fecha y hora actual
fecha=$(date +"%Y-%m-%d_%H-%M-%S")

# Nombre de la carpeta
carpeta="Carpeta_${fecha}"

# Comprobar si la carpeta ya existe
if [ -d "$carpeta" ]; then
  echo "La carpeta ya existe. Eliminando la carpeta existente..."
  rm -rf "$carpeta"
fi

# Crear la carpeta
mkdir "$carpeta"

# Cambiar al directorio de la carpeta
cd "$carpeta" || exit

# Crear 10 archivos con la fecha y hora de creación
for i in {1..10}; do
  archivo="Archivo_${i}_${fecha}.txt"
  echo "Fecha y hora de creación: $fecha" > "$archivo"
done

echo "Se ha creado la carpeta '$carpeta' con 10 archivos dentro."
