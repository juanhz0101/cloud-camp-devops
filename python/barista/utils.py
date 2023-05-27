products_available = []
def get_menu():
  
  file_name = "menu.txt"

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
  encontrado = False
  product_finded = None
  for product in products_available:
    if product_id in product.values():
      product_finded = product
      encontrado = True
      break
    
  if encontrado:
    print("El valor está presente en el array de diccionarios")
    return product_finded
  else:
      print("El valor no está presente en el array de diccionarios")
            