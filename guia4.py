# Guia n°4 - Pilas

# Ejercicio n°1

# Implementar una pila básica:

# Crear una clase llamada Pila que tenga los métodos apilar, desapilar y esta_vacia. Utiliza una lista para almacenar los elementos de la pila.

# El método apilar debe agregar un elemento al final de la lista.

# El método desapilar debe eliminar y devolver el último elemento de la lista.

# El método esta_vacia debe verificar si la lista está vacía y devolver un valor booleano.
#%%

class Pila:
  def __init__(self):
    self.data = []
  def apilar(self, item):
    self.data.append(item)
  def desapilar(self):
    return None if self.esta_vacia() else self.data.pop()
  def esta_vacia(self):
    return True if len(self.data) == 0 else False

pila = Pila()
print(pila.esta_vacia())
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
pila.apilar(6)
print(pila.data)
pila.desapilar()
print(pila.data)
print(pila.esta_vacia())

# - - - - - - - - - - - - - - - -

# Ejercicio n°2

# Implementar una función llamada verificar_balance que tome una cadena de texto que contiene paréntesis y verifique si están balanceados.

# Utiliza una pila para realizar el seguimiento de los paréntesis abiertos.

# Recorre la cadena de texto y cada vez que encuentres un paréntesis de apertura, apílalo.

# Si encuentras un paréntesis de cierre, verifica si la pila está vacía o si el elemento en la cima de la pila corresponde al paréntesis de apertura correspondiente.

# Al final, la pila debe estar vacía si los paréntesis están balanceados.
#%%

class Pila:
  def __init__(self):
    self.data = []
  def apilar(self, item):
    self.data.append(item)
  def desapilar(self):
    return None if self.esta_vacia() else self.data.pop()
  def esta_vacia(self):
    return True if len(self.data) == 0 else False

def verificar_balance(texto):
  pila = Pila()
  for caracter in texto:
    if caracter == '(':
      pila.apilar(caracter)
    elif caracter == ')':
      pila.desapilar()
  return pila.esta_vacia()
#%%

# - - - - - - - - - - - - - - - -

# Ejercicio n°3

# Implementa una función llamada es_palindromo que tome una palabra como entrada y verifique si es un palíndromo.

# Utiliza una pila para almacenar las letras de la palabra.

# Recorre la palabra y apila cada letra.

# Luego, desapila las letras y compáralas con las letras originales de la palabra.

# Si todas las letras coinciden, la palabra es un palíndromo  
# %%
class Pila:
  def __init__(self):
    self.data = []
  def apilar(self, item):
    self.data.append(item)
  def desapilar(self):
    return None if self.esta_vacia() else self.data.pop()
  def esta_vacia(self):
    return True if len(self.data) == 0 else False

def es_palindromo(palabra):
  pila = Pila()
  veredicto = True
  for letra in palabra:
    pila.apilar(letra)
  for letra in palabra:
    palindromo = pila.desapilar()
    if letra != palindromo:
      veredicto = False
  return veredicto

# - - - - - - - - - - - - - - - -

# Ejercicio n°4

# Implementa una función llamada revertir_pila que tome una pila como entrada y la revierta.

# Utiliza una pila auxiliar para almacenar temporalmente los elementos de la pila original.

# Desapila los elementos de la pila original y apílalos en la pila auxiliar. 

# Luego, desapila los elementos de la pila auxiliar y apílalos en la pila original.

# Al finalizar, la pila original contendrá los elementos en orden inverso. 
# %%

class Pila:
  def __init__(self):
    self.data = []
  def apilar(self, item):
    self.data.append(item)
  def desapilar(self):
    return None if self.esta_vacia() else self.data.pop()
  def esta_vacia(self):
    return True if len(self.data) == 0 else False

def revertir_pila(pila):
  pila_revertida = Pila()
  for elemento in range(len(pila.data)):
    aux = pila.desapilar()
    pila_revertida.apilar(aux)
  return pila_revertida

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
pila_revertida = revertir_pila(pila)
print(pila_revertida.data)

# %%
