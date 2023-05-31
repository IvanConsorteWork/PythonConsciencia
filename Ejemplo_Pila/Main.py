
import time
from entities.Stack import *
from entities.Call import *


def verRegistro():
    for llamada in registroDeLlamadas.stack:
        print(f"{llamada.contacto} {time.asctime(llamada.hora)} {llamada.estadoLLamada}")

def borrarLlamada():
    registroDeLlamadas.pop()
    
# localtime = time.localtime(time.time())
# print ("Local current time :", time.asctime(localtime))

registroDeLlamadas = Stack()

registroDeLlamadas.push()
time.sleep(1)
registroDeLlamadas.push(LLamada("Sebi",time.localtime(time.time()),EstadoLlamada.ATENDIDA))
time.sleep(1)
registroDeLlamadas.push(LLamada("Ale",time.localtime(time.time()),EstadoLlamada.PERDIDA))
time.sleep(1)
registroDeLlamadas.push(LLamada("Nico",time.localtime(time.time()),EstadoLlamada.PERDIDA))
time.sleep(1)
registroDeLlamadas.push(LLamada("Laura",time.localtime(time.time()),EstadoLlamada.ATENDIDA))
time.sleep(1)
registroDeLlamadas.push(LLamada("Valentina",time.localtime(time.time()),EstadoLlamada.PERDIDA))
time.sleep(1)
registroDeLlamadas.push(LLamada("Sofia",time.localtime(time.time()),EstadoLlamada.EN_CURSO))

verRegistro()

print("#################################################################")
borrarLlamada()



verRegistro()

print("#################################################################")
print("#################################################################")


borrarLlamada()
print("#################################################################")
print("#################################################################")
verRegistro()

#Hacer funcion para visalizar solo las atendidas
#Hacer funcion para visalizar solo las perdidas
#Hacer funcion para borrar atendidas
#Hacer funcion para borrar perdidas


