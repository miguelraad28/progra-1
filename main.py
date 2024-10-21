"""
-----------------------------------------------------------------------------------------------
Título: TPO
Fecha: 14/10/2024
Autor: Miguel Raad, Roberto Saavedra, Felipe Di Liscia, Daniel Bilikin

Descripción: Proyecto de gestión de alumnos, clases y facturación de una universidad, EDAU.

Pendientes: Listado de clases y su filtrado por turno, día y materia. Módulo de facturas con listado, marcar como pagada y ver morosos
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import alumnos as alumnosModule
import clases_materias as clasesMateriasModule
import json

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def menuGestionAlumnos(alumnos):
  while True:
    opciones = 8
    while True:
      print()
      print("---------------------------")
      print("GESTIÓN DE ALUMNOS        ")
      print("---------------------------")
      print("[1] Listar alumnos")
      print("[2] Nuevo alumno")
      print("[3] Modificar alumno")
      print("[4] Eliminar alumno por legajo")
      print("[5] Buscar alumno por legajo")
      print("[6] Buscar alumno por DNI")
      print("[7] Listar alumnos inactivos")
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

    elif opcion == "1":   # Opción listar alumnos
      alumnosModule.listarAlumnos(alumnos)
      
    elif opcion == "2":   # Opción nuevo alumno
      nombre = input("Ingrese el nombre del alumno: ").capitalize()

      while nombre == "" or len(nombre) < 3:
        print("El nombre no puede estar vacío y debe tener minimo 3 letras.")
        nombre = input("Ingrese el nombre del alumno: ").capitalize()

      apellido = input("Ingrese el apellido del alumno: ").capitalize()

      while apellido == "" or len(apellido) < 3:
        print("El apellido no puede estar vacío y debe tener minimo 3 letras.")
        apellido = input("Ingrese el apellido del alumno: ").capitalize()

      dni = alumnosModule.pedirDniNuevoAlumno()

      alumnos = alumnosModule.nuevoAlumno(nombre, apellido, dni, alumnos)
      alumnoCreado = alumnos[-1]
      
      print("")
      print(f"Nombre: {alumnoCreado["nombre"]}")
      print(f"Apellido: {alumnoCreado["apellido"]}")
      print(f"D.N.I: {alumnoCreado["DNI"]:,}")
      print(f"L.U: {alumnoCreado["LU"]:,}")
      print(f"Email: {alumnoCreado["email"]}")
      print("_________________________")
      print("")
      
    elif opcion == "3":   # Opción modificar alumno
      while True:
        [encontrado, alumno] = alumnosModule.encontrarPorLegajo(alumnos)

        if encontrado:
          print(f"Nombre: {alumno["nombre"]}")
          print(f"Apellido: {alumno["apellido"]}")
          print(f"D.N.I: {alumno["DNI"]:,}")
          print(f"L.U: {alumno["LU"]:,}")
          print(f"Email: {alumno["email"]}")
          print(f"Estado: {alumno["estado"]}")
          print("_________________________")
          break
        else:
          print("No se encontró un alumno con el legajo ingresado.")
      
      while True:
        campo = input("Ingrese el campo a modificar (nombre, apellido): ")
        if campo.lower() in ["nombre", "apellido"]:
          break
      
      while True:
        nuevoValor = input(f"Ingrese el nuevo valor para el campo {campo}: ")
        if nuevoValor != "":
          nuevoValor = nuevoValor.capitalize()
          break
        else:
          print("El valor no puede estar vacío.")
      alumnosModule.modificarAlumnoPorLU(alumno["LU"], campo.lower(), nuevoValor, alumnos)
      
    elif opcion == "4":   # Opción eliminar alumno
      LU = int(input("Ingrese el Legajo a eliminar: "))
      alumnosModule.borrarAlumnoLogico(LU, alumnos)
      
    elif opcion == "5":   # Opción buscar alumno por legajo
        [encontrado, alumno] = alumnosModule.encontrarPorLegajo(alumnos)

        if encontrado:
          print(f"Nombre: {alumno["nombre"]}")
          print(f"Apellido: {alumno["apellido"]}")
          print(f"D.N.I: {alumno["DNI"]:,}")
          print(f"L.U: {alumno["LU"]:,}")
          print(f"Email: {alumno["email"]}")
          print(f"Estado: {alumno["estado"]}")
          print("_________________________")
          break
        else:
          print("No se encontró un alumno con el legajo ingresado.")
      

    elif opcion == "6":   # Opción buscar alumno por DNI
      while True:
        dni = int(input("Ingrese el DNI del alumno: "))
        if dni <= 0:
            print("El DNI debe ser un número positivo.")
            continue
        if len(str(dni)) < 7 or len(str(dni)) > 8:
            print("El DNI debe tener entre 7 y 8 dígitos.")
            continue
        break

      alumnoEncontrado = alumnosModule.encontrarPorDni(dni)

      if alumnoEncontrado:
        print(f"Nombre: {alumnoEncontrado["nombre"]}")
        print(f"Apellido: {alumnoEncontrado["apellido"]}")
        print(f"D.N.I: {alumnoEncontrado["DNI"]:,}")
        print(f"L.U: {alumnoEncontrado["LU"]:,}")
        print(f"Email: {alumnoEncontrado["email"]}")
        print(f"Estado: {alumnoEncontrado["estado"]}")
        print("_________________________")
        print("")
      else:
        print("No se encontró un alumno con el DNI ingresado.")

    elif opcion == "7":   # Opcion mostrar alumnos inactivos
      alumnosModule.listarAlumnosInactivos(alumnos)

    input("\nPresione ENTER para volver al menú de gestión de alumnos.")
    print("\n\n")

def menuGestionClases(clases, alumnos):
  '''
  Menú de gestión de clases
  ARGS: clases - Lista de clases
  '''
  while True:
    opciones = 7
    while True:
      print()
      print("---------------------------")
      print("GESTIÓN DE CLASES        ")
      print("---------------------------")
      print("[1] Crear nueva Clase")
      print("[2] Modificar Clases")
      print("[3] Eliminar Clases")
      print("[4] Asignar Alumno a Clase")
      print("[5] Dar de baja un alumno de una Clase")
      print("[6] Listar Clases de Alumno")
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

    elif opcion == "1":   # Opción nueva clase
      clasesMateriasModule.crearClase(clases)
      
    elif opcion == "2":   # Opción modificar clase
      clasesMateriasModule.modificarClase(clases)
      
    elif opcion == "3":   # Opción eliminar clase
      clasesMateriasModule.eliminarClase(clases)

    elif opcion == "4":   # Opción asignar alumno a clase
      alumnoEncontrado, legajo = alumnosModule.chequeaLegajo(alumnos)
      clasesDisponibles = clasesMateriasModule.listarClasesDisponibles(alumnoEncontrado, clases)
      while True:
        claseElegida = int(input("Ingrese la clase a la que deseas inscribir al alumno: "))
        if claseElegida not in clasesDisponibles:
            print("La clase elegida no es valida")
        else:
          break
      clasesMateriasModule.asignarNuevaClase(legajo, claseElegida, alumnos)

    elif opcion == "5":   # Opción Dar de baja un alumno de una clase
      alumnoEncontrado, legajo = alumnosModule.chequeaLegajo(alumnos)
      clasesAsignadasDeAlumno = clasesMateriasModule.listarClasesDeAlumno(alumnoEncontrado, clases)
      while True:
        claseElegida = int(input("Ingrese la clase a dar de baja: "))
        if claseElegida not in clasesAsignadasDeAlumno:
            print("La clase elegida no es valida")
        else:
          break
      clasesMateriasModule.desasignarClase(legajo, claseElegida, alumnos)

    elif opcion == "6":   # Opción Listar Clases de Alumnos
      alumnoEncontrado, legajo = alumnosModule.chequeaLegajo(alumnos)
      clasesMateriasModule.listarClasesDeAlumno(alumnoEncontrado, clases)

    input("\nPresione ENTER para volver al menú de gestión de alumnos.")
    print("\n\n")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def mostrarMenu(alumnos, clases, facturas):
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
      menuGestionClases(clases, alumnos)
      ...
    elif opcion == "3":   # Opción 3
      # menuGestionFacturas()
      ...

    input("\nPresione ENTER para volver al menú.")
    print("\n\n")

def main():
  #-------------------------------------------------
  # Inicialización de variables
  #----------------------------------------------------------------------------------------------
  with open("./data/data_alumnos.json", "r", encoding='utf-8') as file:
    alumnos = json.load(file)
    file.close()

  with open("./data/data_clases.json", "r", encoding='utf-8') as file:
    clases = json.load(file)
    file.close()

  facturas = []
  #-------------------------------------------------
  # Bloque de menú
  #----------------------------------------------------------------------------------------------
  mostrarMenu(alumnos, clases, facturas)

if __name__ == "__main__":
  main()
