import nodo as Nodo

class Lista:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.longitud = 0
    
    def insertarPrincipio(self, dato):
        nodo = Nodo.Nodo(dato)
        if self.inicio == None:
            self.fin = nodo
        nodo.puntero = self.inicio
        self.inicio = nodo
        self.longitud += 1
    
    
    def insertarFin(self, dato):
        if self.inicio == None:
            self.insertarPrincipio(dato)
        else:
            nodo = Nodo.Nodo(dato)
            self.fin.puntero = nodo
            self.fin = nodo
            print(self.fin.puntero)
            self.longitud += 1
    
    
    def insertarIdx(self, n, dato):
        if self.inicio == None:
            self.insertarPrincipio(dato)
        else:
            if n == 0:
                self.insertarPrincipio(dato)
            else:
                nodo = Nodo.Nodo(dato)
                puntero = self.inicio
                contador = 0
                while contador < n - 1 and puntero.puntero != None:
                    puntero = puntero.puntero
                    contador += 1
                nodo.puntero = puntero.puntero
                puntero.puntero = nodo
                self.longitud += 1
    
    
    def buscarIdx(self, n):
        if self.inicio == None:
            return None
        else:
            puntero = self.inicio
            contador = 0
            while contador < n and puntero.puntero != None:
                puntero = puntero.puntero
                contador += 1
            if contador != n:
                return None
            else:
                return puntero.dato
    
    
    def length(self):
        return self.longitud
    
    
    def estaVacia(self):
        return self.inicio == None
    
    
    def eliminarPrimero(self):
        if self.inicio != None:
            primero = self.inicio
            self.inicio = self.inicio.puntero
            primero.puntero = None
            self.longitud -= 1
    
    
    def eliminarUltimo(self):
        if not self.estaVacia():
            if self.inicio.puntero == None:
                self.inicio = None
                self.fin = None
            else:
                puntero = self.inicio
                while puntero.puntero.puntero != None:
                    puntero = puntero.puntero
                puntero.puntero = None
                self.fin = puntero
            self.longitud -= 1
    
    
    def eliminarIdx(self, n):
        if not self.estaVacia():
            if n == 0:
                self.eliminarPrimero()
            elif n == self.longitud:
                self.eliminarUltimo()
            elif n < self.longitud:
                puntero = self.inicio
                contador = 0
                while contador < n - 1:
                    puntero = puntero.puntero
                    contador += 1
                temp = puntero.puntero
                puntero.puntero = temp.puntero
                temp.puntero = None
                self.longitud -= 1
                
    
    
    def imprimir(self):
        if not self.estaVacia():
            puntero = self.inicio
            contador = self.longitud
            while  contador > 0:
                print(puntero.dato)
                puntero = puntero.puntero
                contador -= 1