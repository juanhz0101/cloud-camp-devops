#! /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
from config.utils import get_menu, get_product_by_id, get_receipt
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
            units = int(input("cuantas unidades deseas? \n"))
            if units > product_requested['stock']:
              print(f"No tenemos unidades las unidades que nos solicitas del producto: {product_requested['name']}, tenemos {product_requested['stock']} ")
            else:
              total_by_product = product_requested['price'] * units
              item = { "name": product_requested['name'], "units": units, "total": total_by_product }
              order.append(item)
            other_product = input("Deseas ordenar otro producto? (y/n) \n")
            if other_product == "n":
                break
        except ValueError:
            print("Por favor ingresa un ID valido")
      get_receipt(order)


