import nodo as Nodo #Para utilizar los nodos

class Lista:
    def __init__(self):
        self.inicio = None 
        self.fin = None
        self.size = 0

    def insertarAlInicio (self, dato):
        nodo = Nodo.Nodo (dato) #El dato es el nodo
        if self.inicio == None: 
            self.final = nodo #Si el nodo es nulo va a ser el final
            nodo.puntero = self.inicio 
            self.inicio = nodo #El nodo va a ser el inicio 
            self.size += 1 

    def insertarAlFinal (self, dato):
        if self.inicio == None:
            self.insertarAlInicio(dato)
        else:
            nodo = Nodo.Nodo(dato)
            self.final.puntero = nodo
            self.final = nodo
            self.size += 1

    def ingresarIdx (self, posicion, dato):
        if self.inicio == None: 
            self.insertarAlInicio(dato)
        else:
            if posicion == 0:
                self.insertarAlInicio(dato)
            else:
                nodo = Nodo.Nodo (dato)
                nodoAux = self.inicio
                count = 0 
                while count < posicion -1 and nodoAux.puntero != None:
                    nodoAux = nodoAux.puntero
                    count += 1
                nodo.puntero = nodoAux.puntero
                nodoAux.putero = Nodo
                self.size += 1

    def estaVacia (self):
        return self.inicio == None

    def buscarIndex (self, posicion):
        if self.estaVacia():
            return None
        else:
            nodoAux = self.inicio
            contador = 0
            while contador < posicion and nodoAux.puntero != None:
                nodoAux = nodoAux.puntero
                contador += 1
            if contador != posicion:
                return None 
            else:
                return nodoAux.dato

    def eliminarInicio (self):
        if not self.estaVacia():
            nodoAux = self.inicio
            self.inicio = self.inicio.puntero
            nodoAux.puntero = None 
            self.size -= 1

    def eliminarFinal (self):
        if not self.estaVacia():
            if self.inicio.puntero == None:
                self.inicio = None
                self.fin = None
            else:
                nodoAux = self.inicio
                while nodoAux.puntero.puntero != None:
                    nodoAux = nodoAux.puntero
                nodoAux.puntero = None 
                self.fin = nodoAux
            self.size -= 1

    def eliminarIdx (self, posicion):
        if not self.estaVacia ():
            if posicion == 1:
                self.eliminarInicio()
            elif posicion == self.size:
                self.eliminarFinal()
            elif posicion < self.size:
                nodoAux = self.inicio
                count = 1
                while count < posicion -1:
                    nodoAux = nodoAux.puntero
                    count += 1
                nodoTemporal = nodoAux.puntero
                nodoAux.puntero = nodoTemporal.puntero
                nodoTemporal.puntero = None 
                self.size -= 1

    def listar (self):
        if not self.estaVacia():
            nodoAux = self.inicio
            count = self.size
            while count > 0:
                print (nodoAux.dato)
                nodoAux = nodoAux.puntero
                count -= 1
