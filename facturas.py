import json

costo_por_clase = 50000

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


def marcarComoPagada(factura):
  '''
  Marca una factura como pagada.
  Args:
    factura: dict - Diccionario con los datos de la factura.
  Returns:
    bool - True si se pudo marcar, False si no.
  '''
  success, facturas = abrirArchivoFacturas()
  if not success:
    return False

  for f in facturas:
    if f["id"] == factura["id"]:
      f["pagada"] = True
      break

  return reescribirArchivoFacturas(facturas)

def listarMorosos(facturas, alumnos):
  '''
  Lista los alumnos morosos.
  Args:
    facturas: list - Lista de facturas.
    alumnos: list - Lista de alumnos.
  Returns:
    None
  '''
  morosos = []
  for alumno in alumnos:
    deuda = 0
    for factura in facturas:
      if factura["alumnoLU"] == alumno["LU"] and not factura["pagada"]:
        deuda += len(factura.clases) * costo_por_clase
    if deuda > 0:
      morosos.append({"LU": alumno["LU"], "nombre": alumno["nombre"],"apellido": alumno["apellido"], "deuda": deuda})
  return morosos

'''
{
  alumnoLU: 123,
  clases: [1, 2, 3],
  pagada: False
}
'''