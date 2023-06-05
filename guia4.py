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

  for caracter in texto:
    if caracter == ')':
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

# - - - - - - - - - - - - - - - -

# Ejercicio n°5

# Implementar una cola básica:

# Crea una clase llamada Cola que tenga los métodos agregar, quitar y esta_vacia.
# La función agregar debe agregar un elemento al final de la cola.
# La función quitar debe quitar y devolver el elemento en el frente de la cola.
# La función esta_vacia debe devolver True si la cola está vacía, y False en caso contrario.
#%%

class Cola:
  def __init__(self):
    self.data = []
  def agregar(self, item):
    self.data.append(item)
  def quitar(self):
    return None if self.esta_vacia() else self.data.pop(0)
  def esta_vacia(self):
    return True if len(self.data) == 0 else False

cola = Cola()
print(cola.esta_vacia())
cola.agregar(1)
cola.agregar(2)
cola.agregar(3)
cola.agregar(4)
cola.agregar(5)
cola.agregar(6)
print(cola.data)
print(cola.quitar())
print(cola.data)
print(cola.esta_vacia())

# - - - - - - - - - - - - - - - -

# Ejercicio n°6

# Implementar un simulador de atención de clientes:

# Crea una clase llamada AtencionClientes que tenga los métodos nuevo_cliente, atender_cliente y esta_vacia.
# La función nuevo_cliente debe agregar un cliente a la cola de atención.
# La función atender_cliente debe quitar y devolver el siguiente cliente en la cola de atención.
# La función esta_vacia debe devolver True si la cola de atención está vacía, y False en caso contrario.
# %%

class AtencionClientes:
  def __init__(self):
    self.data = []
  def nuevo_cliente(self, item):
    self.data.append(item)
  def atender_cliente(self):
    return None if self.esta_vacia() else self.data.pop(0)
  def esta_vacia(self):
    return True if len(self.data) == 0 else False

simulador = AtencionClientes()
print(simulador.esta_vacia())
simulador.nuevo_cliente("Carlos Hernandez")
simulador.nuevo_cliente("Jose Martinez")
simulador.nuevo_cliente("Guadalupe Barrios")
simulador.nuevo_cliente("Juan Ignacio Herrera")
simulador.nuevo_cliente("Federico Guzman")
simulador.nuevo_cliente("Gaston Moreno")
print(simulador.data)
cliente_atendido = simulador.atender_cliente()
print(cliente_atendido)
print(simulador.data)
print(simulador.esta_vacia())
  
# - - - - - - - - - - - - - - - -

# Ejercicio n°7

# Implementar una cola de prioridad:

# Crea una clase llamada ColaPrioridad que tenga los métodos agregar, quitar y esta_vacia.
# La función agregar debe agregar un elemento a la cola de prioridad según su nivel de prioridad (mayor prioridad primero).
# La función quitar debe quitar y devolver el elemento con mayor prioridad de la cola.
# La función esta_vacia debe devolver True si la cola de prioridad está vacía, y False en caso contrario.
# %%

class ColaPrioridad:
  def __init__(self):
    self.data = []
    self.max = 0
  def agregar(self, item):
    if self.esta_vacia():
      self.data.append(item)
      self.max = item
    else:
      for i in range (0, len(self.data)):
        if item > self.max:
          self.data.append(item)
          self.max = item
          break
        elif item < self.data[i]:
          self.data.insert(i, item)
          break
        
  def quitar(self):
    return None if self.esta_vacia() else self.data.pop(0)
  def esta_vacia(self):
    return True if len(self.data) == 0 else False

cola = ColaPrioridad()
print(cola.esta_vacia())
cola.agregar(12)
cola.agregar(32)
cola.agregar(3)
cola.agregar(74)
cola.agregar(15)
cola.agregar(26)
print(cola.data)
print(cola.quitar())
print(cola.data)
print(cola.esta_vacia())

# - - - - - - - - - - - - - - - -

# Ejercicio n°8

# Implementar una cola de reproducción de música:

# Crea una clase llamada ColaReproduccion que tenga los métodos agregar_cancion, reproducir_siguiente y mostrar_canciones_pendientes.
# La función agregar_cancion debe agregar una canción a la cola de reproducción.
# La función reproducir_siguiente debe quitar y reproducir la siguiente canción de la cola de reproducción.
# La función mostrar_canciones_pendientes debe mostrar todas las canciones pendientes en orden sin modificar la cola.
# %%

class ColaReproduccion:
  def __init__(self):
    self.data = []
  def agregar_canción(self, item):
    self.data.append(item)
  def reproducir_siguiente(self):
    return None if len(self.data) == 0 else self.data.pop(0)
  def mostrar_canciones_pendientes(self):
    return None if len(self.data) == 0 else self.data

cola = ColaReproduccion()
print(cola.mostrar_canciones_pendientes())
cola.agregar_canción('Blue Moon - Dizzy Gillespie')
print(cola.mostrar_canciones_pendientes())
cola.agregar_canción('Out of Nowhere - Charlie Parker')
cola.agregar_canción('Wow - Lennie Tristano')
print(cola.mostrar_canciones_pendientes())
print(cola.reproducir_siguiente())
print(cola.mostrar_canciones_pendientes())

# - - - - - - - - - - - - - - - -

# Ejercicio n°9

# Implementar un sistema de impresión en cola:

# Crea una clase llamada Impresora que tenga los métodos agregar_documento, imprimir_documento y mostrar_documentos_pendientes.
# La función agregar_documento debe agregar un documento a la cola de impresión.
# La función imprimir_documento debe quitar y mostrar el siguiente documento de la cola de impresión.
# La función mostrar_documentos_pendientes debe mostrar todos los documentos pendientes en orden sin modificar la cola
# %%

class Impresora:
  def __init__(self):
    self.data = []
  def agregar_documento(self, item):
    self.data.append(item)
  def imprimir_documento(self):
    return None if len(self.data) == 0 else self.data.pop(0)
  def mostrar_documentos_pendientes(self):
    return None if len(self.data) == 0 else self.data

cola = Impresora()
print(cola.mostrar_documentos_pendientes())
cola.agregar_documento('Ensayo.txt')
cola.agregar_documento('Resumen.text')
cola.agregar_documento('Apuntes.txt')
print(cola.mostrar_documentos_pendientes())
print(cola.imprimir_documento())
print(cola.mostrar_documentos_pendientes())

# %%
