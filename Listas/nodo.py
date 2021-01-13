#Una clase es la estructura
class Nodo:

    def __init__(self,dato=None): #Es un contructor, sirve para incializar el objeti INIT 
        self.dato = dato #Hace que la variable se creee en la clase
        self.puntero = None

    def __str__(self): #Para impirmir 
        return self.dato
