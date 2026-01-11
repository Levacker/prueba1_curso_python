# --- FUNCIÓN PRINCIPAL DE ENTRADA Y RESUMEN ---
def ingresar_calificaciones():
  lista_materias = []
  lista_notas = []
  
  # Bloque de inicio de entrada de datos
  print("¿Quieres introducir materias y notas? Y (yes) or No (no)")
  respuesta = input()
  
  if(respuesta == 'Y' or respuesta == 'y'):
    # Bucle principal para ingresar materias
    while(respuesta == 'Y' or respuesta == 'y'):
      print("Introduzca la materia que ha cursado:")
      materia = input()
      lista_materias.append(materia)
      
      # Entrada y validación de nota
      print("Introduza la nota de la materia anterior:")
      nota = float(input())
      
      while(nota<0 or nota>10):
        print("Valor no valido, las notas deben de tener un valor entre el 0 y el 10")
        print("Introduza la nota correcta de la materia anterior:")
        nota = float(input())
        
      lista_notas.append(nota)  
      
      print("¿Quieres seguir introduciendo materias y notas? Y (yes) or No (no)")
      respuesta = input()
      # --- Salida ---
      
  if not lista_materias:
    print("\nNo se ha ingresado ninguna materia. No se puede generar el resumen.")
    return lista_materias, lista_notas
      
  print("\nMATERIAS Y NOTAS\n")
  for i in range (0, len(lista_materias)):
    print("En " + lista_materias[i] + " tienes la calificacion sigueinte: "+ str(lista_notas[i]))
    
  print("\nMEDIA GENERAL\n")
  print("Esta es tu media general de notas:"+ str(calcular_promedio(lista_notas)))
  
  # Determinación y presentación de aprobadas/suspensas
  aprobadas, suspensas = determinar_estado(lista_notas,5)
  
  if(len(aprobadas)==0):
    print("\nHay que estudiar mas, no has aprobado ninguna asignatura\n")
  else:
    print("\nEstas son tus asignaturas aprobadas:\n")
    
    for i in aprobadas:
      print(lista_materias[i])
  if(len(suspensas)==0):
    print("\nEres muy buen estudiante, no tienes ninguna asignatura suspensa\n")
  else:
    print("\nEstas son tus asignaturas suspensas:\n")
    for i in suspensas:
      print(lista_materias[i])
      
  # Presentación de extremos (máxima y mínima nota)
  nota_max, nota_min = encontrar_extremos(lista_notas)
  print("\nLa mejor nota la has conseguido en "+ lista_materias[nota_max] +" y conseguiste sacar un "+ str(lista_notas[nota_max]))
  print("\nLa peor nota la has conseguido en "+ lista_materias[nota_min] +" y conseguiste sacar un " + str(lista_notas[nota_min]))
  
  return lista_materias, lista_notas

# --- FUNCIONES AUXILIARES ---

def calcular_promedio(calificaciones):
  # Devuelve el promedio o 0 si la lista está vacía
  if not calificaciones :
    return 0
  promedio = sum(calificaciones)/ len(calificaciones)
  return promedio
  
def determinar_estado(calificaciones, umbral):
  # Devuelve los índices de las materias aprobadas/suspensas
  aprobadas = []
  suspensas = []
  for i in range (0, len(calificaciones)):
    if(calificaciones[i]<umbral):
      suspensas.append(i)
    else:
      aprobadas.append(i)
  return(aprobadas, suspensas)
      
def encontrar_extremos(calificaciones):
  # Devuelve el índice de la nota máxima y mínima
  nota_max = max(calificaciones)
  nota_min= min(calificaciones)
  return(calificaciones.index(nota_max), calificaciones.index(nota_min))

# --- PUNTO DE ENTRADA DEL PROGRAMA ---
if __name__ == "__main__":
  # Ejecuta la función principal
    ingresar_calificaciones()
    # Mensaje de despedida
    print("\nEsta es toda la informacion conseguida, hasta pronto")