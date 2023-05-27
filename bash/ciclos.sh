#!/bin/bash

# Ejemplo de bucle "for"
echo "Bucle 'for':"
for i in {1..5}; do
  echo "Iteración $i"
done

echo

# Ejemplo de bucle "while"
echo "Bucle 'while':"
counter=1
while [ $counter -le 5 ]; do
  echo "Iteración $counter"
  ((counter++))
done

echo

# Ejemplo de bucle "until"
echo "Bucle 'until':"
counter=1
until [ $counter -gt 5 ]; do
  echo "Iteración $counter"
  ((counter++))
done
