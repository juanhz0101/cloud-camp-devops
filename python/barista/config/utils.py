products_available = []
def get_menu():
  
  file_name = "menu.txt"

  if len(products_available) > 0:
    products_available.clear()
  # Abrir el archivo en modo lectura
  with open(file_name, 'r') as file:
      # Leer cada línea del archivo
      for line in file:
          # Eliminar los espacios en blanco al inicio y final de la línea
          line = line.strip()
          print("-----------------------")
          print(line)

          if line.split("|")[0] != "ID":
            product = { 
              "id": int(line.split("|")[0]), 
              "name": line.split("|")[1], 
              "price": float(line.split("|")[2]),
              "stock": int(line.split("|")[3])
              }
            products_available.append(product)
  
  return products_available

def get_product_by_id(product_id):
  
  exists = False
  product_finded = None
  for product in products_available:
    if product_id in product.values():
      product_finded = product
      exists = True
      break
    
  if exists:
    return product_finded
  else:
      raise ValueError("El producto seleccionado no está presente en el menu")
  
def get_receipt(order):
  total = 0
  print("Factura")
  print("-------")
  for item in order:
    print(f"{item['name']} | {item['units']} | {item['total']}")
    total += item['total']
  print(f"Total: {total}")
  print("-------")
  print("Gracias por su compra")
            