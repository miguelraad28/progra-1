"""
-----------------------------------------------------------------------------------------------
Título: TPO
Fecha: 25/11/2024
Autor: Miguel Raad, Roberto Saavedra, Felipe Di Liscia, Daniel Bilikin

Descripción: Proyecto de gestión de alumnos, clases y facturación de una universidad, EDAU.

Pendientes: Relacionar las modificaciones de clases de los alumnos con la entidad de facturas. CUando al alumno se le asigna, desasigna una materia o se Inactiva el alumno, es necesario awctualizar la entidad de facturas
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import alumnos as alumnosModule
import clases_materias as clasesMateriasModule
import facturas as facturasModule
from variables import dias, turnos, costo_por_clase

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def menuGestionAlumnos():
  success, alumnos = alumnosModule.abrirArchivoAlumnos()

  success2, clases = clasesMateriasModule.abrirArchivoClases()

  success3, materias = clasesMateriasModule.abrirArchivoDeMaterias()

  if not success:
    return

  if not success2:
    return

  if not success3:
    return

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
        print("El nombre no puede estar vacío y debe tener mínimo 3 letras.")
        nombre = input("Ingrese el nombre del alumno: ").capitalize()

      apellido = input("Ingrese el apellido del alumno: ").capitalize()
      while apellido == "" or len(apellido) < 3:
        print("El apellido no puede estar vacío y debe tener mínimo 3 letras.")
        apellido = input("Ingrese el apellido del alumno: ").capitalize()

      success, dni = alumnosModule.pedirDniNuevoAlumno(alumnos)
      
      if not success:
        return

      alumnosActualizado = alumnosModule.nuevoAlumno(nombre, apellido, dni, alumnos)
      alumnoCreado = alumnosActualizado[-1]
      
      success = alumnosModule.reescribirArchivoAlumnos(alumnosActualizado)
      
      if success:
        print("")
        print(f"Nombre: {alumnoCreado["nombre"]}")
        print(f"Apellido: {alumnoCreado["apellido"]}")
        print(f"D.N.I: {alumnoCreado["DNI"]:,}")
        print(f"L.U: {alumnoCreado["LU"]:,}")
        print(f"Email: {alumnoCreado["email"]}")
        print("_________________________")
        print("")
      else:
        print('Error cargando el nuevo alumno')
      
    elif opcion == "3":   # Opción modificar alumno
      while True:
        alumno = alumnosModule.encontrarPorLegajo(alumnos)

        if alumno:
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
        else:
          print("\nEl campo ingresado no es válido. Intente nuevamente.\n")
      
      while True:
        nuevoValor = input(f"Ingrese el nuevo valor para el campo {campo}: ")
        if nuevoValor != "":
          nuevoValor = nuevoValor.capitalize()
          break
        else:
          print("El valor no puede estar vacío.")

      alumnosModule.modificarAlumnoPorLU(alumno["LU"], campo.lower(), nuevoValor, alumnos)
      
      print(f"El campo '{campo}' ha sido modificado correctamente.")
    elif opcion == "4":  # Opción eliminar alumno
      alumno = alumnosModule.encontrarPorLegajo(alumnos)
      
      if alumno:
        alumnosModule.borrarAlumnoLogico(alumno["LU"], alumnos)
      else:
        print("No se encontró un alumno con el legajo ingresado.")
      return

    elif opcion == "5":   # Opción buscar alumno por legajo
      alumno = alumnosModule.encontrarPorLegajo(alumnos)

      if alumno:
        # Le asignamos al array de id de clases, la clase con el nombre de la materia
        for i in range(len(alumno["clases"])):
          for clase in clases:
            if clase["id"] == alumno["clases"][i]:
              alumno["clases"][i] = clase
              for materia in materias:
                if materia["id"] == clase["materiaId"]:
                  clase["materia"] = materia["nombre"]
        #############################################
        print("_________________________")
        print(f"Nombre: {alumno["nombre"]}")
        print(f"Apellido: {alumno["apellido"]}")
        print(f"D.N.I: {alumno["DNI"]:,}")
        print(f"L.U: {alumno["LU"]:,}")
        print(f"Email: {alumno["email"]}")
        print(f"Estado: {alumno["estado"]}")
        print("\nClases:")
        for clase in alumno["clases"]:
          print(f"   {clase["materia"]} - {dias[clase["dia"]]} {turnos[clase["turno"]]}")
        print("_________________________")
      else:
        print("No se encontró un alumno con el legajo ingresado.")
      return
    elif opcion == "6":   # Opción buscar alumno por DNI
      try:
        while True:
          dni = int((input("Ingrese el DNI del alumno o '0' para volver al menu: ")))
          if dni == 0:
            return
          elif dni < 0:
              print("El DNI debe ser un número positivo.")
              continue
          elif len(str(dni)) < 7 or len(str(dni)) > 8:
              print("El DNI debe tener entre 7 y 8 dígitos.")
              continue
          break
      except Exception as ex:
        print("Ocurrió un error al recibir el DNI, ", ex)
        return

      alumno = alumnosModule.encontrarPorDni(alumnos, dni)


      if alumno:
        # Le asignamos al array de id de clases, la clase con el nombre de la materia
        for i in range(len(alumno["clases"])):
          for clase in clases:
            if clase["id"] == alumno["clases"][i]:
              alumno["clases"][i] = clase
              for materia in materias:
                if materia["id"] == clase["materiaId"]:
                  clase["materia"] = materia["nombre"]
        #############################################
        print("_________________________")
        print(f"Nombre: {alumno["nombre"]}")
        print(f"Apellido: {alumno["apellido"]}")
        print(f"D.N.I: {alumno["DNI"]:,}")
        print(f"L.U: {alumno["LU"]:,}")
        print(f"Email: {alumno["email"]}")
        print(f"Estado: {alumno["estado"]}")
        print("\nClases:")
        for clase in alumno["clases"]:
          print(f"   {clase["materia"]} - {dias[clase["dia"]]} {turnos[clase["turno"]]}")
        print("_________________________")
        print("")
      else:
        print("No se encontró un alumno con el DNI ingresado.")

    elif opcion == "7":   # Opcion mostrar alumnos inactivos
      alumnosModule.listarAlumnosInactivos(alumnos)

    input("\nPresione ENTER para volver al menú de gestión de alumnos.")
    print("\n\n")


def menuGestionClases():
  '''
  Menú de gestión de clases
  '''
  
  success, alumnos = alumnosModule.abrirArchivoAlumnos()

  success2, clases = clasesMateriasModule.abrirArchivoClases()
  
  success3, materias = clasesMateriasModule.abrirArchivoDeMaterias()
  
  if not success:
    return
  
  if not success2:
    return
  
  if not success3:
    return

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
      clasesMateriasModule.crearClase(clases[:])
      
    elif opcion == "2":   # Opción modificar clase
      clasesMateriasModule.modificarClase(clases[:])
      
    elif opcion == "3":   # Opción eliminar clase
      clasesMateriasModule.eliminarClase(clases[:], alumnos[:])

    elif opcion == "4":   # Opción asignar alumno a clase
      alumnoEncontrado, legajo = alumnosModule.chequeaLegajo(alumnos[:])

      alumnoEncontradoCopia = {
        "clases": alumnoEncontrado["clases"][:],
        "nombre": alumnoEncontrado["nombre"],
        "apellido": alumnoEncontrado["apellido"],
      }
      
      clasesDisponibles = clasesMateriasModule.listarClasesDisponibles(alumnoEncontradoCopia, clases[:], materias[:])

      while True:
        claseInput = input("Ingrese la clase a la que deseas inscribir al alumno: ").strip()
        if not claseInput:  # Validar si está vacío
            print("El campo no puede estar vacío. Por favor, ingrese un valor válido.")
            continue
        if not claseInput.isdigit():  # Validar si no es un número
            print("La clase debe ser un número entero. Por favor, intente nuevamente.")
            continue
        claseElegida = int(claseInput)
        if claseElegida not in clasesDisponibles:  # Validar si la clase está disponible
            print("La clase elegida no es válida. Por favor, elija una clase de la lista disponible.")
        else:
          clasesMateriasModule.asignarNuevaClase(legajo, claseElegida, alumnos[:])
          break  # Salir del bucle si el valor es válido


    elif opcion == "5":   # Opción Dar de baja un alumno de una clase
      alumnoEncontrado, legajo = alumnosModule.chequeaLegajo(alumnos[:])
      clasesAsignadasDeAlumno = clasesMateriasModule.listarClasesDeAlumno(alumnoEncontrado, clases[:])
      while True:
        claseElegida = int(input("Ingrese la clase a dar de baja: "))
        if claseElegida not in clasesAsignadasDeAlumno:
            print("La clase elegida no es valida")
        else:
          break
      clasesMateriasModule.desasignarClase(legajo, claseElegida, alumnos[:])

    elif opcion == "6":   # Opción Listar Clases de Alumnos
      alumnoEncontrado, legajo = alumnosModule.chequeaLegajo(alumnos[:])
      clasesMateriasModule.listarClasesDeAlumno(alumnoEncontrado, clases[:])

    input("\nPresione ENTER para volver al menú de gestión de clases y materias.")
    print("\n\n")

def menuGestionFacturas():
  '''
  Menú de gestión de facturas
  '''
  
  success, alumnos = alumnosModule.abrirArchivoAlumnos()

  success2, clases = clasesMateriasModule.abrirArchivoClases()

  success3, facturas = facturasModule.abrirArchivoFacturas()
  
  if not success:
    return
  
  if not success2:
    return
  
  if not success3:
    return

  while True:
    opciones = 4
    while True:
      print()
      print("---------------------------")
      print("GESTIÓN DE FACTURAS Y PAGOS   ")
      print("---------------------------")
      print("[1] Ver morosos")
      print("[2] Ver última factura por LU")
      print("[3] Marcar factura como pagada")
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

    elif opcion == "1":   # Ver morosos
      morosos = facturasModule.obtenerMorosos(facturas[:], alumnos[:], clases[:])
      # print("*morosos")
      # print(morosos)
      for moroso in morosos:
        print(f"\n{moroso["alumno"]["apellido"]}, {moroso["alumno"]["nombre"]} - LU: {moroso["alumno"]["LU"]:,}")
        print(f"Deuda: ${moroso['factura']['monto']:,}")
        print("\nDetalle:")
        for clase in moroso["factura"]["clases"]:
          print(f"   {clase["materia"]} - {dias[clase["dia"]]} {turnos[clase["turno"]]}")
        print("____________________________________")
      ...
      
      moraTotal = len([clase for moroso in morosos for clase in moroso["factura"]["clases"]]) * costo_por_clase
      print(f"\nMora total: ${moraTotal:,}")
    elif opcion == "2":   # Ver última factura por LU
      alumno = alumnosModule.encontrarPorLegajo(alumnos[:])

      if alumno:
        factura = facturasModule.verUltimaFacturaPorLU(facturas, alumno["LU"], clases)
        
        if factura:
          print("---------------------------")
          print(f"{alumno["apellido"]}, {alumno["nombre"]}, LU: {alumno["LU"]:,}")
          print(f"Monto: ${factura['monto']:,}")
          print("Pagada: ", "Sí" if factura["pagada"] else "No")
          print("Detalle:")
          for clase in factura["clases"]:
            print(f"   {clase["materia"]} - {dias[clase["dia"]]} {turnos[clase["turno"]]}")
          print("---------------------------")
          
          if not factura["pagada"]:
            opcion = input("Desea marcarla como pagada? (s/n): ")
            if opcion.lower() == "s":
              factura = facturasModule.marcarComoPagada(alumno["LU"])
              print("Factura marcada como pagada.")
            else:
              return
        else: 
          print("No se encontraron facturas para el alumno.")
        return
      else:
        print("No se encontró un alumno con el legajo ingresado.")
      return
      ...
    elif opcion == "3":   # Marcar factura como pagada
      print("\nMarcar como paga la factura un alumno por Legajo Único")
      alumno = alumnosModule.encontrarPorLegajo(alumnos[:])

      if alumno:
        factura = facturasModule.marcarComoPagada(alumno["LU"])
        print("Factura marcada como pagada.")
      else:
        print("No se encontró un alumno con el legajo ingresado.")
      return
      ...
    input("\nPresione ENTER para volver al menú de gestión de facturas y pagos.")
    print("\n\n")

  
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def mostrarMenu():

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
      menuGestionAlumnos()
      ...
    elif opcion == "2":   # Opción 2
      menuGestionClases()
      ...
    elif opcion == "3":   # Opción 3
      menuGestionFacturas()
      ...

    input("\nPresione ENTER para volver al menú.")
    print("\n\n")

def main():
  #-------------------------------------------------
  # Inicialización de variables
  #----------------------------------------------------------------------------------------------
  #-------------------------------------------------
  # Bloque de menú
  #----------------------------------------------------------------------------------------------
  mostrarMenu()

main()