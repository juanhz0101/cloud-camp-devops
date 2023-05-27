#!/bin/bash

# Declaración de un arreglo
arreglo=("Manzana" "Banana" "Naranja" "Pera")

# Acceder a elementos individuales del arreglo
echo "El primer elemento del arreglo es: ${arreglo[0]}"
echo "El segundo elemento del arreglo es: ${arreglo[1]}"

# Imprimir todos los elementos del arreglo
echo "Todos los elementos del arreglo son: ${arreglo[@]}"
