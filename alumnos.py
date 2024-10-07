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
      dni_generado = random.randint(30000000, 45000000)
      
    legajo_generado = random.randint(800000, 1200000)
    
    while legajo_generado in [alumno["LU"] for alumno in alumnos]:
      legajo_generado = random.randint(800000, 1200000)
    
    alumno = {
      "nombre": nombre,
      "apellido": apellido,
      "DNI": dni_generado,
      "LU": legajo_generado
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
    print("_________________________")
    print("")

  print(f"Alumnos totales: {len(alumnos)}")
  return

def nuevoAlumno(nombre, apellido, dni, alumnos):
  alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "DNI": dni,
    "LU": random.randint(800000, 1200000)
  }
  
  alumnos.append(alumno)
  
  return alumnos

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
  dni = int(input("Ingrese el dni del alumno: "))
  
  for alumno in alumnos:
    if alumno["DNI"] == dni:
      print(f"Nombre: {alumno["nombre"]}")
      print(f"Apellido: {alumno["apellido"]}")
      print(f"D.N.I: {alumno["DNI"]:,}")
      print(f"L.U: {alumno["LU"]:,}")
      print("_________________________")
      print("")
      break
  else:
    print("No se encontró un alumno con el legajo ingresado.")
  return

if __name__ == "__main__":
  print(len(alumnos))
  print(nuevoAlumno("Juan", "Pérez", 45222555, alumnos))
  print(modificarAlumnoPorLU(800000, "nombre", "Juan Pablo", alumnos))