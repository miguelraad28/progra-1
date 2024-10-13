import random

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

def generarClases(materias, cantidad):
  '''
  Genera una lista de clases basado en las materias que tenemos al inicio del modulo de manera aleatoria para inicializar el programa con datos en memoria.
  '''
  clases = []
  for i in range(cantidad):
    clase = {
      "id": 1000 + i,
      "dia": random.randint(0, 4),
      "turno": random.randint(0, 2),
      "anio": "2024",
      "cuatrimestre": random.randint(0, 1),
      "materiaId": random.choice(materias)["id"],
    }
    clases.append(clase)
  return clases

def crearClase(clases, materias):
  '''
  Crea una nueva clase y la agrega a la lista de clases.
  ARGS:
    clases: List[Dict] - Lista de clases a la que se le agregará la nueva clase.
    materias: List[Dict] - Lista de materias disponibles para seleccionar la materia de la clase.
  '''
  if len(clases) > 0:
      nuevoId = clases[-1]["id"] + 1 
  else:
      nuevoId = 1000 

  while True:
      dia = int(input("Ingrese el dia de dictado de la clase (0: Lunes, 1: Martes, 2: Miercoles, 3: Jueves, 4: Viernes): "))
      if 0 <= dia <= 4:
          break
      else:
          print("Opcion invalida, por favor ingrese una opcion correcta (0: Lunes, 1: Martes, 2: Miercoles, 3: Jueves, 4: Viernes)")
  
  while True:
      turno = int(input("Ingrese el turno de la clase (0: Mañana, 1: Tarde, 2: Noche): "))
      if 0 <= turno <= 2:
          break
      else:
          print("Opcion invalida, por favor ingrese una opcion correcta (0: Mañana, 1: Tarde, 2: Noche)")
  
  while True:
      print("")
      print("Listado materias: ")
      for materia in materias:
          print(f"{materia['id']}: {materia['nombre']}")
      id = int(input("Ingrese el ID de la materia de la clase a crear: "))
      if 1 <= id <= 10: # Acá forzamos un poco la validación del id de la materia basada en las que tenemos preescritas en el código.
          break
      else:
          print("ID invalido, por favor ingrese un ID correcto (entre 1 y 10)")

  claseNueva = {
    "id": nuevoId,
    "dia": dia, 
    "turno": turno,
    "anio": "2024",
    "cuatrimestre": 1,
    "materia_id": id,
  }
  
  clases.append(claseNueva)
  print("Clase creada con éxito:", claseNueva)

def buscarClasePorId(clases, id):
    for clase in clases:
        if clase["id"] == id:
            return clase
    return None

def modificarClase(clases):
    id = int(input("Ingrese el ID de la clase que desea modificar: "))
    claseEncontrada = buscarClasePorId(clases, id)
    if claseEncontrada:
      print(f"Clase encontrada: {claseEncontrada}") 
      while True:
          nuevoDia = int(input("Ingrese el nuevo día de la clase (0: Lunes, 1: Martes, 2: Miércoles, 3: Jueves, 4: Viernes): "))
          if 0 <= nuevoDia <= 4:
              claseEncontrada["dia"] = nuevoDia
              break
          else:
              print("Opción inválida. Ingrese un día válido (0: Lunes, 1: Martes, 2: Miércoles, 3: Jueves, 4: Viernes).")
      while True:
          nuevoTurno = int(input("Ingrese el nuevo turno de la clase (0: Mañana, 1: Tarde, 2: Noche): "))
          if 0 <= nuevoTurno <= 2:
              claseEncontrada["turno"] = nuevoTurno
              break
          else:
              print("Opción inválida. Ingrese un turno válido (0: Mañana, 1: Tarde, 2: Noche).")
      print(f"Clase actualizada: {claseEncontrada}")
    else:
      print("No se encontró una clase con el ID ingresado.")

def eliminarClase(clases):
    id = int(input("Ingrese el ID de la clase que desea eliminar: "))
    for clase in clases:
        if clase["id"] == id:
            if clase["Estado"] == "Activa":
                clase["Estado"] = "Inactiva"
                print(f"Clase eliminada: {clase}")
            else:
                print("La clase ya está eliminada.")
                print(f"{clase}")
            return
    print("No se encontró una clase con el ID ingresado.")
  
def asignarNuevaClase(LU, clase, alumnos):
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" not in alumno:
        alumno["clases"] = []
      alumno["clases"].append(clase)
      return alumnos
  return alumnos


def desasignarClase(LU, clase, alumnos):
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" in alumno:
        alumno["clases"].remove(clase)
      return alumnos
  return alumnos

if __name__ == "__main__":
  clases = generarClases(materias, 5)
  print(clases)
  print(asignarNuevaClase(800000, clases[0], [{"LU": 800000}]))
  print(desasignarClase(800000, clases[0], [{"LU": 800000, "clases": [clases[0]]}]))