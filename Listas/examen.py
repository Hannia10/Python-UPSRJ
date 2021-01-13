#Una clase es la estructura
class Nodo:

    def __init__(self,nombre=None,apellido=None,edad=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.puntero = None

    def __str__(self): #Para impirmir 
        return self.nombre
        return self.apellido
        return self.edad
    
class Stack:

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertar(self,nombre, apellido, edad):
        nodo = Nodo (nombre, apellido, edad)
        if self.inicio == None:
            self.fin = nodo
            nodo.puntero = self.inicio
            self.inicio = nodo
            self.size += 1
        else:
            nodo = Nodo (nombre, apellido, edad)
            self.fin.puntero = nodo
            self.fin = nodo
            self.size +=1

    def estaVacia(self):
        return self.inicio == None

    def length(self):
        return self.size

    def eliminar(self):
        if not self.estaVacia():
            if self.inicio.puntero != None:
                self.fin = None
            else:
                nodoAux = self.inicio 
                while nodoAux.puntero.puntero != None:
                    nodoAux = nodoAux.puntero
                nodoAux.puntero = None
                self.fin = nodoAux
            self.size -= 1

    def listar(self):
        if not self.estaVacia():
            nodoAux = self.inicio
            contador = self.size
            while contador > 0:
                print(nodoAux.nombre)
                print(nodoAux.apellido)
                print(nodoAux.edad)
                nodoAux = nodoAux.puntero
                contador -= 1

    def burbuja (self):
        pass

if __name__ == "__main__":
    s = Stack()
    s.insertar('Hannia', 'Arias', '20')
    s.insertar('Vianney','Hernandez','40')
    s.insertar('Santiago','Catanon','30')
    s.listar()
    print('*' * 15)
    s.eliminar()
    s.listar()