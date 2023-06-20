# Guia n°5: Ordenamiento

# Ejercicio N° 1

# Escribe un programa que solicite al usuario una serie de 10 números separados por espacios y luego ordene esos números de forma ascendente. Utiliza el algoritmo de ordenamiento de burbuja para implementar la solución.
#%%

# lista = [55, 66, 44, 77, 33, 88, 22, 99, 11, 45]

def ordenamiento_burbuja():

  lista = []

  for i in range (0, 10):
    numero = int(input(f'Ingresa un número entero (faltan {10 - i} ingresos \n>>> '))
    lista.append(numero)

  for i in range (1, len(lista)):
    for j in range (0, len(lista) - 1):
      if lista[j] > lista[j+1]:
        aux = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = aux

  print(lista)

ordenamiento_burbuja()

# - - - - - - - - - - - - - - - - - - 

# Ejercicio N° 2

# Escribe un programa que solicite al usuario una serie de 10 palabras separadas por espacios y luego ordene esas palabras alfabéticamente.

# Utiliza el método sort() para ordenar la lista de palabras.
# %%

def ordenar_alfabeticamente():

  lista = []

  for i in range (0, 10):
    palabra = input(f'Ingresa una palabra (faltan {10 - i} ingresos \n>>> ')
    lista.append(palabra)

  lista.sort()

  print(lista)

ordenar_alfabeticamente()

# - - - - - - - - - - - - - - - - - - 

# Ejercicio N° 3

# Escribe un programa que solicite al usuario ingresar una lista de 8 números enteros separados por espacios. Luego, utiliza el método de ordenamiento por inserción para ordenar la lista en orden ascendente. Finalmente, muestra la lista ordenada al usuario.

# Requisitos adicionales:

# El programa debe manejar correctamente los números negativos.
# El programa debe validar que se ingresen únicamente números enteros y manejar errores en caso contrario.
# %%

# lista = [55, 66, 44, 77, 33, 88, 22, 99, 11, 45]

def ordenamiento_insercion():
  lista = []
  cantidad_numeros_restantes = 8

  while cantidad_numeros_restantes > 0:
    try:
      numero = int(input(f'Ingresa un número entero (faltan {cantidad_numeros_restantes} ingresos \n>>> '))
      lista.append(numero)
      cantidad_numeros_restantes -= 1
    except:
      print('Error: Solo serán válidos los ingresos de números enteros')
      continue

  for i in range (1, len(lista)):
    j = i    
    while j > 0 and lista[j-1] > lista[j]:
      aux = lista[j-1]
      lista[j-1] = lista[j]
      lista[j] = aux
      j = j - 1
  
  print(lista)
    
ordenamiento_insercion()

# - - - - - - - - - - - - - - - - - - 

# Ejercicio N° 4

# Escribe un programa que solicite al usuario ingresar una lista de 8 números enteros separados por espacios. Luego, utiliza el método de ordenamiento por selección para ordenar la lista en orden ascendente. Finalmente, muestra la lista ordenada al usuario.

# Requisitos adicionales:

# El programa debe manejar correctamente los números negativos.
# El programa debe validar que se ingresen únicamente números enteros y manejar errores
# en caso contrario.
# %%

# lista = [55, 66, 44, 77, 33, 88, 22, 99, 11, 45]

def ordenamiento_seleccion():
  lista = []
  cantidad_numeros_restantes = 8

  while cantidad_numeros_restantes > 0:
    try:
      numero = int(input(f'Ingresa un número entero (faltan {cantidad_numeros_restantes} ingresos \n>>> '))
      lista.append(numero)
      cantidad_numeros_restantes -= 1
    except:
      print('Error: Solo serán válidos los ingresos de números enteros')
      continue

  for j in range (0, len(lista) - 1):
    i_min = j
    
    for i in range (j + 1, len(lista)):
      if lista[i] < lista[i_min]:
        i_min = i

    if i_min != j:
      aux = lista[j]
      lista[j] = lista[i_min]
      lista[i_min] = aux

  print(lista)

ordenamiento_seleccion()

# - - - - - - - - - - - - - - - - - - 

# Búsqueda

# Ejercicio N° 1

# Escribe una función que tome una lista de números y un valor objetivo, y realice una búsqueda lineal para determinar si el valor objetivo está presente en la lista. La función debe devolver True si el valor objetivo se encuentra en la lista y False en caso contrario.
# %%

lista = [55, 66, 44, 77, 33, 88, 22, 99, 11, 45]

def busqueda_linear(lista, numero_objetivo):
  for num in lista:
    if num == numero_objetivo:
      return True

  return False

print(busqueda_linear(lista, 55))
print(busqueda_linear(lista, 56))

# - - - - - - - - - - - - - - - - - - 

# Ejercicio N° 2

# Escribe una función que tome una lista de 12 números ordenados de forma ascendente y un valor objetivo, y realice una búsqueda binaria para determinar si el valor objetivo está presente en la lista.

# La función debe devolver True si el valor objetivo se encuentra en la lista y False en caso contrario.
# %%

lista = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101]

def busqueda_binaria(lista, numero_objetivo):
  indice_mitad = len(lista) // 2

  if indice_mitad == 0 and lista[indice_mitad] != numero_objetivo:
    return False
  
  if lista[indice_mitad] == numero_objetivo:
    return True
  else:
    if lista[indice_mitad] > numero_objetivo:
      return busqueda_binaria(lista[0:indice_mitad],numero_objetivo)
    else:
      return busqueda_binaria(lista[indice_mitad: len(lista)], numero_objetivo)

print(busqueda_binaria(lista, 55))
print(busqueda_binaria(lista, 56))
print(busqueda_binaria(lista, 11))

# %%
