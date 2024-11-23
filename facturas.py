import json
import clases_materias as clasesMateriasModule

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

def obtenerMorosos(facturas, alumnos, clases):
  '''
  Lista los alumnos morosos.
  Args:
    facturas: list - Lista de facturas.
    alumnos: list - Lista de alumnos.
    clases: list - Lista de clases.
  Returns:
    list - Lista de diccionarios con los alumnos morosos y la factura que moran.
  '''
  success, materias = clasesMateriasModule.abrirArchivoDeMaterias()
  if not success:
    print("No se pudo abrir el archivo de materias.")
    return
  
  morosos = []
  for factura in facturas:
    if not factura["pagada"]:
      print("No pagada")
      for alumno in alumnos:
        if factura["alumnoLU"] == alumno["LU"]:
          print("Es del alumno ", alumno["nombre"])
          for i in range(0, len(factura["clases"])):
            for clase in clases:
              ...
              if clase["id"] == factura["clases"][i]:
                for materia in materias:
                  if materia["id"] == clase["materiaId"]:
                    clase["materia"] = materia['nombre']
                    break
                factura["clases"][i] = clase
      factura["monto"] = len(factura["clases"]) * costo_por_clase
      morosos.append({"alumno": alumno, "factura": factura})
  return morosos

'''
{
  alumnoLU: 123,
  clases: [1, 2, 3],
  pagada: False
}
'''