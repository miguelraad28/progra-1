import json
import clases_materias as clasesMateriasModule
from variables import costo_por_clase, archivo_facturas

def abrirArchivoFacturas():
  '''
  Abre el archivo json de las facturas
  Returns:
    list - Lista de diccionarios con las facturas.
  '''
  success = True
  
  try:
    file = open(archivo_facturas, "r", encoding='utf-8')
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
    file =  open(archivo_facturas, "w", encoding='utf-8')
    json.dump(facturas, file, ensure_ascii=False, indent=4)
  except:
    return False
  finally:
    try:
      file.close()
    except:
      pass 

  return success


def marcarComoPagada(alumnoLU):
  '''
  Marca una factura como pagada.
  Args:
    alumnoLU: number - LU del alumno para marcar su factura como pagada.
  Returns:
    bool - True si se pudo marcar, False si no.
  '''
  success, facturas = abrirArchivoFacturas()
  if not success:
    return False

  facturaPagada = None

  for f in facturas:
    if f["alumnoLU"] == alumnoLU:
      facturaPagada = f
      if f["pagada"] == True:
        print('La factura ya está pagada.')
      else:
        f["pagada"] = True
      break

  reescribirArchivoFacturas(facturas)

  return facturaPagada

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
      
      alumnoConFacturaImpaga = None
      
      for alumno in alumnos:
        if factura["alumnoLU"] == alumno["LU"]:
          factura = expandirDatosFactura(factura, clases, materias)
          
          alumnoConFacturaImpaga = alumno
          
      factura["monto"] = len(factura["clases"]) * costo_por_clase
      morosos.append({"alumno": alumnoConFacturaImpaga, "factura": factura})
  return morosos

def expandirDatosFactura(factura, clases, materias):
  '''
  Expande los datos de una factura agregando información detallada de las clases y materias.
  ARGS:
    factura (dict): Diccionario que contiene la información de la factura, incluyendo una lista de IDs de clases.
    clases (list): Lista de diccionarios con información de las clases, cada uno con un ID y un ID de materia.
    materias (list): Lista de diccionarios con información de las materias, cada uno con un ID y un nombre.
  Retorna:
    dict: La factura actualizada con información detallada de las clases y materias.
  '''
  for i in range(0, len(factura["clases"])):
    for clase in clases:
      ...
      if clase["id"] == factura["clases"][i]:
        for materia in materias:
          if materia["id"] == clase["materiaId"]:
            clase["materia"] = materia['nombre']
            break
        factura["clases"][i] = clase
        
  return factura

def verUltimaFacturaPorLU(facturas, lu, clases):
  '''
  Muestra la última factura de un alumno.
  Args:
    facturas: list - Lista de facturas.
    lu: int - LU del alumno.
  Returns:
    dict - Diccionario con la última factura del alumno.
  '''
  success, materias = clasesMateriasModule.abrirArchivoDeMaterias()
  
  if not success:
    print("No se pudo abrir el archivo de materias.")
    return
  
  ultimaFactura = None

  for factura in facturas:
    if factura["alumnoLU"] == lu:
      ultimaFactura = expandirDatosFactura(factura, clases, materias)
      ultimaFactura["monto"] = len(ultimaFactura["clases"]) * costo_por_clase

  return ultimaFactura