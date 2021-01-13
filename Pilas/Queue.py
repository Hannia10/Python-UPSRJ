import nodo as Nodo
import copy
class Queue:
    
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.longitud = 0
        self.pilaMayor = None
        self.pilaMenor = None
    
    
    def apilar(self, dato):
        nodo = Nodo.Nodo(dato)
        if self.inicio == None:
            self.fin = nodo
            nodo.puntero = self.inicio
            self.inicio = nodo
        else:
            self.fin.puntero = nodo
            self.fin = nodo
        self.longitud += 1
    
    
    def length(self):
        return self.longitud
    
    
    def estaVacia(self):
        return self.inicio == None
    
    
    def desapilar(self):
        if not self.estaVacia():
            if self.inicio.puntero == None:
                ultimo = self.inicio
                self.inicio = None
                self.fin = None
                self.longitud -=1
                return ultimo.dato
            else:
                puntero = self.inicio
                while puntero.puntero.puntero != None:
                    puntero = puntero.puntero
                ultimo = puntero.puntero
                puntero.puntero = None
                self.fin = puntero
                self.longitud -= 1
                return ultimo.dato
        return None
    
    
    def tope(self):
        if not self.estaVacia():
            return self.fin.dato
    
    
    def imprimir(self):
        if not self.estaVacia():
            puntero = self.inicio
            contador = self.longitud
            while  contador > 0:
                print(puntero.dato)
                puntero = puntero.puntero
                contador -= 1
    
    def _crear_persona(self,persona):
        newPersona = {
            'nombre' : persona.nombre,
            'apellido' : persona.apellido,
            'edad' : persona.edad
        }
        return newPersona
    
    def burbuja(self, mayor = None):
        if self.pilaMayor == None:
            self.pilaMayor = Queue()
        if self.pilaMenor == None:
            self.pilaMenor = Queue()
        if not self.estaVacia():
                if not mayor:
                    mayor = self.desapilar()
                menor = self.desapilar()
                if menor:
                    if mayor.edad > menor.edad:
                        pass
                    else:
                        temp = menor
                        menor = mayor
                        mayor = temp
                    self.pilaMenor.apilar(self._crear_persona(menor))
                self.burbuja(mayor)
        else:
            self.pilaMayor.apilar(self._crear_persona(mayor))
            if not self.pilaMenor.estaVacia():
                while not self.pilaMenor.estaVacia():
                    self.apilar(self._crear_persona(self.pilaMenor.desapilar()))
                self.burbuja()
            else:
                while not self.pilaMayor.estaVacia():
                    self.apilar(self._crear_persona(self.pilaMayor.desapilar()))