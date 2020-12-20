# crear una lista de palabras
palabras = []

#cantidad de palabras
pregunta = int(input(' cuantas palabras deseas agregar '))

#llenando la lista
for x in range(pregunta):
  p = str(input(' que palabras desea agregar '))
  palabras.append(p)

print('la lista de palabras son', palabras)

#el programa escribe la lista
print('el programa muestra la lista completa de palabras que son', palabras)
