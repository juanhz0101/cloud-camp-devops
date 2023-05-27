#!/bin/bash

# Nombre del archivo de lista de compras
archivo_lista="lista_compras.txt"

# Arreglo para almacenar los elementos de la lista de compras
lista_compras=()

# Función para agregar elementos a la lista de compras
function agregar_a_lista {
  lista_compras+=("$1")
  echo "Se ha agregado '$1' a la lista de compras."
}

# Preguntar al usuario los elementos a agregar a la lista
echo "Bienvenido a la lista de compras!"
echo "Ingresa los elementos que deseas agregar (presiona Enter para finalizar):"

while true; do
  read -r elemento
  if [[ -z "$elemento" ]]; then
    break
  fi
  agregar_a_lista "$elemento"
done

# Guardar la lista de compras en el archivo
if [ ${#lista_compras[@]} -gt 0 ]; then
  echo "Guardando la lista de compras en el archivo '$archivo_lista'..."
  printf "%s\n" "${lista_compras[@]}" > "$archivo_lista"
  echo "La lista de compras se ha guardado exitosamente en el archivo."
else
  echo "La lista de compras está vacía. No se ha guardado ningún archivo."
fi
