import random

# Materias & Clases

materias = [{"id": 1, "nombre": "Matemática Discreta"},
  {"id": 2, "nombre": "Álgebra y Geometría Analítica"},
  {"id": 3, "nombre": "Análisis Matemático I"},
  {"id": 4, "nombre": "Algoritmos y Estructuras de Datos"},
  {"id": 5, "nombre": "Arquitectura de Computadoras"},
  {"id": 6, "nombre": "Introducción a la Programación"},
  {"id": 7, "nombre": "Sistemas y Organizaciones"},
  {"id": 8, "nombre": "Física I"},
  {"id": 9, "nombre": "Química"},
  {"id": 10, "nombre": "Inglés Técnico I"},
  {"id": 11, "nombre": "Matemática II"},
  {"id": 12, "nombre": "Probabilidad y Estadística"},
  {"id": 13, "nombre": "Programación Orientada a Objetos"},
  {"id": 14, "nombre": "Bases de Datos"},
  {"id": 15, "nombre": "Redes de Computadoras"},
  {"id": 16, "nombre": "Ingeniería de Software I"},
  {"id": 17, "nombre": "Sistemas Operativos"},
  {"id": 18, "nombre": "Ética y Deontología Profesional"},
  {"id": 19, "nombre": "Economía"},
  {"id": 20, "nombre": "Gestión de Proyectos"}
]

def generarClases(materias, cantidad):
  clases = []
  for _ in range(cantidad):
    clase = {
      "dia": random.randint(0, 4),
      "turno": random.randint(0, 2),
      "anio": 2024,
      "cuatrimestre": random.randint(0, 1),
      "materiaId": random.choice(materias)["id"]
    }
    clases.append(clase)
  return clases

def asignarNuevaClase(LU, clase, alumnos):
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" not in alumno:
        alumno["clases"] = []
      alumno["clases"].append(clase)
      return alumnos
  return alumnos


def desasignarClase(LU, clase, alumnos):
  for alumno in alumnos:
    if alumno["LU"] == LU:
      if "clases" in alumno:
        alumno["clases"].remove(clase)
      return alumnos
  return alumnos

if __name__ == "__main__":
  clases = generarClases(materias, 5)
  print(clases)
  print(asignarNuevaClase(800000, clases[0], [{"LU": 800000}]))
  print(desasignarClase(800000, clases[0], [{"LU": 800000, "clases": [clases[0]]}]))