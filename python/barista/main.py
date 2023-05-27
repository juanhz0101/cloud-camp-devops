#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3

from factory import Factory

# Crear una instancia de la factoría
factory = Factory()


# Obtener la instancia deseada según la variante
print ("Hola, bienvenido a la cafeteria de camilo.")
name = input("Cual es tu nombre? \n")
role = "client"
instance = None
if name == "admin_12345678":
    role = "admin"
instance = factory.create_instance(role)
instance.init_process(name)

  
  
