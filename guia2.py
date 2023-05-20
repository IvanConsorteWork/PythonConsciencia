# Ejercicio 1

# Ingresar un valor por teclado y avisar por consola si es positivo o negativo

#%%

valor_ingresado = int(input('Ingresa un valor \n>>> ')) 
if valor_ingresado == 0:
    print ("el radio es 0")
elif valor_ingresado < 0:
    print ("el radio es negativo")
elif valor_ingresado > 0:
    print ("el radio es positivo")
else:
    print ("error")

# - - - - - - - - - - - - - 

# Ejercicio 2

# Ingresar el radio de un círculo. Indicar en consola su perímetro y superficie.

#%%

radio_ingresado = float(input('Ingrese el radio de un círculo \n>>> '))

superficie = 3.1415 * radio_ingresado ** 2

perimetro = 3.1415 * (radio_ingresado * 2)

print("Su perímetro es de " + str(perimetro) + " y su superficie es de " + str(superficie)) 

# - - - - - - - - - - - - - 

# Ejercicio 3

# Ingresar un valor por teclado y avisar por consola si es par o impar

#%%

valorIngresado = int(input())

if valorIngresado == 0:
  print ("el resultado es 0")
elif valorIngresado % 2 == 0:
    print ("el resultado es par")
elif valorIngresado % 2 == 1:
    print ("el resultado es impar")
else:
    print("error")

# - - - - - - - - - - - - -

# Ejercicio 4

# Realizá un programa que permita resolver el siguiente problema: Cuatro personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje). 

# Solicitar la carga por teclado del nombre de cada socio, su capital aportado y a partir de esto calcular e informar lo requerido previamente.

#%%

nombre_persona1 = input('ingresar el nombre del primer contribuyente \n>>> ')
aporte_persona1 = float(input("ingresar el aporte del contribuyente \n>>> "))
nombre_persona2 = input('ingresar el nombre del segundo contribuyente \n>>> ')
aporte_persona2 = float(input("ingresar el aporte del contribuyente \n>>> "))
nombre_persona3 = input('ingresar el nombre del tercer contribuyente \n>>> ')
aporte_persona3 = float(input("ingresar el aporte del contribuyente \n>>> "))
nombre_persona4 = input('ingresar el nombre del cuatro contribuyente \n>>> ')
aporte_persona4 = float(input("ingresar el aporte del contribuyente \n>>> "))

suma = aporte_persona1 + aporte_persona2 + aporte_persona3 + aporte_persona4    

porcentaje_persona1 = str((aporte_persona1 * 100) / suma)
porcentaje_persona2 = str((aporte_persona2 * 100) / suma)
porcentaje_persona3 = str((aporte_persona3 * 100) / suma)
porcentaje_persona4 = str((aporte_persona4 * 100) / suma)

print ("La suma total es de $" + str(suma))
print(f"El porcentaje que contribuyó {nombre_persona1} es del {porcentaje_persona1}%")
print(f"El porcentaje que contribuyó {nombre_persona2} es del {porcentaje_persona2}%")
print(f"El porcentaje que contribuyó {nombre_persona3} es del {porcentaje_persona3}%")
print(f"El porcentaje que contribuyó {nombre_persona4} es del {porcentaje_persona4}%")

# - - - - - - - - - - - - -

# Ejercicio 5

# Ingresar 10 valores, indicar para cada uno su paridad, y al final indicar cuántos pares y cuantos impares hubo.

#%%

numeros_pares = 0
numeros_impares = 0

for i in range(10, 0, -1):
  numero = int(input(f'Ingrese un valor (Le quedan por ingresar {str(i)} valores \n>>> '))
  if numero % 2 == 0:
    numeros_pares += 1
  elif numero % 2 == 1:
    numeros_impares += 1
  else: 
    print('Ingreso inválido, vuelva a intentarlo')
    i += 1

print(f"Se ingreso un total de {numeros_pares} números pares y {numeros_impares} números impares")

# - - - - - - - - - - - - -

# Ejercicio 6

# Generalizar el punto anterior para ingresar N valores, indicar de cada uno su # paridad, y al final indicar cuántos pares y cuantos impares hubo

#%%

numeros_pares = 0
numeros_impares = 0
numero_veces = int(input('Ingrese la cantidad de números a evaluar \n>>> '))

for i in range(numero_veces, 0, -1):
  numero = int(input(f'Ingrese un valor (Le quedan por ingresar {str(i -1)} valores \n>>> '))
  if numero % 2 == 0:
    numeros_pares += 1
  elif numero % 2 == 1:
    numeros_impares += 1
  else: 
    print('Ingreso inválido, vuelva a intentarlo')
    i += 1

print(f"Se ingreso un total de {numeros_pares} números pares y {numeros_impares} números impares")

# - - - - - - - - - - - - -

# Ejercicio 7

# Ingresar 10 valores por teclado. Indicar cuál fue el mayor y cuál fue el menor

# def minMax():
#   lista = []

valor_inicial = int(input('Ingrese un valor (le quedan 9 ingresos) \n>>> '))
min = valor_inicial
max = valor_inicial

for i in range (9, 0, -1):
  nuevo_valor = int(input(f'Ingrese un valor (le quedan {i -1} ingresos) \n>>> '))
  if nuevo_valor < min:
    min = nuevo_valor
  elif nuevo_valor > max:
    max = nuevo_valor

print(f'El valor mínimo ingresado es de {min} y el valor máximo es de {max}')


# - - - - - - - - - - - - -

# Ejercicio 8 

# Indicar por teclado cuántos números deben ingresarse, ingresarlos y luego calcular
# la suma y multiplicación de los mismos.

#%%

numero_ingresos = int(input('Indique la cantidad de valores a ingresar \n>>> '))
primer_ingreso = int(input('Ingrese el valor inicial'))
suma = primer_ingreso
multi = primer_ingreso

for i in range(numero_ingresos - 1, 0, -1):
  nuevo_ingreso = int(input(f'Ingrese otro valor (le quedan {i -1} ingresos \n>>> '))
  suma += nuevo_ingreso
  multi *= nuevo_ingreso

print(f'La suma total es de {suma} y la multiplicación total es de {multi}')


# - - - - - - - - - - - - -

# Ejercicio 9

# Ingresar por teclado usuario y contraseña. Debe indicar si el usuario ingresado es
# correcto o no.

#%%

registeredUser = 'Ivan Consorte'
registeredPassword = 'Open Sesame'

user = input('Input a username \n>>> ')
password = input('Input a password\n>>> ')

if(user == registeredUser and password == registeredPassword):
    print ('Login succesful')
elif(user != registeredUser):
    print ('The user doesn\'t exist')
elif(user == registeredUser and password != registeredPassword):
    print ('Incorrect password')
else:
    print ('Error')

# - - - - - - - - - - - - -

# Ejercicio 10

# Realizar un programa que solicite números y finalice al ingresar un valor 0. Al
# terminar indicar la sumatoria total.

#%%

valor = 1
suma = 0
while valor != 0:
  valor = int(input('Ingrese un valor (este proceso finalizará cuando ingrese 0) \n>>> '))
  suma += valor

print(f'La suma total es de {suma}')

# - - - - - - - - - - - - -

# Ejercicio 11

# Realizá un programa que permita ingresar el monto mensual de ventas realizadas
# por un comercio durante el año (un ingreso por mes). A su vez ingresar gasto por
# mes. Calcular:
# a) Facturación anual
# b) Ganancia mensual
# c) Ganancia promedio

#%%

ventas_enero = int(input('Ingrese el monto de ventas correspondiente a Enero \n>>> '))
gastos_enero = int(input('Ingrese el gasto correspondiente a Enero \n>>> '))

ventas_febrero = int(input('Ingrese el monto de ventas correspondiente a Febrero \n>>> '))
gastos_febrero = int(input('Ingrese el gasto correspondiente a Febrero \n>>> '))

ventas_marzo = int(input('Ingrese el monto de ventas correspondiente a Marzo \n>>> '))
gastos_marzo = int(input('Ingrese el gasto correspondiente a Marzo \n>>> '))

ventas_abril = int(input('Ingrese el monto de ventas correspondiente a Abril \n>>> '))
gastos_abril = int(input('Ingrese el gasto correspondiente a Abril \n>>> '))

ventas_mayo = int(input('Ingrese el monto de ventas correspondiente a Mayo \n>>> '))
gastos_mayo = int(input('Ingrese el gasto correspondiente a Mayo \n>>> '))

ventas_junio = int(input('Ingrese el monto de ventas correspondiente a Junio \n>>> '))
gastos_junio = int(input('Ingrese el gasto correspondiente a Junio \n>>> '))

ventas_julio = int(input('Ingrese el monto de ventas correspondiente a Julio \n>>> '))
gastos_julio = int(input('Ingrese el gasto correspondiente a Julio \n>>> '))

ventas_agosto = int(input('Ingrese el monto de ventas correspondiente a Agosto \n>>> '))
gastos_agosto = int(input('Ingrese el gasto correspondiente a Agosto \n>>> '))

ventas_septiembre = int(input('Ingrese el monto de ventas correspondiente a Septiembre \n>>> '))
gastos_septiembre = int(input('Ingrese el gasto correspondiente a Septiembre \n>>> '))

ventas_octubre = int(input('Ingrese el monto de ventas correspondiente a Octubre \n>>> '))
gastos_octubre = int(input('Ingrese el gasto correspondiente a Octubre \n>>> '))

ventas_noviembre = int(input('Ingrese el monto de ventas correspondiente a Noviembre \n>>> '))
gastos_noviembre = int(input('Ingrese el gasto correspondiente a Noviembre \n>>> '))

ventas_diciembre = int(input('Ingrese el monto de ventas correspondiente a Diciembre \n>>> '))
gastos_diciembre = int(input('Ingrese el gasto correspondiente a Diciembre \n>>> '))

ganancia_total = ventas_enero + ventas_febrero + ventas_marzo

#TENGO QUE TERMINAR ESTO

# - - - - - - - - - - - - -

# Ejercicio 12

# Realizar una calculadora que permita ingresar dos valores y la operación a realizar y brinde el resultado en pantalla. El programa no finaliza.

#%%  

while True:
  operación = input("Ingrese el tipo de operación \n>>> ")
  valor1 = int(input("Ingrese el primer valor de la operación \n>>> "))
  valor2 = int(input("Ingrese el segundo valor de la operación \n>>> "))  
  resultado = 0 
  
  if(operación == "suma"):
    resultado = valor1 + valor2
  elif(operación == "resta"):
    resultado = valor1 - valor2
  elif(operación == "multiplicación"):
    resultado = valor1 * valor2
  elif(operación == "división"):
    resultado = valor1 / valor2
  else:
    print('operación inválida')

  print(f'El resultado de la {operación} es de {resultado}')





    

  
  






# %%
