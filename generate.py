import json
import random

file = open("data_alumnos.json", "r", encoding='utf-8')
alumnos = json.load(file)
file2 = open("data_clases.json", "r", encoding='utf-8')
clases = json.load(file2)
file3 = open("data_materias.json", "r", encoding='utf-8')
materias = json.load(file3)
file4 = open("data_facturas.json", "r", encoding='utf-8')
facturas = json.load(file4)

def encontrarClasePorId(id):
  for clase in clases:
    if clase['id'] == id:
      return clase


todosLosTurnos = [[clase for clase in clases if clase['turno'] == 0],[clase for clase in clases if clase['turno'] == 1], [clase for clase in clases if clase['turno'] == 2]]

count = 0
clasesUsadas = []
for i in range(len(alumnos)):
  clasesPorTurno = todosLosTurnos[count]
  for j in range(random.randint(1,len(clasesPorTurno))):
    clase = random.choice(clasesPorTurno)

    loop = 0
    reachedMaxLoop = False
    while (clase["id"] in [clase["id"] for clase in clasesUsadas]) or (clase["materiaId"] in [clase["materiaId"] for clase in clasesUsadas]) or (clase["dia"] in [clase["dia"] for clase in clasesUsadas]):
      if loop > 10:
        reachedMaxLoop = True
        break
      clase = random.choice(clasesPorTurno)
      loop +=1

    if not reachedMaxLoop:
      clasesUsadas.append(clase)

  alumnos[i]["clases"] = [clase["id"] for clase in clasesUsadas[:7]]

  clasesUsadas = []
  if count == 2:
    count = 0
  else:
    count += 1
    
for alumno in alumnos:
  print(alumno["clases"])
  
  
with open("data_alumnos.json", "w", encoding='utf-8') as file:
  json.dump(alumnos, file, indent=4, ensure_ascii=False)