#Una clase es la estructura
class Nodo:

    def __init__(self,dato = None):
        self.dato = dato
        self.puntero = None

    def __str__(self):
        return self.dato

class Queue:

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
            nodoAux = self.inicio
            self.inicio = self.inicio.puntero
            nodoAux.puntero = None
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
    q = Queue()
    q.insertar('Hannia')
    q.insertar('Vianney')
    q.insertar('Santiago')
    q.listar()
    print(q.estaVacia())
    print('*' * 15)
    q.eliminar()
    q.listar()
    print('*' * 15)
    q.insertar('Diego')
    q.listar()
    print('*' * 15)
    q.eliminar()
    q.listar()