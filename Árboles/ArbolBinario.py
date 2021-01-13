class Nodo:
    def __init__(self, nombre=None, edad=None, izq=None, der=None):
        self.nombre = nombre
        self.edad = edad
        self.izq = izq
        self.der = der

    def __str__(self):
        return "%s %s"%(self.nombre, self.edad)

class arbol:
    def __init__(self):
        self.raiz =None

    def agregar(self, elemento):
        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.cedula) >= int(aux.edad):
                    aux = aux.der
                else:
                    aux = aux.izq
            if int(elemento.edad) >= int(padre.edad):
                padre.der = elemento
            else: 
                padre.izq = elemento

    def preorden(self,elemento):
        if elemento != None:
            print (elemento)
            self.preorden(elemento.izq)
            self.preorden(elemento.der)

    def postorden(self,elemento):
        if elemento != None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print (elemento)

    def inorden(self,elemento):
        if elemento != None:
            self.inorden(elemento.izq)
            print(elemento)
            self.inorden(elemento.der)

    def getRaiz(self):
        return self.raiz

    def peso(self, edad):
        pass


if __name__ == "__main__":
    a = arbol()
    menu = True
    while (menu ==True):
        print("---MENU---")
        print("1.Agregar")
        print("2.Preorden")
        print("3.Postorden")
        print("4.Inorden")
        print ("5.Profundidad")
        num = input("Ingrese la opcion: ")
        if num == "1":
            nombre = input("Ingrese nombre: ")
            edad = input("Ingrese edad: ")
            nodo = Nodo(nombre, edad)
            a.agregar(nodo)
        elif num == "2":
            print ("---PREORDEN---")
            a.preorden(a.getRaiz())
        elif num == "3":
            print ("---POSTORDEN---")
            a.postorden(a.getRaiz())
        elif num == "4":
            print ("---INORDEN---")
            a.inorden(a.getRaiz())
        elif num == "5":
            print ("---PROFUNDIDAD---")
        else:
            menu = False
            print ("---BYE---")
        