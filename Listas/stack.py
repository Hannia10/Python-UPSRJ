#Una clase es la estructura
class Nodo:

    def __init__(self,dato=None): #Es un contructor, sirve para incializar el objeti INIT 
        self.dato = dato #Hace que la variable se creee en la clase
        self.puntero = None

    def __str__(self): #Para impirmir 
        return self.dato
    
class Stack:

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertar(self,dato):
        nodo = Nodo (dato)
        if self.inicio == None:
            self.fin = nodo
            nodo.puntero = self.inicio
            self.inicio = nodo
            self.size += 1
        else:
            nodo = Nodo (dato)
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
                print(nodoAux.dato)
                nodoAux = nodoAux.puntero
                contador -= 1

if __name__ == "__main__":
    s = Stack()
    s.insertar('Hannia')
    s.insertar('Vianney')
    s.insertar('Santiago')
    s.listar()
    print('*' * 15)
    s.eliminar()
    s.listar()