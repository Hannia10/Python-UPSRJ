
def _crear_product(name,department,cost):
    persona = {
        'name' : name,
        'department' : department,
        'cost' : cost
    }
    return product

if __name__ == "__main__":
    cola = Cola.Queue()
    cola.fifo(_crear_product('Milk','Dairy products', 25))
    cola.fifo(_crear_product('Tacos','Mexican food', 50))
    cola.fifo(_crear_product('Pizza','Fast food', 150))
    cola.fifo(_crear_product('Hamburger','Fast food', 80))
    cola.fifo(_crear_product('Soda','Drinks', 20))
    cola.printt()
    print('*' * 25)
    cola.noFifo()
    cola.printt()
