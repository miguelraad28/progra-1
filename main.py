import alumnos as alumnosModule
import clases_materias as clasesMateriasModule

def menuGestionAlumnos(alumnos):
  while True:
    opciones = 5
    while True:
      print()
      print("---------------------------")
      print("GESTIÓN DE ALUMNOS        ")
      print("---------------------------")
      print("[1] Listar alumnos")
      print("[2] Nuevo alumno")
      print("[3] Modificar alumno")
      print("[4] Eliminar alumno")
      print("[5] Buscar alumno por legajo")
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
      alumnosModule.listarAlumnos(alumnos)
      ...
    elif opcion == "2":   # Opción nuevo alumno
      nombre = input("Ingrese el nombre del alumno: ")
      apellido = input("Ingrese el apellido del alumno: ")
      dni = int(input("Ingrese el DNI del alumno: "))

      alumnos = alumnosModule.nuevoAlumno(nombre, apellido, dni, alumnos[:])
      alumnoCreado = alumnos[-1]
      
      print("")
      print(f"Nombre: {alumnoCreado["nombre"]}")
      print(f"Apellido: {alumnoCreado["apellido"]}")
      print(f"D.N.I: {alumnoCreado["DNI"]:,}")
      print(f"L.U: {alumnoCreado["LU"]:,}")
      print("_________________________")
      print("")
      ...
    elif opcion == "3":   # Opción modificar alumno
      while True:
        legajo = int(input("Ingrese el legajo del alumno a modificar: "))
        [encontrado, alumno] = alumnosModule.encontrarPorLegajo(legajo, alumnos)
        if encontrado:
          break
      
      while True:
        campo = input("Ingrese el campo a modificar (nombre, apellido): ")
        if campo in ["nombre", "apellido"]:
          break
        
      alumnosModule.modificarAlumnoPorLU(legajo, campo, alumnos)
      
      # menuGestionClasesMaterias()
      ...
    elif opcion == "4":   # Opción eliminar alumno
      # menuGestionFacturas()
      ...
    elif opcion == "5":   # Opción buscar alumno por legajo
      alumnosModule.encontrarPorLegajo()

    input("\nPresione ENTER para volver al menú de gestión de alumnos.")
    print("\n\n")

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
      # menuGestionClasesMaterias()
      ...
    elif opcion == "3":   # Opción 3
      # menuGestionFacturas()
      ...

    input("\nPresione ENTER para volver al menú.")
    print("\n\n")

def main():
  alumnos = alumnosModule.generarAlumnos(125)
  clases = clasesMateriasModule.generarClases(clasesMateriasModule.materias, 20)
  facturas = []
  
  mostrarMenu(alumnos, clases, facturas)

if __name__ == "__main__":
  main()
