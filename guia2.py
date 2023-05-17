# Ejercicio 1

# Ingresar un radio por teclado
# radioIngresado = int(input('Ingresa un radio')) 
#====> yo ingreso un radio. El radio queda declarado asi '55'. Y
#lo devuelve como 55
#  y avisar por consola si es positivo o negativo
# if radioIngresado < 0:
#     print ("el radio es negativo")
# elif radioIngresado > 0:
#     print ("el radio es positivo")
# else:
#     print ("el radio es 0")

# - - - - - - - - - - - - - 

# Ejercicio 2

# Ingresar el radio de un círculo. 

# radioIngresado = float(input())
 
# # Indicar en consola su perímetro y superficie.

# superficie = 3.1415 * radioIngresado ** 2

# perimetro = 3.1415 * (radioIngresado * 2)

# print("Su perímetro es de " + str(perimetro) + " y su superficie es de " + str(superficie)) 

# - - - - - - - - - - - - - 

# Ejercicio 3

# Ingresar un valor por teclado 

# valorIngresado = int(input())

# y avisar por consola si es par o impar

# if valorIngresado == 0:
#   print ("el resultado es 0")
# elif valorIngresado % 2 == 0:
#     print ("el resultado es par")
# else:
#     print ("el resultado es impar")

# - - - - - - - - - - - - -

# Ejercicio 4

# Realizá un programa que permita resolver el siguiente problema: Cuatro personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje). 

# Solicitar la carga por teclado del nombre de cada socio, su capital aportado y a partir de esto calcular e informar lo requerido previamente.

# def programaDeCalculo ():
#     aportePersona1 = float(input("ingresar el aporte de la primer persona"))
#     aportePersona2 = float(input("ingresar el aporte de la segunda persona"))
#     aportePersona3 = float(input("ingresar el aporte de la tercera persona"))
#     aportePersona4 = float(input("ingresar el aporte de la cuarta persona"))

#     suma = aportePersona1 + aportePersona2 + aportePersona3 + aportePersona4    

#     porcentajePersona1 = (suma * aportePersona1) / 100
#     porcentajePersona2 = (suma * aportePersona2) / 100
#     porcentajePersona3 = (suma * aportePersona3) / 100
#     porcentajePersona4 = (suma * aportePersona4) / 100

#     print ("La suma total es de $" + str(suma))
#     print("El porcentaje del primer aporte es de " + str(porcentajePersona1) + "%") 
#     print("El porcentaje del segundo aporte es de " + str(porcentajePersona2) + "%")
#     print("El porcentaje del tercero aporte es de " + str(porcentajePersona3) + "%")
#     print("El porcentaje del cuarto aporte es de " + str(porcentajePersona4) + "%")

# programaDeCalculo()

# - - - - - - - - - - - - -

# Ejercicio 5

# Ingresar 10 valores, indicar para cada uno su paridad, y al final indicar cuántos pares y cuantos impares hubo.

# def paridad():
#   lista = []
#   listaDeParidad = []
#   cantidadPares = 0
#   cantidadImpares = 0

#   for _ in range(10): 
#     print("ingresa un valor")
#     valor = int(input())
#     lista.append(valor)
  
#   for valor in lista:
#     if(valor % 2 == 0):
#       listaDeParidad.append("Par")
#       cantidadPares += 1
#     else:
#       listaDeParidad.append("Impar")
#       cantidadImpares += 1
  
#   print(lista)
#   print(listaDeParidad)
#   print("La cantidad de pares es de " + str(cantidadPares) + " y la cantidad de impares es " + str(cantidadImpares))

# paridad()

# - - - - - - - - - - - - -

# Ejercicio 6

# Generalizar el punto anterior para ingresar N valores, indicar de cada uno su # paridad, y al final indicar cuántos pares y cuantos impares hubo

# def paridadN():
#   lista = []
#   listaDeParidad = []
#   cantidadPares = 0
#   cantidadImpares = 0

#   print("ingresa la cantidad de valores")
#   cantidadValores = int(input())

#   for i in range(cantidadValores): 
#     print("ingresa un valor")
#     valor = int(input())
#     lista.append(valor)
  
#   for valor in lista:
#     if(valor % 2 == 0):
#       listaDeParidad.append("Par")
#       cantidadPares += 1
#     else:
#       listaDeParidad.append("Impar")
#       cantidadImpares += 1
  
#   print(lista)
#   print(listaDeParidad)
#   print("La cantidad de pares es de " + str(cantidadPares) + " y la cantidad de impares es " + str(cantidadImpares))

# paridadN()

# - - - - - - - - - - - - -

# Ejercicio 7

# Ingresar 10 valores por teclado. Indicar cuál fue el mayor y cuál fue el menor

# def minMax():
#   lista = []
#   min = None
#   max = None

#   for i in range(10): 
#     print("ingresa un valor")
#     valor = int(input())
#     lista.append(valor)

#   min = lista[0]
#   max = lista[0]

#   for valor in lista:
#     if (valor > max):
#       max = valor
#     elif (valor < min):
#       min = valor

#   max = str(max)
#   min = str(min) 

#   print("el valor mayor es " + max + " y el valor menor es " + min)

# minMax()

# - - - - - - - - - - - - -

# Ejercicio 8 

# Indicar por teclado cuántos números deben ingresarse, ingresarlos y luego calcular
# la suma y multiplicación de los mismos.

# def sumaYmulti():
    # lista = [] #[1, 2, 3, 4, 5]
    # suma = 0
    # multi = 1

    # print("ingresa una cantidad de valores")
    # cantidadValores = int(input()) 

    # for _ in range(cantidadValores): 
    #     print("ingresa un valor")
    #     valor = int(input())
    #     lista.append(valor)

    # for valor in lista:
    #     suma += valor
    #     multi *= valor

    # suma = str(suma)
    # multi = str(multi)

    # print('La suma total es de ' + suma + " y la multiplicación total es de " + multi)

# sumaYmulti()

# - - - - - - - - - - - - -

# Ejercicio 9

# Ingresar por teclado usuario y contraseña. Debe indicar si el usuario ingresado es
# correcto o no.

# def login():
#     registeredUser = 'Ivan Consorte'
#     registeredPassword = 'Open Sesame'

#     print('Input a username')
#     user = input()
#     print('Input a password')
#     password = input()

#     if(user == registeredUser and password == registeredPassword):
#         print ('Login succesful')
#     elif(user != registeredUser):
#         print ('The user doesn\'t exist')
#     elif(user == registeredUser and password != registeredPassword):
#         print ('Incorrect password')
#     else:
#         print ('Error')

# login()

# - - - - - - - - - - - - -

# Ejercicio 10

# Realizar un programa que solicite números y finalice al ingresar un valor 0. Al
# terminar indicar la sumatoria total.

# def sumaHasta():
#     print('Ingrese un valor')
#     numero = int(input())

#     if (numero == 0):
#         return 0
    
#     return numero + sumaHasta()

# result = sumaHasta()

# print(result)

# - - - - - - - - - - - - -

# Ejercicio 11

# Realizá un programa que permita ingresar el monto mensual de ventas realizadas
# por un comercio durante el año (un ingreso por mes). A su vez ingresar gasto por
# mes. Calcular:
# a) Facturación anual
# b) Ganancia mensual
# c) Ganancia promedio

# def calculoGanancias():
#     ventasMes = []
#     gastosMes = []
#     mesesDelAño = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

#     for i in range(12):
#         print ("Ingrese las ventas de " + mesesDelAño[i])
#         ventas = int(input())
#         ventasMes.append(ventas)
#         print ("Ingrese los gastos de " + mesesDelAño[i])
#         gastos = int(input())
#         gastosMes.append(gastos)

#     facturacionAnual = 0
#     gananciaMensual = []
#     gananciaAnual = 0

#     for i in range (12):
#       facturacionAnual += ventasMes[i]
#       ganancia = ventasMes[i] - gastosMes[i]
#       gananciaMensual.append(ganancia)

#     for ganancia in gananciaMensual:
#       gananciaAnual += ganancia
    
#     gananciaPromedio = gananciaAnual / 12

#     print("")
#     print ("La facturación anual es de " + str(facturacionAnual))
#     print ("")
#     for i in range(12):
#         print ("La ganancia del mes de " + mesesDelAño[i] + " es de " + str(gananciaMensual[i]))
#     print("")
#     print("La ganancia promedio es de " + str(gananciaPromedio))

# calculoGanancias()

# Realizar una calculadora que permita ingresar dos valores y la operación a realizar y
# brinde el resultado en pantalla. El programa no finaliza.

# def calculadora():
#     print("Ingrese el primer valor de la operación")
#     valor1 = int(input())
#     print("")

#     print("Ingrese el segundo valor de la operación")
#     valor2 = int(input())
#     print("")

#     print("Ingrese el tipo de operación")
#     operación = input()
#     print("")

#     resultado = 0

   

#     if(operación == "suma"):
#       resultado = valor1 + valor2
#     elif(operación == "resta"):
#       resultado = valor1 - valor2
#     elif(operación == "multiplicación"):
#       resultado = valor1 * valor2
#     elif(operación == "división"):
#       resultado = valor1 / valor2
#     else:
#       print('operación inválida')
#       return 0

#     print('El resultado de la ' + operación + ' es de ' + str(resultado))

#     calculadora()

# calculadora()




    

  
  





