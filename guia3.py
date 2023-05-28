# Guía n°3 - Funciones

# Ejercicio N° 1

# Escribe una función llamada "saludo" que no reciba parámetros y y muestre el mensaje "¡Hola!".

#%%
def saludo():
  print("¡Hola!") 

saludo()

# - - - - - - - - - - - - - - -

# Ejercicio N° 2

# Escribe una función llamada "saludo" que reciba un nombre como parámetro y muestre el mensaje "¡Hola, [nombre]!".

#%%

def saludo(nombre):
  print(f"¡Hola, {nombre}!")

saludo('Ivan')

# - - - - - - - - - - - - - - -

# Ejercicio N° 3

# Crea una función llamada "suma" que reciba dos números como parámetros y devuelva la suma de ambos.

# Llama a la función con diferentes pares de números e imprime el resultado

#%%

def suma(n1, n2):
  return n1 + n2

print(suma(33, 66))
print(suma(2, 1))
print(suma(45, 51))

# - - - - - - - - - - - - - - -

# Ejercicio N° 4

# Define una función llamada "saludo_personalizado" que reciba un nombre y un saludo opcionalmente. Si no se proporciona un saludo, debe utilizar "¡Hola" como saludo predeterminado.

# Llama a la función para saludar a diferentes personas con y sin saludo personalizado.

#%%

def saludo_personalizado(nombre, saludo = 'Hola'):
  print(f"¡{saludo}, {nombre}!")

saludo_personalizado('Ivan')
saludo_personalizado('Ivan', 'Cómo estas')

# - - - - - - - - - - - - - - -

# Ejercicio N° 5

# Escribe una función llamada "promedio" que acepte una cantidad variable de números y calcule su promedio.

# Llama a la función con diferentes conjuntos de números y muestra el promedio resultante.

#%%

def promedio(*numeros):
  suma = 0
  for num in numeros:
    suma += num
  return suma / len(numeros)

print(promedio(3, 3, 3))

print(promedio(3, 5, 7))

print(promedio(9, 26, 11))

# - - - - - - - - - - - - - - -

# Ejercicio N° 6

# Crea una función llamada "factorial" que calcule el factorial de un número dado.

# Utiliza la recursividad para implementar la función.

# Prueba la función con diferentes números y muestra los resultados.
# %%

def factorial (num):
  if num < 1:
    return 1
  return num * factorial(num - 1)

print(factorial(4))
print(factorial(6))

# - - - - - - - - - - - - - - -

# Ejercicio N° 7

# Escribe una función llamada "ordenar_lista" que reciba una lista de números y devuelva una nueva lista con los mismos números ordenados de forma ascendente.

# Utiliza una función integrada de Python para realizar la clasificación.

# Prueba la función con diferentes listas de números.
# %%

def ordenar_lista(lista):
  lista.sort()
  return lista

print(ordenar_lista([4,6,3,89,32,45,87]))
print(ordenar_lista([345, 567, 23, 675, 333, 0]))

# - - - - - - - - - - - - - - -

# Ejercicio N° 8

# Define una función llamada "dividir" que acepte dos números y realice la división del primero por el segundo.

# Maneja la excepción que se produce cuando el divisor es igual a cero y muestra un mensaje de error adecuado.

# Llama a la función con diferentes pares de números, incluido el caso en el que el divisor sea cero.
# %%

def dividir(num1, num2):
  if num2 == 0:
    return "El divisor no puede ser igual a cero"
  return num1 / num2

print(dividir(5, 2))
print(dividir(345, 34))
print(dividir(3, 0))

# - - - - - - - - - - - - - - -

# Ejercicio N° 9

# Crea una función llamada "informacion_persona" que acepte los siguientes parámetros: nombre, edad y ciudad.

# La función debe imprimir en pantalla la información proporcionada en un formato
# legible, como "Nombre: [nombre], Edad: [edad], Ciudad: [ciudad]". Llama a la función utilizando argumentos de palabras clave para especificar los valores de los parámetros.
# %%

def informacion_persona(nombre, edad, ciudad):
  print(f'Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}')

informacion_persona('Ivan', '29', 'Mar del Plata')
informacion_persona('Yasmin', '25', 'Buenos Aires')
informacion_persona('Jonas', '19', 'Mar de Ajó')

# - - - - - - - - - - - - - - -

# Ejercicio N° 10

# Define una función llamada "dividir" que acepte dos números y realice la división del primero por el segundo.

# Maneja la excepción que se produce cuando el divisor es igual a cero y muestra un mensaje de error adecuado.

# Llama a la función con diferentes pares de números, incluido el caso en el que el divisor sea cero.
# %%

def dividir(num1, num2):
  if num2 == 0:
    return "El divisor no puede ser igual a cero"
  return num1 / num2

print(dividir(5, 2))
print(dividir(345, 34))
print(dividir(3, 0))

# - - - - - - - - - - - - - - -

# Ejercicio N° 11

# Define una función llamada "concatenar_strings" que acepte una cantidad
# variable de cadenas de texto y las concatene en una sola cadena.

# Utiliza el operador de concatenación de cadenas o el método join() para realizar la concatenación.

# Prueba la función con diferentes cadenas y muestra el resultado.
# %%

def concatenar_strings(*strings):
  return "".join(strings)

print(concatenar_strings('Hola,', ' Cesar'))
print(concatenar_strings('Hola, ', 'Cesar ', '¿Cómo ', 'estás?'))

# - - - - - - - - - - - - - - -

# Ejercicio N° 12

# Escribe una función llamada "eliminar_duplicados" que reciba una lista como parámetro y devuelva una nueva lista que contenga los elementos únicos de la lista
# original, sin duplicados.

# Utiliza las propiedades de los conjuntos (set) para eliminar los elementos duplicados.

# Prueba la función con diferentes listas y muestra el resultado.
# %%

def eliminar_duplicados(lista):
  lista = set(lista)
  lista = list(lista)
  return lista

print(eliminar_duplicados([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]))
print(eliminar_duplicados([234, 234, 234, 234, 456, 456, 456, 678, 678]))

# - - - - - - - - - - - - - - -

# Ejercicio N° 13

# Crea una función recursiva llamada "fibonacci" que calcule el enésimo número de la secuencia de Fibonacci.

# La secuencia de Fibonacci comienza con 0 y 1, y cada número siguiente se calcula sumando los dos números anteriores.

# Prueba la función para obtener diferentes números de la secuencia de Fibonacci.
# %%

def fibonacci(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(4))
print(fibonacci(7))
print(fibonacci(11))

# - - - - - - - - - - - - - - -

# Ejercicio N° 14

# Crea una función llamada "generar_numero_aleatorio" que utilice el
# módulo random de Python para generar un número entero aleatorio entre un rango dado.

# El rango debe ser especificado como parámetros de la función.

# Llama a la función para generar diferentes números aleatorios y muestra los resultados.
# %%

import random

def generar_mumero_aleatorio(num1, num2):
  return random.randint(num1, num2)

print(generar_mumero_aleatorio(1, 5))
print(generar_mumero_aleatorio(1, 33))
print(generar_mumero_aleatorio(45, 78))

# - - - - - - - - - - - - - - -

# Ejercicio N° 15

# Escribe una función llamada "contar_lineas" que acepte el nombre de un archivo como parámetro y cuente el número total de líneas en ese archivo.

# Utiliza el manejo de archivos en Python para abrir y leer el archivo.

# Llama a la función con diferentes archivos y muestra el número de líneas resultante.
# %%

def contar_lineas(archivo):
  with open(f'{archivo}') as f:
    lines = f.readlines()
    return len(lines)

contar_lineas('guia1.py')
contar_lineas('guia2.py')
contar_lineas('guia3.py')

# - - - - - - - - - - - - - - -

# Ejercicio N° 16

# Escribe una función llamada "calcular_estadisticas" que reciba una tupla de números como parámetro y devuelva la suma, el promedio y el máximo valor de la tupla.

# Llama a la función con diferentes tuplas de números y muestra los resultados obtenidos.
# %%

def calcular_estadística(tupla):
  suma = 0
  max = tupla[0]

  for element in tupla:
    suma += element
    if element > max:
      max = element
  
  return suma, max, suma / len(tupla)

print(calcular_estadística((1, 2, 3, 4, 5, 6)))
print(calcular_estadística((7, 8, 9, 10, 11, 12)))

# %%
