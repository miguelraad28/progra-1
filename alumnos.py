import random
import re
import re

# Alumnos

nombres = [
  "Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Marta", 
  "José", "Lucía"
]

apellidos = [
  "García", "Martínez", "Rodríguez", "López", "González", "Pérez", "Sánchez", 
  "Ramírez", "Torres", "Flores"]

alumnos = [{
      "nombre": "Miguel",
      "apellido": "Raad",
      "DNI": 95656210,
      "LU": 1200447,
      "email": "miguelraad2020@gmail.com",
      "clases": [],
      "estado": 'Activo',
    }]

def generarAlumnos(cantidad):
  '''
  Genera una lista de alumnos con nombres, apellidos, DNI y legajos aleatorios para inicializar el programa con datos en memoria.
  '''
  
  while len(alumnos) < cantidad:
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    
    dniGenerado = random.randint(30000000, 45000000)
    
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
      "DNI": dniGenerado,
      "LU": legajoGenerado,
      "email": mailGenerado,
      "clases": [],
      "estado": 'Activo',
    }
    alumnos.append(alumno)

  return alumnos

# Uso dentro del programa

def listarAlumnos(alumnos):
  numeroDeActivos = 0 
  for alumno in alumnos:
    if alumno['estado'] == 'Activo':
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print(f"Email: {alumno["email"]}")
      print("_________________________")
      print("")
      numeroDeActivos += 1
    
  print(f"Alumnos activos totales: {numeroDeActivos}")
  return

def listarAlumnosInactivos(alumnos):
  encontradosInactivos = 0
  for alumno in alumnos:
    if alumno['estado'] == 'Inactivo':
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print(f"Email: {alumno["email"]}")
      print("_")
      print("")
      encontradosInactivos += 1
  print(f"Alumnos inactivos totales: {encontradosInactivos}")
  return

def nuevoAlumno(nombre, apellido, dni, alumnos):
  '''
  Crea un nuevo alumno y lo agrega a la lista de alumnos.
  ARGS:
    nombre: str - Nombre del alumno.
    apellido: str - Apellido del alumno.
    dni: int - DNI del alumno.
    alumnos: list - Lista de alumnos a la que se le agregará el nuevo alumno.
  '''
  legajoGenerado = random.randint(800000, 1200000)
    
  while legajoGenerado in [alumno["LU"] for alumno in alumnos]:
    legajoGenerado = random.randint(800000, 1200000)
  email = generarEmail(nombre, apellido, legajoGenerado)

  alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "DNI": dni,
    "LU": legajoGenerado,
    "email": email,
    "clases": [],
    "estado": 'Activo'
  }

  alumnos.append(alumno)
  
  return alumnos

def generarEmail(nombre, apellido, legajo):
  '''
  Genera un email a partir del nombre, apellido y legajo del alumno utilizando expresiones regulares para evitar caracteres especiales.
  '''
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

def encontrarPorLegajo(alumnos):
  legajo = int(input("Ingrese el legajo del alumno: "))
  
  encontrado = False
  alumnoEncontrado = {}
  
  for alumno in alumnos:
    if alumno["LU"] == legajo and alumno['estado'] == 'Activo':
      encontrado = True
      alumnoEncontrado = alumno   
  return [encontrado, alumnoEncontrado]

def encontrarPorDni(dni):
  '''
  Busca alumnos por DNI
  '''
  alumnoEncontrado = None
  for alumno in alumnos:
    if alumno["DNI"] == dni and alumno['estado'] == 'Activo':
      alumnoEncontrado = alumno
  return alumnoEncontrado

def borrarAlumnoLogico(LU, alumnos):
    for alumno in alumnos:
        if alumno["LU"] == LU:
            alumno["estado"] = "Inactivo"
            print(f"El alumno con LU {LU} ha sido marcado como Inactivo.")
            return alumnos
    print(f"No se encontró un alumno con el LU {LU}.")
    return alumnos

def pedirDniNuevoAlumno():
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

      encontrado = encontrarPorDni(dni)
      if encontrado: 
        print("El dni ingresado ya está en uso")
      else:
          return dni 

def chequeaLegajo(alumnos):
  '''
  Pide el legajo y comprueba que sea valido, si no lo es o no corresponde a un alumno pide de vuelta, si lo es devuelve legajo y alumno
  '''
  while True:
    legajo = int(input("Ingrese el legajo del alumno: "))

    if 0 < legajo < 9999999:
      alumno_encontrado = False
      for alumno in alumnos:
        if legajo == alumno["LU"]:
          alumno_encontrado = alumno
          break

      if not alumno_encontrado:
        print("El legajo no coincide con ningun alumno.")
    else:
      print("El legajo debe ser un número entre 1 y 9,999,999.")

    if alumno_encontrado:
      break
  return alumno_encontrado, legajo          

if __name__ == "__main__":
  print(len(alumnos))
  print(nuevoAlumno("Juan", "Pérez", 45222555, alumnos))
  print(modificarAlumnoPorLU(800000, "nombre", "Juan Pablo", alumnos))