# Guia n°5: Ordenamiento

# Ejercicio N° 1

# Escribe un programa que solicite al usuario una serie de 10 números separados por espacios y luego ordene esos números de forma ascendente. Utiliza el algoritmo de ordenamiento de burbuja para implementar la solución.
#%%

# lista = [55, 66, 44, 77, 33, 88, 22, 99, 11, 45]

def ordenamiento_burbuja():

  ingreso = input('Ingresa una serie de 10 números separados por espacios a ordenar').split()

  lista = []

  for numero in ingreso:
    numero = int(numero)
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

  lista = input('Ingrese una serie de 10 palabras separadas por espacios ha ser ordenadas alfabéticamente')
  lista = lista.split(" ")

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
  comprobado = False
  
  lista = []

  while comprobado == False:
    ingreso = input('Ingresa una serie de 8 números separados por espacios a ordenar').split()

    error = False

    for numero in ingreso:
      try:
        numero = int(numero)
      except:
        print('Error: Uno de los ingresos no fue un número válido')
        error = True
    
    if error == False:
      comprobado = True    
    
  for numero in ingreso:
    numero = int(numero)
    lista.append(numero)

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
  comprobado = False
  
  lista = []

  while comprobado == False:
    ingreso = input('Ingresa una serie de 8 números separados por espacios a ordenar').split()

    error = False

    for numero in ingreso:
      try:
        numero = int(numero)
      except:
        print('Error: Uno de los ingresos no fue un número válido')
        error = True
    
    if error == False:
      comprobado = True    
    
  for numero in ingreso:
    numero = int(numero)
    lista.append(numero)

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

# Ejercicio N° 5

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

# Ejercicio N° 6

# Escribe una función que tome una lista de 12 números ordenados de forma ascendente y un valor objetivo, y realice una búsqueda binaria para determinar si el valor objetivo está presente en la lista.

# La función debe devolver True si el valor objetivo se encuentra en la lista y False en caso contrario.
# %%

lista = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132]

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

# - - - - - - - - - - - - - - - - - - 

# Ejercicio N° 7

# Escribe un programa que solicite al usuario ingresar una lista de números separados por espacios. Luego, pide al usuario que ingrese un número específico y utiliza el método index() para encontrar el índice de la primera
# aparición de ese número en la lista. Muestra el índice encontrado al usuario.
# %%

def busqueda_indice():
  comprobado = False
  
  lista = []

  while comprobado == False:
    ingreso = input('Ingresa una serie de 10 números separados por espacios').split()

    error = False

    for numero in ingreso:
      try:
        numero = int(numero)
      except:
        print('Error: Uno de los ingresos no fue un número válido \n>>>')
        error = True
    
    if error == False:
      comprobado = True    
    
  for numero in ingreso:
    numero = int(numero)
    lista.append(numero)

  numero_objetivo = int(input('Ingrese el número ha ser buscado'))

  try:
    indice = lista.index(numero_objetivo)
    print(f'El número se halla en la posición {indice}')
  except:
    print('El número no se halla en la lista')
    
busqueda_indice(lista, 55)
busqueda_indice(lista, 56)
busqueda_indice(lista, 11)

# - - - - - - - - - - - - - - - - - - 

# Ejercicio N° 8

# Escribe una función que tome una lista de objetos (por ejemplo, objetos de una clase particular) y un valor objetivo, y realice una búsqueda para determinar si algún objeto de la lista tiene una propiedad o atributo específico igual al valor objetivo. La función debe devolver True si se encuentra un objeto con la propiedad deseada y False en caso contrario.
# %%

def busqueda_objetos(numero_objetivo):

  class Nodo:
    def __init__(self, item):
      self.valor = item
    def __repr__(self):
      return str(self.valor)

  lista = list()

  for i in range (1, 10):
    nodo = Nodo(i)
    lista.append(nodo)

  for elemento in lista:
    if elemento.valor == numero_objetivo:
      return True

  return False

print(busqueda_objetos(3))
print(busqueda_objetos(77))
print(busqueda_objetos(7))

# %%
