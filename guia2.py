# Guía n° 2 - Estructuras de datos

# Listas

# Ejercicio N° 1

# Crea una lista llamada "frutas" que contenga las siguientes frutas: manzana, banana, naranja y pera.

# Imprime en pantalla la lista completa

#%%

frutas = ["manzana", "banana", "naranja", "pera"]

print(frutas)

# - - - - - - - - - - - - - -

# Ejercicio N° 2

# En base al ej 1

# Accede al segundo elemento de la lista "frutas" e imprímelo en pantalla.

#%%

frutas = ["manzana", "banana", "naranja", "pera"]

print(frutas[1])

# - - - - - - - - - - - - - -

# Ejercicio N° 3

# En base al ej 1

# Modifica el primer elemento de la lista "frutas" y cámbialo por "Cereza".

# Imprime en pantalla la lista actualizada.
# %%

frutas = ["manzana", "banana", "naranja", "pera"]

frutas[0] = "Cereza"

print(frutas[0])

# - - - - - - - - - - - - - -

# Ejercicio N° 4

# En base al ej 1

# Agrega la fruta "sandía" al final de la lista "frutas" utilizando el método append().

# Imprime en pantalla la lista actualizada.
# %%

frutas = ["manzana", "banana", "naranja", "pera"]

frutas.append("sandía")

print(frutas)

# - - - - - - - - - - - - - -

# Ejercicio N° 5

# En base al ej 1

# Elimina la fruta "naranja" de la lista "frutas" utilizando el método remove().

# Imprime en pantalla la lista resultante.
# %%

frutas = ["manzana", "banana", "naranja", "pera"]

frutas.remove('naranja')

print(frutas)

# - - - - - - - - - - - - - -

# Ejercicio N° 6

# Crea una lista de números llamada "numeros" con valores del 1 al 5.

# Utiliza un bucle for para recorrer la lista e imprimir en pantalla cada número.
# %%

numeros = [1, 2, 3, 4, 5]

for num in numeros:
  print(num)

# - - - - - - - - - - - - - -

# Ejercicio N° 7

# Crea una lista llamada "pares" con los números pares del 2 al 10.

# Utiliza el método reverse() para invertir el orden de los elementos en la lista.

# Utiliza el método sort() para ordenar la lista de forma ascendente.

# Imprime en pantalla la lista resultante.
# %%

pares = [2, 4, 6, 8, 10]

pares.reverse()

print(pares)

pares.sort()

print(pares)

# - - - - - - - - - - - - - -

# Ejercicio N° 8

# Crea una lista llamada "cuadrados" que contenga los cuadrados de los números del 1 al
# 5.

# Utiliza la comprensión de listas para generar la lista de forma concisa.

# Imprime en pantalla la lista resultante.
# %%

cuadrados = [numeros * numeros for numeros in range (1, 6)]

print(cuadrados)

# - - - - - - - - - - - - - -

# Ejercicio N° 9

# Crea una lista llamada "nombres" con varios nombres de personas.

# Pide al usuario que ingrese un nombre y verifica si está presente en la lista.

# Muestra un mensaje en pantalla indicando si el nombre está o no en la lista.
# %%

nombres = ["Matias", "Jose", "Esteban"]

nombre_ingresado = input('Ingrese un nombre \n>>>')

if (nombre_ingresado in nombres):
  print("El nombre se encuentra en la lista")
else:
  print("El nombre no se encuentra en la lista")

# - - - - - - - - - - - - - -

# Ejercicio N° 10

# Crea una lista llamada "numeros" con valores del 1 al 10.

# Divide la lista en sublistas de tamaño 3 utilizando la técnica de slicing.

# Imprime en pantalla las sublistas resultantes.

#%%

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_resultante = []

for i in range(0, len(numeros), 3):
  lista_resultante.append(numeros[i:i+3])

print(lista_resultante)

# - - - - - - - - - - - - - -

# Diccionarios

# Ejercicio N° 1

# Crea un diccionario llamado "alumno" que contenga las siguientes claves: "nombre", "edad" y "carrera". Asigna valores adecuados a cada clave.

# Imprime en pantalla la información del alumno utilizando las claves del diccionario.
# %%

alumno = {
  "nombre": "Ivan",
  "edad": 29,
  "carrera": "Data Science"
}

print(alumno["nombre"], alumno["edad"], alumno["carrera"])

# - - - - - - - - - - - - - -

# Ejercicio N° 2

# Modifica el valor de la clave "edad" en el diccionario "alumno" y actualízalo con una nueva edad.

# Imprime en pantalla la información actualizada del alumno.
# %%

alumno["edad"] = 27

print(alumno["edad"])

# - - - - - - - - - - - - - -

# Ejercicio N° 3

# Agrega una nueva entrada al diccionario "alumno" con la clave "universidad" y un valor correspondiente a la universidad en la que estudia.

# Imprime en pantalla la información completa del alumno, incluyendo la nueva entrada.
# %%

alumno["universidad"] = 'asociación consciencia'

print(alumno['universidad'])

# - - - - - - - - - - - - - -

# Ejercicio N° 4

# Crea un diccionario llamado "calificaciones" que contenga las claves "matemáticas", "física" y "química", y asigna valores numéricos a cada una.

# Utiliza un bucle para recorrer el diccionario e imprimir en pantalla cada clave y su respectivo valor.
# %%

calificaciones = {
  "matematicas": 9,
  "fisica": 7,
  "quimica": 5
}

for materia, calificacion in calificaciones.items():
  print(f'{materia}: {calificacion}')

# - - - - - - - - - - - - - -

# Ejercicio N° 5

# En base al ej 4:

# Elimina la entrada correspondiente a la clave "química" del diccionario "calificaciones".

# Vuelve a recorrer el diccionario y muestra en pantalla las claves y valores restantes.
# %%

calificaciones = {
  "matematicas": 9,
  "fisica": 7,
  "quimica": 5
}

calificaciones.pop("quimica")

for materia, calificacion in calificaciones.items():
  print(f'{materia}: {calificacion}')

# - - - - - - - - - - - - - -

# Ejercicio N° 6

# En base al ej 4:

# Utiliza el método keys() para obtener una lista de todas las claves del diccionario "calificaciones".

# Utiliza el método values() para obtener una lista de todos los valores del diccionario.
# %%

calificaciones = {
  "matematicas": 9,
  "fisica": 7,
  "quimica": 5
}

print(calificaciones.keys())

print(calificaciones.values())

# - - - - - - - - - - - - - -

# Ejercicio N° 7

# Crea un diccionario llamado "agenda" que contenga información de contactos.

# Cada contacto debe ser representado por un diccionario con claves como "nombre", "teléfono" y "email".

# Agrega al menos tres contactos al diccionario "agenda" y muestra la información de cada contacto en pantalla.
# %%

agenda = {
  "contacto1": {
    "nombre": "Ivan",
    "telefono": 123123,
    "emal": "Ivanconsorte@mail.com"
  },
  "contacto2": {
    "nombre": "Yasmin",
    "telefono": 345345,
    "emal": "Yasmingomez@mail.com"
  },
  "contacto3": {
    "nombre": "Martina",
    "telefono": 678678,
    "emal": "Martinapapina@mail.com"
  },
}

for contacto in agenda:
  print(agenda[contacto])

# - - - - - - - - - - - - - -

# Tuplas

# Ejercicio N° 1

# Crea una tupla llamada "meses" que contenga los nombres de los meses del año como elementos.

# Imprime en pantalla la tupla completa.

# %%

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

print(meses)

# - - - - - - - - - - - - - -

# Ejercicio N° 2

# En base al ej.1

# Accede al tercer elemento de la tupla "meses" e imprímelo en pantalla.
# %%

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

print(meses[2])

# - - - - - - - - - - - - - -

# Ejercicio N° 3

# Accede al último elemento de la tupla "meses" utilizando indexación negativa.

# Imprime en pantalla el último elemento.
# %%

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

print(meses[-1])

# - - - - - - - - - - - - - -

# Ejercicio N° 4

# Intenta asignar un nuevo valor a uno de los elementos de la tupla "meses" y observa el error que se produce.

# Comenta el código erróneo y explica en un comentario por qué ocurre el error.
# %%

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

meses[0] = 'Abrete Sesamo' 

# TypeError: 'tuple' object does not support item assignment

# >>> Este error ocurre porque las tuplas son inmutables, no puede cambiarse su valor una vez está declarada

# - - - - - - - - - - - - - -

# Ejercicio N° 5

# Crea dos tuplas llamadas "tupla1" y "tupla2" con diferentes elementos.

# Concatena las dos tuplas y almacena el resultado en una nueva tupla llamada "tupla_concatenada".

# Imprime en pantalla la tupla concatenada.
# %%

tupla1 = (1, 2, 3)

tupla2 = (4, 5, 6)

tupla_concatenada = tupla1 + tupla2

print(tupla_concatenada)

# - - - - - - - - - - - - - -

# Ejercicio N° 6

# Crea una tupla llamada "coordenadas" que contenga las coordenadas x, y, z de un punto en el espacio.

# Utiliza el desempaquetado de tuplas para asignar cada valor de la tupla a variables individuales llamadas "x", "y" y "z".

# Imprime en pantalla los valores de las variables.
# %%

coordenadas = (25, 45, 75)

(x, y, z) = coordenadas

print(x, y, z)

# - - - - - - - - - - - - - -

# Ejercicio N° 7

# Crea una lista de tuplas llamada "alumnos" que contenga el nombre y la edad de varios estudiantes.

# Utiliza un bucle para iterar sobre la lista de tuplas y mostrar en pantalla el nombre y la edad de cada estudiante.
# %%

alumnos = [("Ivan", 29), ("Yasmin", 29), ("Martina", 25)]

for alumno in alumnos:
  for datos in alumno:
    print(datos)

# - - - - - - - - - - - - - -

# Sets

# Ejercicio N° 1

# Crea un conjunto llamado "frutas" que contenga las siguientes frutas: manzana, plátano, naranja y pera.

# Imprime en pantalla el conjunto completo.
# %%

frutas = {"manzana", "plátano", "naranja", "pera"}

print(frutas)

# - - - - - - - - - - - - - -

# Ejercicio N° 2

# Crea dos conjuntos: "frutas1" con las frutas manzana, plátano y pera, y "frutas2" con las frutas naranja y sandía.

# Realiza las siguientes operaciones e imprime los resultados:

# Unión de los conjuntos frutas1 y frutas2.
# Intersección de los conjuntos frutas1 y frutas2.
# Diferencia entre los conjuntos frutas1 y frutas2.
# %%

frutas1 = {"manzana", "plátano", "pera"}
frutas2 = {"naranja", "sandia"}

union_frutas = frutas1.union(frutas2)
print(union_frutas)

intersección_frutas = frutas1.intersection(frutas2)
print(intersección_frutas)

differencia_frutas = frutas1.difference(frutas2)
print(differencia_frutas)

# - - - - - - - - - - - - - -

# Ejercicio N° 3

# Crea un conjunto vacío llamado "numeros". 

# Agrega los números del 1 al 5 al conjunto utilizando el método add().

# Elimina el número 3 del conjunto utilizando el método remove() o discard().

# Imprime en pantalla el conjunto resultante.
# %%

numeros = set()

for i in range(1, 6):
  numeros.add(i)

numeros.remove(3)

print(numeros)

# - - - - - - - - - - - - - -

# Ejercicio N° 4

# Crea un conjunto llamado "vocales" que contenga las vocales del alfabeto.

# Pide al usuario que ingrese una letra y verifica si esa letra está presente en el conjunto "vocales".

# Muestra un mensaje en pantalla indicando si la letra es una vocal o no.
# %%

vocales = {"a", "e", "i", "o", "u"}

letra = input('Ingrese una letra \n>>> ')

if letra in vocales:
  print("La letra es una vocal")
else:
  print("La letra no es una vocal")

# - - - - - - - - - - - - - -

# Ejercicio N° 5

# Crea una lista llamada "numeros_repetidos" que contenga números repetidos.

# Convierte la lista en un conjunto utilizando la función set() para eliminar los elementos duplicados.

# Convierte el conjunto resultante nuevamente en una lista y muéstrala en pantalla.
# %%

numeros_repetidos = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6]

numeros_repetidos = set(numeros_repetidos)

numeros_repetidos = list(numeros_repetidos)

print(numeros_repetidos)

# - - - - - - - - - - - - - -

# Ejercicio N° 6

# Crea dos conjuntos: "set1" con los números del 1 al 5, y "set2" con los números del 4 al 8. 

# Utiliza los métodos de conjuntos para realizar las siguientes operaciones e imprime los resultados:

# Obtener la diferencia simétrica entre set1 y set2.

# Comprobar si set1 es un subconjunto de set2.

# Comprobar si set2 es un subconjunto propio de set1.
#%%

set1 = set()

set2 = set()

for i in range(1, 9):
  if i < 5:
    set1.add(i)
  else:
    set2.add(i)

print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issuperset(set1))

# - - - - - - - - - - - - - -

# Ejercicio N° 7

# Crea dos conjuntos llamados "set_a" y "set_b" con elementos en común.

# Utiliza un método de conjuntos para eliminar los elementos comunes de set_a en relación con set_b.

# Imprime en pantalla el conjunto resultante de set_a.
# %%

set_a = {1, 2, 3, 4, 5}

set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b))
# %%

