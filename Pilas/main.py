import Stack as Pila

def _crear_persona(nombre,apellido,edad):
    persona = {
        'nombre' : nombre,
        'apellido' : apellido,
        'edad' : edad
    }
    return persona

if __name__ == "__main__":
    pila = Pila.Pila()
    pila.apilar(_crear_persona('Santiago','Castañon', 19))
    pila.apilar(_crear_persona('Rafa','Montes de oca', 2))
    pila.apilar(_crear_persona('Erick','Montes de oca', 3))
    pila.apilar(_crear_persona('Diego','Viesca', 25))
    pila.apilar(_crear_persona('M','J', 2))
    pila.imprimir()
    pila.eliminarEdad(2)
    pila.imprimir()
    print('*' * 25)
    pila.burbuja()
    pila.imprimir()