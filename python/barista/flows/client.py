#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
from utils import get_menu, get_product_by_id
class Client:
    def init_process(self, name = ''):
      print(f"Hola, {name} que deseas ordenar del menu.")
      
      order = []

      while True:
        
        try: 
            get_menu()
            product_id = int(input("Que deseas ordenar, selecciona un ID valido por favor\n"))
            product_requested = get_product_by_id(product_id)
            print(f"El producto que deseas ordenar es {product_requested['name']}")
            #indice = products_available.index(product_id)
            #print(f"El valor {product_id} se encuentra en el índice {indice} del array")
            """
            units = int(input("cuantas unidades deseas? \n"))
            item = { "id": product_id, "units": units }
            order.append(item) """
            other_product = input("Deseas ordenar otro producto? (y/n) \n")
            if other_product == "n":
                break
        except ValueError:
            print("El valor no está presente en el array")
      print(order)


