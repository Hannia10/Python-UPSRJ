class Persona:
    def __init__(self, persona):
        self.nombre = persona['nombre']
        self.apellido = persona['apellido']
        self.edad = int(persona['edad'])
    
    
    def __str__(self):
        return '{} {} tiene {} años'.format(self.nombre, self.apellido, self.edad)



class Nodo:
    def __init__(self, dato = None):
        self.dato = Persona(dato)
        self.puntero = None
    
    def __str__(self):
        return '{}'.format(self.dato)