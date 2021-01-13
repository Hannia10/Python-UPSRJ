class Persona:
    def __init__(self,persona):
        self.nombre = persona ['nombre']
        self.apellido = persona['apellido']
        self.edad = int(persona['edad'])

    def __str__(self):
        return '{} {} tiene {} años'.format(self.nombre, self.apellido, self.edad)



class Nodo:

    def __init__(self, dato = None):
        self.dato = Persona (dato) #Hata aquí el nodo recibe persona
        

    def __str__(self):
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

#    def _crear_persona(nombre,apellido,edad):
#        persona{
#            'nombre':nombre
#            'apellido':apellido
#            'edad':edad
#        }
#        return Persona

if __name__ == "__main__":
    s = Stack()
    s.insertar({'nombre':'Hannia', 'apellido':'Arias','edad': '20'})
    s.insertar({'nombre':'Diego','apellido':'Viesca','edad':'30'})
    s.insertar({'nombre':'Santiago','apellido':'Catañon','edad':'25'})
    s.listar()
    print('*' * 15)
    s.eliminar()
    s.listar()