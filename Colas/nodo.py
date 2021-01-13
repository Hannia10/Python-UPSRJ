class Product:
    def __init__(self, product):
        self.name = product['name']
        self.cost = product['cost']
        self.department = int(product['department'])
    
    def __str__(self):
        return '{} {} costs {} pesos'.format(self.name, self.department, self.cost)

class Nodo:
    def __init__(self, data = None):
        self.data = Product(data)
        self.nextt = None
    
    def __str__(self):
        return '{}'.format(self.data)