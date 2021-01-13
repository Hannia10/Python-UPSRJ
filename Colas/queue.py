import copy
class Queue:
    
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0
        self.big = None
        self.small = None
    
    def encolar(self, data):
        nodo = Nodo.Nodo(data)
        if self.start == None:
            self.end = nodo
            nodo.nextt = self.start
            self.start = nodo
        else:
            self.end.nextt = nodo
            self.end = nodo
        self.size += 1
    
    def length(self):
        return self.size
    
    def empty(self):
        return self.start == None
    
    def noFifo(self):
        if not self.empty():
            nodoAux = self.start
            self.start = self.start.nextt
            nodoAux.nextt = None
            self.size -= 1
            return nodoAux.data

    def printt(self):
        if not self.empty():
            nextt = self.start
            count = self.size
            while  count > 0:
                print(nextt.data)
                nextt = nextt.nextt
                count -= 1
    
    def _crear_product(self,product):
        newProduct = {
            'name' : product.name,
            'cost' : product.cost,
            'department' : product.department
        }
        return newProduct