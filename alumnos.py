import random
import re

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
    
    while dniGenerado in [alumno["DNI"] for alumno in alumnos]:
      dniGenerado = random.randint(300000, 45000000)
      
    legajoGenerado = random.randint(800000, 1200000)
    
    while legajoGenerado in [alumno["LU"] for alumno in alumnos]:
      legajoGenerado = random.randint(800000, 1200000)
    
    # Ya el legajo es único asi que por lo tanto el email también.
    mailGenerado = str(f"{nombre[0].lower()}{apellido.lower()}.{legajoGenerado}@edau.edu.ar")

    alumno = {
      "nombre": nombre,
      "apellido": apellido,
      "DNI": dni_generado,
      "LU": legajoGenerado,
      "email": mailGenerado,
      "clases": [],
      "estado": 'Activo',
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
    print(f"Email: {alumno["email"]}")
    print("_________________________")
    print("")
    
    print(f"Alumnos activos totales: {sum(1 for alumno in alumnos if alumno['estado'] == 'Activo')}")
  return

def listarAlumnosInactivos(alumnos):
  for alumno in alumnos:
    if alumno['estado'] == 'Inactivo':
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print(f"Email: {alumno["email"]}")
      print("_")
      print("")
  print(f"Alumnos inactivos totales: {sum(1 for alumno in alumnos if alumno['estado'] == 'Inactivo')}")
  return

def nuevoAlumno(nombre, apellido, email, dni, alumnos):
  legajoGenerado = random.randint(800000, 1200000)
    
  while legajoGenerado in [alumno["LU"] for alumno in alumnos]:
    legajoGenerado = random.randint(800000, 1200000)
  
  email = generarMail(nombre, apellido, legajoGenerado)
  
  alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "DNI": dni,
    "LU": legajoGenerado,
    "email": email,
    "estado": 'Activo'
  }

  alumnos.append(alumno)
  
  return alumnos

def generarMail(nombre, apellido, legajo):
    nombreSinEspaciosYLimpio = re.sub(r'[^a-zA-Z]', '', nombre).lower()
    apellidoSinEspaciosYLimpio = re.sub(r'[^a-zA-Z]', '', apellido).lower()
    mail = f"{nombreSinEspaciosYLimpio[0]}{apellidoSinEspaciosYLimpio}.{legajo}@edau.edu.ar"
    return mail

def modificarAlumnoPorLU(LU, propiedad, nuevoValor, alumnos):
  if propiedad not in ["nombre", "apellido"]:
    print("Solo se permite modificar el nombre o apellido.")
    return alumnos
  
  for alumno in alumnos:
    if alumno["LU"] == LU:
      alumno[propiedad] = nuevoValor
      return alumnos
  print("No se encontró un alumno con el LU ingresado.")
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
      print(f"Email: {alumno["email"]:,}")
      print("_________________________")
      print("")
      break
  else:
    print("No se encontró un alumno con el DNI ingresado o lo ingresado no fue valido.")
  return

def borrarAlumnoLogico(LU, alumnos):
    for alumno in alumnos:
        if alumno["LU"] == LU:
            alumno["estado"] = "Inactivo"
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