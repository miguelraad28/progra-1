import random
import alumnos as alumnosModule
import clases_materias as clasesMateriasModule


def generarDatosIniciales():
  """
  Genera los datos iniciales para el sistema.
  Esta función llama a dos módulos para generar una lista de alumnos y una lista de clases.
  Utiliza las funciones `generarAlumnos` del módulo `alumnosModule` y `generarClases` del 
  módulo `clasesMateriasModule` con un parámetro de 100 clases.
  Returns:
    list: Una lista que contiene dos elementos:
    - alumnos: Lista de alumnos generada por `alumnosModule.generarAlumnos()`.
    - clases: Lista de clases generada por `clasesMateriasModule.generarClases()`.
  """
  alumnos = alumnosModule.generarAlumnos(500)
  clases = clasesMateriasModule.generarClases(clasesMateriasModule.materias, 20)
  print("* *  * **alumnos")
  print(alumnos)
  print("* * ** * *clases")
  # print(clases)

  return [alumnos, clases]

def menuGestionAlumnos(alumnos):
  while True:
    opciones = 5
    while True:
      print()
      print("---------------------------")
      print("GESTIÓN DE ALUMNOS        ")
      print("---------------------------")
      print("[1] Nuevo alumno")
      print("[2] Modificar alumno")
      print("[3] Eliminar alumno")
      print("[4] Buscar alumno por legajo")
      print("---------------------------")
      print("[0] Volver al menú principal")
      print()
      
      opcion = input("Seleccione una opción: ")
      if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
        break
      else:
        input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    if opcion == "0": # Opción volver al menú principal
      break

    elif opcion == "1":   # Opción nuevo alumno
      nombre = input("Ingrese el nombre del alumno: ")
      apellido = input("Ingrese el apellido del alumno: ")
      alumnosModule.nuevoAlumno(nombre, apellido, alumnos)
      print(alumnos[-1])
      ...
    elif opcion == "2":   # Opción modificar alumno
      # menuGestionClasesMaterias()
      ...
    elif opcion == "3":   # Opción eliminar alumno
      # menuGestionFacturas()
      ...
    elif opcion == "4":   # Opción buscar alumno por legajo
      alumnosModule.encontrarPorLegajo()

    input("\nPresione ENTER para volver al menú de gestión de alumnos.")
    print("\n\n")

def mostrarMenu(alumnos):
  while True:
    opciones = 4
    while True:
      print()
      print("---------------------------")
      print("MENÚ DEL SISTEMA           ")
      print("---------------------------")
      print("[1] Gestión de alumnos")
      print("[2] Gestión de clases y materias")
      print("[3] Gestión de facturas y pagos")
      print("---------------------------")
      print("[0] Salir del programa")
      print()
      
      opcion = input("Seleccione una opción: ")
      if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
        break
      else:
        input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    if opcion == "0": # Opción salir del programa
      exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    elif opcion == "1":   # Opción 1
      menuGestionAlumnos(alumnos)
      ...
    elif opcion == "2":   # Opción 2
      # menuGestionClasesMaterias()
      ...
    elif opcion == "3":   # Opción 3
      # menuGestionFacturas()
      ...

    input("\nPresione ENTER para volver al menú.")
    print("\n\n")

def main():
  [alumnos, clases] = generarDatosIniciales()
  alumnosModule.nuevoAlumno("Juan", "Pérez", alumnos)
  mostrarMenu(alumnos)

if __name__ == "__main__":
  main()
