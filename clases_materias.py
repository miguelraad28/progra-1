import random
import re

# Materias & Clases

materias = [
  {"id": 1, "nombre": "Matemática Discreta"},
  {"id": 2, "nombre": "Álgebra y Geometría Analítica"},
  {"id": 3, "nombre": "Análisis Matemático I"},
  {"id": 4, "nombre": "Algoritmos y Estructuras de Datos"},
  {"id": 5, "nombre": "Arquitectura de Computadoras"},
  {"id": 6, "nombre": "Introducción a la Programación"},
  {"id": 7, "nombre": "Sistemas y Organizaciones"},
  {"id": 8, "nombre": "Física I"},
  {"id": 9, "nombre": "Química"},
  {"id": 10, "nombre": "Inglés Técnico I"},
]

dias = {
  0: "Lunes",
  1: "Martes",
  2: "Miércoles",
  3: "Jueves",
  4: "Viernes" 
}
   
turno = {
  0:"Mañana",
  1:"Tarde",
  2:"Noche"
}

cuatrimestre = {
  0:"1er Cuatrimestre",
  1:"2ndo Cuatrimestre",
}


def generarClases(cantidad):
  '''
  Genera una lista de clases basado en las materias que tenemos al inicio del modulo de manera aleatoria para inicializar el programa con datos en memoria.
  '''
  clases = []
  for i in range(cantidad):
    clase = {
      "id": 1000 + i,
      "dia": random.choice(list(dias.keys())),
      "turno": random.choice(list(turno.keys())),
      "anio": "2024",
      "cuatrimestre": random.choice(list(cuatrimestre.keys())),
      "materiaId": random.choice(materias)["id"],
      "estado":"Activa"
    }
    clases.append(clase)
  return clases

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

  while True:
      diaInput = int(input("Ingrese el dia de dictado de la clase (0: Lunes, 1: Martes, 2: Miercoles, 3: Jueves, 4: Viernes): "))
      if 0 <= diaInput <= 4:
          break
      else:
          print("Opcion invalida, por favor ingrese una opcion correcta (0: Lunes, 1: Martes, 2: Miercoles, 3: Jueves, 4: Viernes)")
  
  while True:
      turnoInput = int(input("Ingrese el turno de la clase (0: Mañana, 1: Tarde, 2: Noche): "))
      if 0 <= turnoInput <= 2:
          break
      else:
          print("Opcion invalida, por favor ingrese una opcion correcta (0: Mañana, 1: Tarde, 2: Noche)")
  
  while True:
      print("")
      print("Listado materias: ")
      print("_____________________")
      for materia in materias:
          print(f"{materia['id']}: {materia['nombre']}")
      id = int(input("Ingrese el ID de la materia de la clase a crear: "))
      if 1 <= id <= 10: # Acá forzamos un poco la validación del id de la materia basada en las que tenemos preescritas en el código.
          break
      else:
          print("ID invalido, por favor ingrese un ID correcto (entre 1 y 10)")

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
  print(f"Clase creada satisfactoriamente: \nID materia: {nuevoId}, \nNombre materia: {materia_nombre}, \nDía: {dias[claseNueva['dia']]}, \nTurno: {turno[claseNueva['turno']]}")
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
  id = int(input("Ingrese el ID de la clase que desea modificar: "))
  claseEncontrada = buscarClasePorId(clases, id)

  if claseEncontrada:
    nombreMateria = "Desconocida"
    for materia in materias:
      if materia['id'] == claseEncontrada["materiaId"]:
        nombreMateria = materia['nombre']
        break
    print(f"Clase encontrada: \nID materia: {claseEncontrada['id']}, \nNombre materia: {nombreMateria}, \nDía: {dias[claseEncontrada['dia']]}, \nTurno: {turno[claseEncontrada['turno']]}, \nCuatrimestre: {cuatrimestre[claseEncontrada['cuatrimestre']]}") 

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
      if nuevoTurno == "":  # Si se presiona Enter, no se cambia el día
        break
      if numeroValido(nuevoTurno,2):
        claseEncontrada["turno"] = int(nuevoTurno)
        break
      else:
        print("Opción inválida. Ingrese un turno válido (0: Mañana, 1: Tarde, 2: Noche).")
    print(f"Clase actualizada: \nID materia: {claseEncontrada['id']}, \nNombre materia: {nombreMateria}, \nDía: {dias[claseEncontrada['dia']]}, \nTurno: {turno[claseEncontrada['turno']]}, \nCuatrimestre: {cuatrimestre[claseEncontrada['cuatrimestre']]}")
  else:
    print("No se encontró una clase con el ID ingresado.")

def eliminarClase(clases, alumnos):
  # RELACIONAR CON FACTURAS
  id = int(input("Ingrese el ID de la clase que desea eliminar: "))
  claseEncontrada = buscarClasePorId(clases, id)
  if claseEncontrada:
    nombreMateria = "Desconocida"
    for materia in materias:
      if materia['id'] == claseEncontrada["materiaId"]:
        nombreMateria = materia['nombre']
        break
  if  claseEncontrada["estado"] == "Activa":
      claseEncontrada["estado"] = "Inactiva"
      print(f"Clase eliminada: \nID materia: {claseEncontrada['id']}, \nNombre materia: {nombreMateria}, \nDía: {dias[claseEncontrada['dia']]}, \nTurno: {turno[claseEncontrada['turno']]}")
      # Eliminar el ID de clase del array 'clases' en cada alumno que la tenga asignada
      for alumno in alumnos:
        if id in alumno["clases"]:
          alumno["clases"].remove(id)
          print(f"El ID de la clase {id} ha sido eliminado de los alumnos inscriptos a la misma.")
  else:
      print("La clase ya está eliminada o no hay una clase con ese ID.")
  return

def asignarNuevaClase(LU, claseId, alumnos):
  for alumno in alumnos:
    if alumno["LU"] == LU:
      alumno["clases"].append(claseId)
  return alumnos


def desasignarClase(LU, clase, alumnos):
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" in alumno:
        alumno["clases"].remove(clase)
      return alumnos
  return alumnos

def listarClasesDisponibles(alumno, clases):
  '''
  Lista clases en las que un alumno se puede inscribir (en el caso de que pueda)
  '''
  dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
  turnos = ["Mañana", "Tarde", "Noche"]
  cuatrimestres = ["Primero", "Segundo"]

  if len(alumno["clases"]) <= 5:
    print(f"El alumno {alumno['nombre']} {alumno['apellido']} está cursando {len(alumno['clases'])} clases.")
    print("Estas son las clases a las cuales se puede inscribir:")
    print("")

    materiasCursadas = []
    diasCursados = []

    for claseId in alumno["clases"]:
      for clase in clases:
        if clase["id"] == claseId:
          materiasCursadas.append(clase["materiaId"])
          diasCursados.append(clase["dia"])
    
    # clases disponibles para cursar
    clasesDisponibles = []
    for clase in clases:
      if clase["id"] not in alumno["clases"]:
        if clase["materiaId"] not in materiasCursadas and clase["dia"] not in diasCursados:
          clasesDisponibles.append(clase["id"])
          for materia in materias:
            if materia["id"] == clase["materiaId"]:
              nombreMateria = materia["nombre"]
              break
          
          dia = dias[clase["dia"]]
          turno = turnos[clase["turno"]]
          cuatrimestre = cuatrimestres[clase["cuatrimestre"]]
          
          print(f"{clase['id']} - {nombreMateria} - Día: {dia} - Turno: {turno} - Año: {clase['anio']} - Cuatrimestre: {cuatrimestre}")
          print("")
  else:
    print(f"El alumno {alumno['nombre']} {alumno['apellido']} está cursando más de 5 materias y no se pueden listar más clases.")
    print("")

  return clasesDisponibles

def listarClasesDeAlumno(alumno, clases):
  '''
  Lista clases en las que esta inscrito un alumno
  '''
  dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
  turnos = ["Mañana", "Tarde", "Noche"]
  cuatrimestres = ["Primero", "Segundo"]

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


def asignarNuevaClase(LU, claseId, alumnos):
  '''
  Asigna una nueva clase a un alumno
  '''
  for alumno in alumnos:
    if alumno["LU"] == LU:
      alumno["clases"].append(claseId)
      print("Clase asignada con exito")
      print("")
  return alumnos


def desasignarClase(LU, clase, alumnos):
  '''
  Desasigna una clase de un alumno
  '''
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" in alumno:
        alumno["clases"].remove(clase)
        print("Clase desasignada con exito")
        print("")
      return alumnos
  return alumnos

if __name__ == "__main__":
  clases = generarClases(5)
  print(clases)
  print(asignarNuevaClase(800000, clases[0], [{"LU": 800000}]))
  print(desasignarClase(800000, clases[0], [{"LU": 800000, "clases": [clases[0]]}]))