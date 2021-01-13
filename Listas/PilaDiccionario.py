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
        return '{}'.format(self.dato)


class Stack:

    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0
        self.pilaMayor = None 
        self.pilaMenor = None
    
    def apilar (self,dato):
        nodo = Nodo(dato)
        if self.inicio == None:
            self.fin = nodo
            nodo.puntero = self.inicio
            self.inicio = nodo

        else:
            self.fin.puntero = nodo
            self.fin = nodo
        self.size +=1 

    def size (self):
        return self.size

    def estaVacia(self):
        return self.inicio == None

    def desapilar (self):
        if not self.estaVacia():
            if self.inicio.puntero == None:
                ultimo = self.inicio
                self.inicio =None
                self.fin = None
                self.size -=1
                return ultimo.dato
            else:
                puntero = self.inicio
                while puntero.puntero.puntero != None:
                    puntero = puntero.puntero
                ultimo = puntero.puntero
                puntero.puntero = None 
                self.fin = puntero
                self.size -=1
                return ultimo.dato 
        return None 

        def tope (self): #Sirve para saber quien es el que está hasta arriba
            if not self.estaVacia():
                return self.fin.dato

        def burbuja(self, mayor = None):
            if self.pilaMayor == None:
                self.pilaMayor = Stack()
            if self.pilaMenor == None:
                self.pilaMenor = Stack()
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
                    else:
                        self.pilaMayor.apilar(self._crear_persona(mayor))


if __name__ == "__main__":
    s = Stack()
    s.apilar({'nombre':'Hannia', 'apellido':'Arias','edad': '20'})
    s.apilar({'nombre':'Diego','apellido':'Viesca','edad':'30'})
    s.apilar({'nombre':'Santiago','apellido':'Catañon','edad':'25'})
    print('*' * 15)
