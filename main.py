"""
-----------------------------------------------------------------------------------------------
Título: TPO
Fecha: 25/11/2024
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
import facturas as facturasModule

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
turnos = ["Mañana", "Tarde", "Noche"]
cuatrimestres = ["Primero", "Segundo"]

def menuGestionAlumnos():
  success, alumnos = alumnosModule.abrirArchivoAlumnos()

  if not success:
    return print("Error obteniendo datos de alumnos")

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
      print(alumnos[0])
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

      success, dni = alumnosModule.pedirDniNuevoAlumno()
      
      if not success:
        return

      alumnos = alumnosModule.nuevoAlumno(nombre, apellido, dni, alumnos)
      alumnoCreado = alumnos[-1]
      
      success = alumnosModule.reescribirArchivoAlumnos(alumnos)
      
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
        encontrado, alumno = alumnosModule.encontrarPorLegajo(alumnos)

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
      
    elif opcion == "4":  # Opción eliminar alumno
      while True:
        legajoUnicoStr = input("Ingrese el Legajo a eliminar (o '0' para volver al menú): ").strip()
        
        if legajoUnicoStr == "0":  # Permitir regresar al menú ingresando "0"
            return
        
        if legajoUnicoStr.isdigit():  # Validar que sea un número
            legajoUnico = int(legajoUnicoStr)
            break  # Salir del bucle si es válido
        
        print("El legajo debe ser un número entero. Intente nuevamente.")
      
      alumnosModule.borrarAlumnoLogico(legajoUnico, alumnos)

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


def menuGestionClases():
  '''
  Menú de gestión de clases
  '''
  
  success, alumnos = alumnosModule.abrirArchivoAlumnos()

  success2, clases = clasesMateriasModule.abrirArchivoClases()
  
  if not success:
    print('Ha ocurrido un error cargando los datos de los alumnos. Por favor intente nuevamente.')
    return
  
  if not success2:
    print('Ha ocurrido un error cargando los datos de las clases. Por favor intente nuevamente.')
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
      clasesMateriasModule.crearClase(clases)
      
    elif opcion == "2":   # Opción modificar clase
      clasesMateriasModule.modificarClase(clases)
      
    elif opcion == "3":   # Opción eliminar clase
      clasesMateriasModule.eliminarClase(clases, alumnos)

    elif opcion == "4":   # Opción asignar alumno a clase
      alumnoEncontrado, legajo = alumnosModule.chequeaLegajo(alumnos)
      print(alumnoEncontrado)
      
      # clasesDisponibles = clasesMateriasModule.listarClasesDisponibles(alumnoEncontrado, clases)

      # while True:
      #   claseInput = input("Ingrese la clase a la que deseas inscribir al alumno: ").strip()
      #   if not claseInput:  # Validar si está vacío
      #       print("El campo no puede estar vacío. Por favor, ingrese un valor válido.")
      #       continue
      #   if not claseInput.isdigit():  # Validar si no es un número
      #       print("La clase debe ser un número entero. Por favor, intente nuevamente.")
      #       continue
      #   claseElegida = int(claseInput)
      #   if claseElegida not in clasesDisponibles:  # Validar si la clase está disponible
      #       print("La clase elegida no es válida. Por favor, elija una clase de la lista disponible.")
      #   else:
      #       break  # Salir del bucle si el valor es válido

      # clasesMateriasModule.asignarNuevaClase(legajo, claseElegida, alumnos)

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
    print('Ha ocurrido un error cargando los datos de los alumnos. Por favor intente nuevamente.')
    return
  
  if not success2:
    print('Ha ocurrido un error cargando los datos de las clases. Por favor intente nuevamente.')
    return
  
  if not success3:
    print('Ha ocurrido un error cargando los datos de las facturas. Por favor intente nuevamente.')
    return

  while True:
    opciones = 3
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
      morosos = facturasModule.obtenerMorosos(facturas, alumnos, clases)

      for moroso in morosos:
        print("---------------------------")
        print(f"{moroso["alumno"]["apellido"]}, {moroso["alumno"]["nombre"]}, LU: {moroso["alumno"]["LU"]:,}")
        print(f"Deuda: ${moroso['factura']['monto']:,}")
        print("Detalle:")
        for clase in moroso["factura"]["clases"]:
          print(f"   {clase["materia"]} - {dias[clase["dia"]]} {turnos[clase["turno"]]}")
      ...
    elif opcion == "2":   # Ver última factura por LU
      print("opcion 2")
      success, alumnoEncontrado = alumnosModule.encontrarPorLegajo(alumnos)
      if not success:
        print("No se encontró el alumno.")
        return
      
      factura = facturasModule.verUltimaFacturaPorLU(facturas, alumnoEncontrado["LU"], clases)
      if not factura:
        print("No se encontró factura para el alumno.")
        return
      else:
        print("---------------------------")
        print(f"{alumnoEncontrado["apellido"]}, {alumnoEncontrado["nombre"]}, LU: {alumnoEncontrado["LU"]:,}")
        print(f"Deuda: ${factura['monto']:,}")
        print("Detalle:")
        for clase in factura["clases"]:
          print(f"   {clase["materia"]} - {dias[clase["dia"]]} {turnos[clase["turno"]]}")
      ...
    elif opcion == "3":   # Marcar factura como pagada
      print("opcion 3")
      # facturasModule.marcarComoPagada(facturas)
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

if __name__ == "__main__":
  main()
