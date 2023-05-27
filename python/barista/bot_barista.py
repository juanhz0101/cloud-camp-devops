#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
print ("Hola, bienvenido a la cafeteria de camilo.")
nombre = input("Cual es tu nombre? \n")
#menu_stock = ["Cafe", "te", "agua"]
menu = "Cafe, te y agua"
orden = input("Hola " + nombre +" que deseas ordenar de nustro menu \n" + menu + "\n")
precio = 10

unidades = int (input("cuantas unidades deseas? \n"))
maxUnidades = 50

if unidades > maxUnidades:
  print("Lo lamentamos, pero solo tenemos" + str(maxUnidades) +"unidades de "+ orden)
else:
  valorTotal = precio * unidades
  print("El valor total de tu orden es: $", valorTotal, "USD")
  print(nombre+"tu "+ orden + "estara en un momento.")