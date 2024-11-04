import random
import re
import json

# Alumnos

nombres = [
  "Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Marta", 
  "José", "Lucía"
]

apellidos = [
  "García", "Martínez", "Rodríguez", "López", "González", "Pérez", "Sánchez", 
  "Ramírez", "Torres", "Flores"]

#Alumno que creamos para testing.
alumnos = [{
      "nombre": "Miguel",
      "apellido": "Raad",
      "DNI": 95656210,
      "LU": 1200447,
      "email": "miguelraad2020@gmail.com",
      "clases": [],
      "estado": 'Activo',
    }]

def generarAlumnos(cantidad):
  '''
  Genera una lista de alumnos con nombres, apellidos, DNI y legajos aleatorios para inicializar el programa con datos en memoria.
  Args:
    int - cantidad: Cantidad de alumnos a generar.
  Returns:
    list - Lista de diccionarios con los datos de los alumnos
  '''
  
  while len(alumnos) < cantidad:
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    
    #Asigna un valor para DNI y se asegura que el mismo sea unico
    dniGenerado = random.randint(30000000, 45000000)
    while dniGenerado in [alumno["DNI"] for alumno in alumnos]:
      dniGenerado = random.randint(300000, 45000000)

    #Asigna un valor de legajo y se asegura que el mismo sea unico  
    legajoGenerado = random.randint(800000, 1200000)
    while legajoGenerado in [alumno["LU"] for alumno in alumnos]:
      legajoGenerado = random.randint(800000, 1200000)
    
    # Ya el legajo es único asi que por lo tanto el email también.
    mailGenerado = str(f"{nombre[0].lower()}{apellido.lower()}.{legajoGenerado}@edau.edu.ar")
    print("**nombre")
    print(nombre)
    alumno = {
      "nombre": nombre,
      "apellido": apellido,
      "DNI": dniGenerado,
      "LU": legajoGenerado,
      "email": mailGenerado,
      "clases": [],
      "estado": 'Activo',
    }
    alumnos.append(alumno)

  return alumnos

# Uso dentro del programa
def abrirArchivoAlumnos():
  '''
  Abre el archivo de datos de alumnos
  Returns:
    list - Lista de diccionarios con los datos de los alumnos.
  '''
  success = True
  
  try:
    file = open("data_alumnos.json", "r", encoding='utf-8')
    alumnos = json.load(file)
  except:
    print("No se encontró el archivo de datos de alumnos.")
    alumnos = []
    success = False
  finally:
    try:
      file.close()
    except:
      pass
  return success, alumnos

def reescribirArchivoAlumnos(alumnos):
  '''
  Reescribe el archivo data_alumnos.json con los alumnos actualizados.
  Args:
    alumnos: list - Lista de alumnos.
  Returns:
    bool - True si se pudo guardar, False si no.
  '''
  success = True
  try:
    file =  open("data_alumnos.json", "w", encoding='utf-8')
    json.dump(alumnos, file, ensure_ascii=False, ident=4)
  except:
    return False
  finally:
    try:
      file.close()
    except:
      pass 

  return success

def listarAlumnos(alumnos):
  """
  Lista los alumnos activos y muestra su información detallada.
  Args:
    alumnos (list): Una lista de diccionarios, donde cada diccionario representa un alumno
  Returns:
    None
  """
  
  numeroDeActivos = 0 
  for alumno in alumnos:
    if alumno['estado'] == 'Activo':
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print(f"Email: {alumno["email"]}")
      print("_________________________")
      print("")
      numeroDeActivos += 1
    
  print(f"Alumnos activos totales: {numeroDeActivos}")
  return

def listarAlumnosInactivos(alumnos):
  '''
  Devuelve la lista completa de alumnos inactivos en el sistema. 
  Args:
      alumnos: list - Lista de alumnos (activos e inactivos)
  Returns:
      None
  '''
  encontradosInactivos = 0
  for alumno in alumnos:
    if alumno['estado'] == 'Inactivo':
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print(f"Email: {alumno["email"]}")
      print("_")
      print("")
      encontradosInactivos += 1
  print(f"Alumnos inactivos totales: {encontradosInactivos}")
  return

def nuevoAlumno(nombre, apellido, dni, alumnos):
  '''
  Crea un nuevo alumno y lo agrega a la lista de alumnos.
  Args:
    nombre: str - Nombre del alumno.
    apellido: str - Apellido del alumno.
    dni: int - DNI del alumno.
    alumnos: list - Lista de alumnos a la que se le agregará el nuevo alumno.
  Returns:
    list - La lista de alumnos con el nuevo alumno agregado
  '''
  legajoGenerado = random.randint(800000, 1200000)
    
  while legajoGenerado in [alumno["LU"] for alumno in alumnos]:
    legajoGenerado = random.randint(800000, 1200000)
  email = generarEmail(nombre, apellido, legajoGenerado)

  alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "DNI": dni,
    "LU": legajoGenerado,
    "email": email,
    "clases": [],
    "estado": 'Activo'
  }

  alumnos.append(alumno)

  return alumnos

def generarEmail(nombre, apellido, legajo):
  """
  Genera un email a partir del nombre, apellido y legajo del alumno utilizando expresiones regulares para evitar caracteres especiales.
  Args:
    nombre (str): El nombre del alumno.
    apellido (str): El apellido del alumno.
    legajo (int): El número de legajo del alumno.
  Returns:
    str: El email generado en el formato 'napellido.legajo@edau.edu.ar'.
  """
  nombreSinEspaciosYLimpio = re.sub(r'[^a-zA-Z]', '', nombre).lower()
  apellidoSinEspaciosYLimpio = re.sub(r'[^a-zA-Z]', '', apellido).lower()
  mail = f"{nombreSinEspaciosYLimpio[0]}{apellidoSinEspaciosYLimpio}.{legajo}@edau.edu.ar"

  return mail

def modificarAlumnoPorLU(LU, propiedad, nuevoValor, alumnos):
  """
  Modifica una propiedad específica (nombre o apellido) de un alumno en una lista de alumnos, 
  identificándolo por su LU (Legajo Universitario).
  Args:
    LU (int): El Legajo Universitario del alumno a modificar.
    propiedad (str): La propiedad a modificar, debe ser "nombre" o "apellido".
    nuevoValor (str): El nuevo valor para la propiedad especificada.
    alumnos (list): Lista de diccionarios que representan a los alumnos, 
            donde cada diccionario contiene las claves "LU", "nombre" y "apellido".
  Returns:
    list: La lista de alumnos con la modificación aplicada, si se encontró el alumno y la propiedad es válida.
        Si no se encontró el alumno o la propiedad no es válida, se devuelve la lista original sin cambios.
  """
  
  if propiedad not in ["nombre", "apellido"]:
    print("Solo se permite modificar el nombre o apellido.")
    return alumnos
  
  for alumno in alumnos:
    if alumno["LU"] == LU:
      alumno[propiedad] = nuevoValor
      return alumnos
  print("No se encontró un alumno con el LU ingresado.")
  return alumnos

def encontrarPorLegajo(alumnos):
  """
  Busca un alumno en la lista de alumnos por su legajo y estado activo.
  Args:
    alumnos (list): Lista de diccionarios que representan a los alumnos. 
            Cada diccionario contienen las claves "LU" (legajo) y "estado".
  Returns:
    list: Una lista que contiene dos elementos:
        - Un booleano que indica si el alumno fue encontrado.
        - Un diccionario con los datos del alumno encontrado, o un diccionario vacío si no se encontró.
  """
  
  legajo = int(input("Ingrese el legajo del alumno: "))
  
  encontrado = False
  alumnoEncontrado = {}
  
  for alumno in alumnos:
    if alumno["LU"] == legajo and alumno['estado'] == 'Activo':
      encontrado = True
      alumnoEncontrado = alumno   
  return [encontrado, alumnoEncontrado]

def encontrarPorDni(dni):
  '''
  Busca alumnos por DNI
  Args: 
    dni: int - DNI del alumno a buscar.
  Returns:
    dict - Diccionario con los datos del alumno encontrado, o None si no se encontró.
  '''
  alumnoEncontrado = None
  for alumno in alumnos:
    if alumno["DNI"] == dni and alumno['estado'] == 'Activo':
      alumnoEncontrado = alumno
  return alumnoEncontrado

def borrarAlumnoLogico(LU, alumnos):
    #RELACIONAR CON FACTURAS CAMBIAR NOMBRE DE ACTIVAR Y DESACTIVAR. 
    encontrado = False
    for alumno in alumnos:
        if alumno["LU"] == LU and alumno["estado"] == "Activo":
            alumno["estado"] = "Inactivo"
            print(f"El alumno con LU {LU} ha sido marcado como Inactivo.")
            encontrado = True
            alumno["clases"] = []
            break
        elif alumno["LU"] == LU and alumno["estado"] == "Inactivo":
          print(f"El alumno con LU {LU} ya se encuentra inactivo.")
          encontrado = True
          break
    if not encontrado:  
          print(f"No se encontró un alumno con el LU {LU}.")
    return alumnos

def pedirDniNuevoAlumno():
    '''
    Solicita al usuario que ingrese un DNI para un nuevo alumno y valida que sea un número positivo,
    que tenga entre 7 y 8 dígitos, y que no esté ya en uso.
    Returns:
      int: El DNI válido ingresado por el usuario.
    '''
    while True:
      dni = int(input("Ingrese el DNI del alumno: "))
      if dni <= 0:
          print("El DNI debe ser un número positivo.")
          continue
      if len(str(dni)) < 7 or len(str(dni)) > 8:
          print("El DNI debe tener entre 7 y 8 dígitos.")
          continue

      encontrado = encontrarPorDni(dni)
      if encontrado: 
        print("El dni ingresado ya está en uso")
      else:
          return dni 

def chequeaLegajo(alumnos):
  '''
  Pide el legajo y comprueba que sea valido, si no lo es o no corresponde a un alumno pide de vuelta,
  si lo es devuelve legajo y alumno
  Args:
    alumnos: list - Lista de alumnos.
  Returns:
    dict - Diccionario con los datos del alumno.
    int - Legajo del alumno.
  '''
  while True:
    legajo = int(input("Ingrese el legajo del alumno: "))

    if 0 < legajo < 9999999:
      alumno_encontrado = False
      for alumno in alumnos:
        if legajo == alumno["LU"]:
          alumno_encontrado = alumno
          break

      if not alumno_encontrado:
        print("El legajo no coincide con ningun alumno.")
    else:
      print("El legajo debe ser un número entre 1 y 9,999,999.")

    if alumno_encontrado:
      break
  return alumno_encontrado, legajo          

if __name__ == "__main__":
  print(len(alumnos))
  print(nuevoAlumno("Juan", "Pérez", 45222555, alumnos))
  print(modificarAlumnoPorLU(800000, "nombre", "Juan Pablo", alumnos))