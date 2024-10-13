import random

# Alumnos

nombres = [
  "Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Marta", 
  "José", "Lucía"
]

apellidos = [
  "García", "Martínez", "Rodríguez", "López", "González", "Pérez", "Sánchez", 
  "Ramírez", "Torres", "Flores"]

alumnos = []
def generarAlumnos(cantidad):
  '''
  Genera una lista de alumnos con nombres, apellidos, DNI y legajos aleatorios para inicializar el programa con datos en memoria.
  '''
  
  while len(alumnos) < cantidad:
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    
    dni_generado = random.randint(30000000, 45000000)
    
    while dni_generado in [alumno["DNI"] for alumno in alumnos]:
      dni_generado = random.randint(30000, 45000000)
      
    legajo_generado = random.randint(800000, 1200000)
    
    while legajo_generado in [alumno["LU"] for alumno in alumnos]:
      legajo_generado = random.randint(800000, 1200000)
    
    mail_generado = str(f"{nombre[0].lower()}{apellido.lower()}.{legajo_generado}@edau.edu.ar")

    while mail_generado in [alumno["Mail"] for alumno in alumnos]:
      mail_generado = str(f"{nombre[0].lower()}{apellido.lower()}.{legajo_generado}@edau.edu.ar")

    estado = 'Activo'
    
    alumno = {
      "nombre": nombre,
      "apellido": apellido,
      "DNI": dni_generado,
      "LU": legajo_generado,
      "Mail": mail_generado,
      "Estado": estado
    }
    alumnos.append(alumno)

  return alumnos

# Uso dentro del programa

def listarAlumnos(alumnos):
  for alumno in alumnos:
    print(f"Nombre: {alumno["nombre"]}")
    print(f"Apellido: {alumno["apellido"]}")
    print(f"D.N.I: {alumno["DNI"]:,}")
    print(f"L.U: {alumno["LU"]:,}")
    print(f"Mail: {alumno["Mail"]}")
    print("_________________________")
    print("")

    print(f"Alumnos activos totales: {sum(1 for alumno in alumnos if alumno['Estado'] == 'Activo')}")
  return

def listarAlumnosInactivos(alumnos):
  for alumno in alumnos:
    if alumno['Estado'] == 'Inactivo':
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print(f"Mail: {alumno["Mail"]}")
      print("_")
      print("")
  print(f"Alumnos inactivos totales: {sum(1 for alumno in alumnos if alumno['Estado'] == 'Inactivo')}")
  return

def nuevoAlumno(nombre, apellido, dni, alumnos):
  legajoU = random.randint(800000, 1200000)
  alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "DNI": dni,
    "LU": legajoU,
    "Mail": generarMail(nombre, apellido, legajoU),
    "Estado": 'Activo'
  }
  
  alumnos.append(alumno)
  
  return alumnos

def generarMail(nombre, apellido, legajo):
  '''
  Genera un mail teniendo en cuenta la primera letra del nombre, el apellido y el legajo
  '''
  mail = str(f"{nombre[0].lower()}{apellido.lower()}.{legajo}@edau.edu.ar")
  return mail

def modificarAlumnoPorLU(LU, propiedad, nuevoValor, alumnos):
  for alumno in alumnos:
    if alumno["LU"] == LU:
      alumno[propiedad] = nuevoValor
      return alumnos
  return alumnos

def encontrarPorLegajo():
  legajo = int(input("Ingrese el legajo del alumno: "))
  
  encontrado = False
  alumnoEncontrado = {}
  
  for alumno in alumnos:
    if alumno["LU"] == legajo:
      encontrado = True
      alumnoEncontrado = alumno
  else:
    print("No se encontró un alumno con el legajo ingresado.")
    
  return [encontrado, alumnoEncontrado]

def encontrarPorDni():
  '''
  Busca alumnos por DNI
  '''
  dni = int(input("Ingrese el dni del alumno: "))
  
  for alumno in alumnos:
    if alumno["DNI"] == dni:
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print(f"Mail: {alumno["Mail"]:,}")
      print("_________________________")
      print("")
      break
  else:
    print("No se encontró un alumno con el DNI ingresado.")
  return

def borrarAlumnoLogico(LU, alumnos):
    for alumno in alumnos:
        if alumno["LU"] == LU:
            alumno["Estado"] = "Inactivo"
            print(f"El alumno con LU {LU} ha sido marcado como Inactivo.")
            return alumnos
    print(f"No se encontró un alumno con el LU {LU}.")
    return alumnos

def pideDNI(alumnos):
    '''
    Controla que el DNI ingresado no haya sido utilizado por otro alumno
    '''
    while True:
      dni = int(input("Ingrese el DNI del alumno: "))
      if dni <= 0:
          print("El DNI debe ser un número positivo.")
          continue
      if len(str(dni)) < 7 or len(str(dni)) > 8:
          print("El DNI debe tener entre 7 y 8 dígitos.")
          continue

      encontrado = False 
      for alumno in alumnos:
          if alumno["DNI"] == dni:
              encontrado = True
              break
      if encontrado:
          print("DNI existente. Por favor, ingrese otro.")
      else:
          return dni 

if __name__ == "__main__":
  print(len(alumnos))
  print(nuevoAlumno("Juan", "Pérez", 45222555, alumnos))
  print(modificarAlumnoPorLU(800000, "nombre", "Juan Pablo", alumnos))