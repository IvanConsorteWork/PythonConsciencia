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

suma(33, 66)

# - - - - - - - - - - - - - - -

# Ejercicio N° 4

# Define una función llamada "saludo_personalizado" que reciba un nombre y un saludo opcionalmente. Si no se proporciona un saludo, debe utilizar "¡Hola" como saludo predeterminado.

# Llama a la función para saludar a diferentes personas con y sin saludo personalizado.

#%%

def saludo_personalizado(nombre, saludo = '¡Hola'):
	print(f"{saludo}, {nombre}!")

saludo_personalizado('Ivan')
saludo_personalizado('Ivan', '¡Cómo estas')