import random

# Alumnos

nombres = [
  "Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Marta", 
  "José", "Lucía", "Miguel", "Elena", "Jorge", "Sofía", "Raúl", "Carmen", 
  "Andrés", "Patricia", "Sergio", "Isabel"
]

apellidos = [
  "García", "Martínez", "Rodríguez", "López", "González", "Pérez", "Sánchez", 
  "Ramírez", "Torres", "Flores", "Rivera", "Gómez", "Díaz", "Cruz", "Morales", 
  "Ortiz", "Vargas", "Castillo", "Jiménez", "Ramos"
]

alumnos = []
def generarAlumnos(cantidad):
  legajos_usados = set()
  
  while len(alumnos) < cantidad:
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    LU = random.randint(800000, 1200000)
    
    if LU not in legajos_usados:
      legajos_usados.add(LU)
      alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "LU": LU
      }
      alumnos.append(alumno)
  
  return alumnos

# Uso dentro del programa

def nuevoAlumno(nombre, apellido, alumnos):
  alumno = {
    "nombre": nombre,
    "apellido": apellido,
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
  
  for alumno in alumnos:
    if alumno["LU"] == legajo:
      print("*** alumno encontrado")
      print(alumno)
      return  alumno
  else:
    print("No se encontró un alumno con el legajo ingresado.")

if __name__ == "__main__":
  print(len(alumnos))
  print(nuevoAlumno("Juan", "Pérez", alumnos))
  print(modificarAlumnoPorLU(800000, "nombre", "Juan Pablo", alumnos))