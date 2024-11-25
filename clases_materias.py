import random
import alumnos as alumnosModule
import re
import json
from variables import dias, turnos, cuatrimestres, archivo_clases, archivo_materias

# Materias & Clases

# Lista de materias con identificadores únicos y nombres de las asignaturas disponibles en el sistema.
def abrirArchivoDeMaterias():
  '''
  Abre el archivo json de las materias
  Returns:
    list - Lista de diccionarios con las materias.
  '''
  success = True
  try:
    file = open(archivo_materias, "r", encoding='utf-8')
    materias = json.load(file)
  except:
    print("No se encontró el archivo de datos de materias.")
    success = False
    materias = []
  finally:
    try:
      file.close()
    except:
      pass
  return success, materias

def generarClases(cantidad):
  '''
  Genera una lista de clases basado en las materias que tenemos al inicio del modulo de manera aleatoria para inicializar el programa con datos en memoria.
  '''
  success, materias = abrirArchivoDeMaterias()
  if not success:
    print("No se encontraron materias.")
    return
  
  clases = []
  for i in range(cantidad):
    clase = {
      "id": 1000 + i,
      "dia": random.choice(dias),
      "turno": random.choice(turnos),
      "anio": "2024",
      "cuatrimestre": random.choice(cuatrimestres),
      "materiaId": random.choice(materias)["id"],
      "estado":"Activa"
    }
    clases.append(clase)
  return clases

# Funciones de uso en el programa
def abrirArchivoClases():
  '''
  Abre el archivo json de las clases
  Returns:
    list - Lista de diccionarios con las clases.
  '''
  success = True
  
  try:
    file = open(archivo_clases, "r", encoding='utf-8')
    clases = json.load(file)
  except:
    print("No se encontró el archivo de datos de clases.")
    success = False
    clases = []
  finally:
    try:
      file.close()
    except:
      pass
  return success, clases

def reescribirArchivoClases(clases):
  '''
  Reescribe el archivo data_clases.json con las clases actualizados.
  Args:
    clases: list - Lista de clases.
  Returns:
    bool - True si se pudo guardar, False si no.
  '''
  success = True
  try:
    file =  open(archivo_clases, "w", encoding='utf-8')
    json.dump(clases, file, ensure_ascii=False, indent=4)
  except:
    return False
  finally:
    try:
      file.close()
    except:
      pass 

  return success


def crearClase(clases):
  '''
  Crea una nueva clase y la agrega a la lista de clases.
  ARGS:
    clases: lista - Lista de clases a la que se le agregará la nueva clase.
    materias: list - Lista de materias disponibles para seleccionar la materia de la clase.
  
  '''
  if len(clases) > 0:
    nuevoId = clases[-1]["id"] + 1
  else:
    nuevoId = 1000

    # Validar día de dictado
  while True:
    diaInput = input("Ingrese el día de dictado de la clase (0: Lunes, 1: Martes, 2: Miércoles, 3: Jueves, 4: Viernes): ").strip()
    if not diaInput:
      print("El campo no puede estar vacío. Por favor, ingrese un valor válido.")
      continue
    if diaInput.isdigit() and 0 <= int(diaInput) <= 4:
      diaInput = int(diaInput)
      break
    else:
      print("Opción inválida. Por favor, ingrese un valor entre 0 y 4.")

  # Validar turno
  while True:
    turnoInput = input("Ingrese el turno de la clase (0: Mañana, 1: Tarde, 2: Noche): ").strip()
    if not turnoInput:
      print("El campo no puede estar vacío. Por favor, ingrese un valor válido.")
      continue
    if turnoInput.isdigit() and 0 <= int(turnoInput) <= 2:
      turnoInput = int(turnoInput)
      break
    else:
      print("Opción inválida. Por favor, ingrese un valor entre 0 y 2.")

  # Validar ID de la materia
  while True:
      print("")
      print("Listado materias: ")
      print("_____________________")

      success, materias = abrirArchivoDeMaterias()
      
      if not success:
        print("No se encontraron materias.")
        return
      
      for materia in materias:
          print(f"{materia['id']}: {materia['nombre']}")
      try:
        id = int(input("Ingrese el ID de la materia de la clase a crear: "))
        if 1 <= id <= 10: # Acá forzamos un poco la validación del id de la materia basada en las que tenemos preescritas en el código.
            break
        else:
            print("ID invalido, por favor ingrese un ID correcto (entre 1 y 10)")
      except Exception as ex: 
        print(f"Error al ingresar el ID de la materia: {ex}")
        

  claseNueva = {
    "id": nuevoId,
    "dia": diaInput, 
    "turno": turnoInput,
    "anio": "2024",
    "cuatrimestre": 1, # Por defecto, siempre se crea en el 2do cuatrimestre (n° 1).
    "materiaId": id,
    "estado":"Activa"
  }
  
  clases.append(claseNueva)
  materia_nombre = "Desconocida"
  for materia in materias:
    if materia['id'] == claseNueva["materiaId"]:
      materia_nombre = materia['nombre']
      break  
  print(f"Clase creada satisfactoriamente: \nID materia: {nuevoId}, \nNombre materia: {materia_nombre}, \nDía: {dias[claseNueva['dia']]}, \nTurno: {turnos[claseNueva['turno']]}")
  return claseNueva

def buscarClasePorId(clases, id):
  for clase in clases:
    if clase["id"] == id:
      return clase
  return None

def numeroValido(entrada, rango):
  '''
  Verifica si la entrada es un número dentro del rango especificado
  retorna: bool
  '''
  return re.match(r'^[0-9]+$', entrada) and (0 <= int(entrada) <= rango)

def modificarClase(clases):
  while True:
    id_input = input("Ingrese el ID de la clase que desea modificar: ").strip()
    if not id_input:  # Validar si está vacío
      print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
      continue
    if not id_input.isdigit():  # Validar si no es un número
      print("El ID debe ser un número entero. Por favor, intente nuevamente.")
      continue
    id = int(id_input)  # Convertir a entero si es válido
    break
  claseEncontrada = buscarClasePorId(clases, id)
  
  success, materias = abrirArchivoDeMaterias()
  
  if not success:
    print("No se encontraron materias.")
    return
  
  if claseEncontrada:
    nombreMateria = "Desconocida"
    for materia in materias:
      if materia['id'] == claseEncontrada["materiaId"]:
        nombreMateria = materia['nombre']
        break
    print(f"Clase encontrada: \nID materia: {claseEncontrada['id']}, \nNombre materia: {nombreMateria}, \nDía: {dias[claseEncontrada['dia']]}, \nTurno: {turnos[claseEncontrada['turno']]}, \nCuatrimestre: {cuatrimestres[claseEncontrada['cuatrimestre']]}") 

    while True:
      nuevoDia = input("Ingrese el nuevo día de la clase (0: Lunes, 1: Martes, 2: Miércoles, 3: Jueves, 4: Viernes): ")
      if nuevoDia == "":  # Si se presiona Enter, no se cambia el día
        break
      if numeroValido(nuevoDia, 4):
        claseEncontrada["dia"] = int(nuevoDia)
        break
      else:
        print("Opción inválida. Ingrese un día válido (0: Lunes, 1: Martes, 2: Miércoles, 3: Jueves, 4: Viernes): ")

    while True:
      nuevoTurno = input("Ingrese el nuevo turno de la clase (0: Mañana, 1: Tarde, 2: Noche): ")
      if nuevoTurno == "":  # Si se presiona Enter, no se cambia el turno
        break
      if numeroValido(nuevoTurno,2):
        claseEncontrada["turno"] = int(nuevoTurno)
        break
      else:
        print("Opción inválida. Ingrese un turno válido (0: Mañana, 1: Tarde, 2: Noche).")
    print(f"Clase actualizada: \nID materia: {claseEncontrada['id']}, \nNombre materia: {nombreMateria}, \nDía: {dias[claseEncontrada['dia']]}, \nTurno: {turnos[claseEncontrada['turno']]}, \nCuatrimestre: {cuatrimestres[claseEncontrada['cuatrimestre']]}")
  else:
    print("No se encontró una clase con el ID ingresado.")

def eliminarClase(clases, alumnos):
    '''
    Elimina clase de la lista de clases, elimina la clase del array clases de los alumnos. 
    Args:
        clases: List - lista de clases.
        alumnos: List - lista de alumnos.
    Returns:
        None
    '''
    while True:
        id_input = input("Ingrese el ID de la clase que desea eliminar: ").strip()
        if not id_input:  # Validar si está vacío
            print("El ID no puede estar vacío. Por favor, ingrese un valor válido.")
            continue
        if not id_input.isdigit():  # Validar si no es un número
            print("El ID debe ser un número entero. Por favor, intente nuevamente.")
            continue
        id = int(id_input)  # Convertir a entero si es válido
        break

    claseEncontrada = buscarClasePorId(clases, id)
    success, materias = abrirArchivoDeMaterias()
      
    if not success:
        print("No se encontraron materias.")
        return
    if claseEncontrada:
        nombreMateria = "Desconocida"
        for materia in materias:
            if materia['id'] == claseEncontrada["materiaId"]:
                nombreMateria = materia['nombre']
                break
        if claseEncontrada["estado"] == "Activa":
            claseEncontrada["estado"] = "Inactiva"
            print(f"Clase eliminada: \nID materia: {claseEncontrada['id']}, \nNombre materia: {nombreMateria}, \nDía: {dias[claseEncontrada['dia']]}, \nTurno: {turnos[claseEncontrada['turno']]}")
            # Eliminar el ID de clase del array 'clases' en cada alumno que la tenga asignada
            for alumno in alumnos:
                if id in alumno["clases"]:
                    alumno["clases"].remove(id)
                    print(f"El ID de la clase {id} ha sido eliminado de los alumnos inscriptos a la misma.")
        else:
            print("La clase ya está eliminada o no está activa.")
    else:
        print("No se encontró una clase con el ID ingresado.")
    return

def asignarNuevaClase(LU, claseId, alumnos):
  """
  Asigna una nueva clase a un alumno específico en la lista de alumnos.
  Args:
    LU (int): El número de legajo universitario (LU) del alumno al que se le asignará la nueva clase.
    claseId (int): El identificador de la clase que se va a asignar.
    alumnos (list): Una lista de diccionarios, donde cada diccionario representa un alumno y contiene
            al menos las claves "LU" y "clases". La clave "clases" es una lista de identificadores
            de clases a las que el alumno está inscrito.
  Returns:
    list: La lista de alumnos actualizada con la nueva clase asignada al alumno correspondiente.
  """
  alumnos[0]
  for alumno in alumnos:
    if alumno["LU"] == LU:
      alumno["clases"].append(claseId)
  
  alumnos = alumnosModule.reescribirArchivoAlumnos(alumnos[:])

  return alumnos


def desasignarClase(LU, clase, alumnos):
  """
  Desasigna una clase de un alumno específico basado en su LU (Legajo Universitario).
  Args:
    LU (str): El Legajo Universitario del alumno.
    clase (str): El nombre de la clase a desasignar.
    alumnos (list): Lista de diccionarios que representan a los alumnos. 
            Cada diccionario debe contener las claves "LU" y "clases".
  Returns:
    list: La lista de alumnos actualizada después de desasignar la clase.
  """
  
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" in alumno:
        alumno["clases"].remove(clase)
      return alumnos
  # TODO: Relacionar con facturas/pagos de ser necesario
  return alumnos

def listarClasesDisponibles(alumno, clases, materias):
  '''
  Lista clases en las que un alumno se puede inscribir (en el caso de que pueda)
  Args:
    alumno: dict - Diccionario con la información del alumno.
    clases: list - Lista de clases disponibles
  return: list - Lista de clases en las que se puede inscribir el alumno
  '''
  clasesIdDisponibles = []

  if len(alumno["clases"]) < 5:
    print(f"El alumno {alumno['nombre']} {alumno['apellido']} está cursando {len(alumno['clases'])} clases.")
    print("Estas son las clases a las cuales se puede inscribir:\n")

    noEstaCursando = []

    # Primero filtramos las que NO está cursando el alumno
    for clase in clases:
      if clase["id"] not in alumno["clases"]:
        noEstaCursando.append(clase)
    
    for i in range(len(alumno["clases"])):
      for clase in clases:
        if clase["id"] == alumno["clases"][i]:
          alumno["clases"][i] = clase
          for materia in materias:
            if materia["id"] == clase["materiaId"]:
              clase["materia"] = materia["nombre"]
    
    opcionesDeInscripcion = []
    
    for noClase in noEstaCursando:
      for clase in alumno["clases"]:
        if (clase["dia"] != noClase["dia"] or clase["turno"] != noClase["turno"]) and noClase["cuatrimestre"] == 1 and noClase["materiaId"] not in [claseAlumn["materiaId"] for claseAlumn in alumno["clases"]]:
          opcionesDeInscripcion.append(noClase)
          break

    clasesIdDisponibles = [clase["id"] for clase in opcionesDeInscripcion]
    
    # clases disponibles para cursar
    for clase in opcionesDeInscripcion:
      print(f"{clase['id']} - {materias[clase["materiaId"] - 1]["nombre"]} - Día: {dias[clase["dia"]]} - Turno: {turnos[clase["turno"]]}")
  else:
    print(f"El alumno {alumno['nombre']} {alumno['apellido']} está cursando más de 5 materias y no se pueden listar más clases.")

  return clasesIdDisponibles

def listarClasesDeAlumno(alumno, clases):
  
  '''
  Lista clases en las que esta inscrito un alumno
  Args:
    alumno: dict - Diccionario con la información del alumno.
    clases: list - Lista de clases disponibles
  return: list - Lista de clases en las que esta inscrito el alumno
  '''
  success, materias = abrirArchivoDeMaterias()
  
  if not success:
    print("No se encontraron materias.")
    return

  if len(alumno["clases"]) == 0:
    print(f"El alumno {alumno['nombre']} {alumno['apellido']} no está cursando ninguna clase.")
    print("")
  else:
    print(f"El alumno {alumno['nombre']} {alumno['apellido']} está cursando las siguientes clases:")
    print("")

    for claseId in alumno["clases"]:
      for clase in clases:
        if clase["id"] == claseId:
          nombreMateria = "Materia no encontrada"
          for materia in materias:
            if materia["id"] == clase["materiaId"]:
              nombreMateria = materia["nombre"]
              break
          
          dia = dias[clase["dia"]]
          turno = turnos[clase["turno"]]
          cuatrimestre = cuatrimestres[clase["cuatrimestre"]]
          
          print(f"{clase['id']} - {nombreMateria} - Día: {dia} - Turno: {turno} - Año: {clase['anio']} - Cuatrimestre: {cuatrimestre}")
          print("")
  return alumno["clases"]


def desasignarClase(LU, clase, alumnos):
  '''
  Desasigna una clase de un alumno
  Args:
    LU: int - Legajo del alumno
    clase: int - ID de la clase a desasignar
    alumnos: list - Lista de alumnos
  Returns:
    list - Lista de alumnos actualizada
  '''
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" in alumno:
        alumno["clases"].remove(clase)
        print("Clase desasignada con exito")
        print("")
      return alumnos
  return alumnos