import random

# Alumnos

nombres = [
  "Juan", "María", "Carlos", "Ana", "Luis", "Pedro", "Sofía", "Marta", "Jorge", "Lucía",
  "Miguel", "Laura", "Andrés", "Elena", "Raúl", "Carmen", "Diego", "Paula", "Fernando", "Isabel",
  "Ricardo", "Patricia", "Gabriel", "Verónica", "Hugo", "Natalia", "Esteban", "Silvia", "Alberto", "Rosa",
  "Francisco", "Claudia", "Manuel", "Adriana", "Javier", "Beatriz", "Gustavo", "Alicia", "Roberto", "Gloria",
  "Sergio", "Daniela", "Eduardo", "Victoria", "Enrique", "Julia", "Oscar", "Monica", "Rafael", "Teresa"
]

apellidos = [
  "Pérez", "García", "Rodríguez", "López", "Martínez", "Sánchez", "Ramírez", "Torres", "Flores", "Rivera",
  "Gómez", "Díaz", "Vargas", "Castro", "Ortiz", "Morales", "Silva", "Ramos", "Reyes", "Cruz",
  "Mendoza", "Herrera", "Jiménez", "Rojas", "Navarro", "Romero", "Soto", "Suárez", "Molina", "Delgado",
  "Moreno", "Aguilar", "Ortiz", "Medina", "Vega", "Campos", "Guerrero", "Pena", "Cabrera", "Vargas",
  "Castillo", "Ramos", "Chávez", "Ríos", "Vargas", "Figueroa", "Cortés", "Pacheco", "Miranda", "Espinoza"
]

def generarAlumnos():
  alumnos = []
  
  for nombre in nombres:
    for apellido in apellidos:
      persona = {
        "nombre": nombre,
        "apellido": apellido,
        "LU": random.randint(800000, 1200000)
      }
      alumnos.append(persona)
  
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


if __name__ == "__main__":
  alumnos = generarAlumnos()
  print(alumnos)
  print(nuevoAlumno("Juan", "Pérez", alumnos))
  print(modificarAlumnoPorLU(800000, "nombre", "Juan Pablo", alumnos))