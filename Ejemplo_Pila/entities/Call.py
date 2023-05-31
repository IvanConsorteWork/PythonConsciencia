from enum import Enum


class LLamada:
    
    def __init__(self,contacto, hora, estadoLLamada):
        self.contacto= contacto
        self.hora = hora
        self.estadoLLamada = estadoLLamada
        
class EstadoLlamada (Enum):
    
    ATENDIDA = 1
    PERDIDA  = 2
    EN_CURSO  = 3
         