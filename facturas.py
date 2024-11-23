import json

def abrirArchivoFacturas():
  '''
  Abre el archivo json de las facturas
  Returns:
    list - Lista de diccionarios con las facturas.
  '''
  success = True
  
  try:
    file = open("data_facturas.json", "r", encoding='utf-8')
    facturas = json.load(file)
  except:
    print("No se encontró el archivo de datos de facturas.")
    success = False
    facturas = []
  finally:
    try:
      file.close()
    except:
      pass
  return success, facturas

def reescribirArchivoFacturas(facturas):
  '''
  Reescribe el archivo data_facturas.json con las facturas actualizados.
  Args:
    facturas: list - Lista de facturas.
  Returns:
    bool - True si se pudo guardar, False si no.
  '''
  success = True
  try:
    file =  open("data_facturas.json", "w", encoding='utf-8')
    json.dump(facturas, file, ensure_ascii=False, indent=4)
  except:
    return False
  finally:
    try:
      file.close()
    except:
      pass 

  return success
