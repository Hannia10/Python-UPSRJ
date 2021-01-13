def _print_welcome():
    print('Welcome to tienda')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[V]enta')
    print('[C]aja')
    print('[Ce]rrar')

def _imprimir_ticket(productos):
    total = 0
    print('#  | Nombre  | Precio  | Cantidad | subTotal')
    for idx, producto in enumerate(productos):
        total += producto['subTotal']
        print('{idx} | {name} | {price} | {quantity} | {subTotal}'.format(
            idx = idx + 1,
            name = producto['nombre'],
            price = producto['precio'],
            quantity = producto['cantidad'],
            subTotal = producto['subTotal']
            ))
    print('Total a pagar {}'.format(total))
    return total

def _get_producto_field(field_name):
    field = None
    while not field:
        field = input('Waht is the product {}? '.format(field_name)).capitalize()
    return field


if __name__ == "__main__":
    condicion = True
    totalCaja = 0
    while condicion:
        _print_welcome()
        command = input()
        command = command.upper()
        if command == 'V':
            productos = []
            respuesta = 'S'
            while respuesta == 'S':
                producto = {
                    'nombre': _get_producto_field('name'),
                    'precio': _get_producto_field('price'),
                    'cantidad': _get_producto_field('quantity'),
                }
                producto['subTotal'] = int(producto['precio']) * int(producto['cantidad'])
                productos.append(producto)
                respuesta = input('Quieres agregar otro producto [S]i y [N]o').upper()
            totalCaja += _imprimir_ticket(productos)
        elif command == 'C':
            print('Total en Caja {}'.format(totalCaja))
        elif command == 'CE':
            condicion = False
        else:
            print('Invalid Command')