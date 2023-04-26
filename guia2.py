#Ejercicio 1

#Ingresar un radio por teclado
# radioIngresado = int(input()) #====> yo ingreso un radio. El radio queda declarado asi '55'. Y
# #lo devuelve como 55
# #  y avisar por consola si es positivo o negativo
# if radioIngresado < 0:
#     print ("el radio es negativo")
# elif radioIngresado > 0:
#     print ("el radio es positivo")
# else:
#     print ("el radio es 0")

# - - - - - - - - - - - - - 

# Ejercicio 2

# Ingresar el radio de un círculo. 

# radioIngresado = int(input());
 
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
#     print("ingresar el aporte de la primer persona")
#     aportePersona1 = int(input())
#     print("ingresar el aporte de la segunda persona")
#     aportePersona2 = int(input())
#     print("ingresar el aporte de la tercera persona")
#     aportePersona3 = int(input())
#     print("ingresar el aporte de la cuarta persona")
#     aportePersona4 = int(input())

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

# Ejercicio 5

# Ingresar 10 valores, indicar para cada uno su paridad, y al final indicar cuántos pares y cuantos impares hubo.

# def paridad():
#   lista = []
#   listaDeParidad = []
#   cantidadPares = 0
#   cantidadImpares = 0

#   for i in range(10): 
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
    

  
  





