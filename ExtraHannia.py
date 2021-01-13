clientes = []
cuentas = []
tarjetas = []

def agregarTarjeta(tarjeta):
    global tarjetas 
    if tarjetas:
        if tarjeta not in tarjetas:
            aux = True
            for tarj in tarjetas:
                if tarj['numero'] == tarjeta['numero']:
                    aux = False
                    break
            if aux:
                tarjetas.append(tarjeta)
            else:
                print ('Numero ya existe')
        else:
            print('Tarjeta ya extiste')
    else:
        tarjetas.append(tarjeta)


def agregarCuenta(cuenta):
    global cuentas
    if cuentas:
        if cuentas not in cuentas:
            aux = True
            for cuen in cuentas:
                if cuen['numero'] == cuenta['numero']:
                    aux = False
                    break
            if aux:
                cuentas.append(cuenta)
            else:
                print('Numero ya existe')
        else:
            print('Grupo ya existe')
    else:
        cuentas.append(cuenta)


def agregarCliente(cliente):
    global clientes
    if cliente not in clientes:
        clientes.append(cliente)
    else:
        print('Cuenta ya existe')


def _get_campo(campo, objeto):
    valor = None
    while not valor:
        valor = input('Cual es el {} de {}: '.format(campo, objeto)).lower()
    return valor


def _crear_tarjeta():
    tarjeta = {
        'numero':_get_campo('numero','Tarjeta'),
        'PIN':_get_campo('PIN','Tarjeta'),
        'saldo':int(_get_campo('saldo','Tarjeta'))
    }
    return tarjeta

def eliminarTarjeta(numero):
    global tarjetas
    for tarjeta in tarjetas:
        if tarjeta['numero'] == numero:
            tarjetas.remove(tarjeta)
            return True
    print('La tarjeta no existe en la lista de tarjetas')


def _crear_cuenta():
    cuenta = {
        'numero':_get_campo('numero','Cuenta'),
        'tarjetas':[],
        'clientes':[]
    }
    return cuenta

def eliminarCuenta(numero):
    global cuentas
    for cuenta in cuentas:
        if cuenta['numero'] == numero:
            cuentas.remove(cuenta)



def _crear_cliente():
    cliente = {
        'nombre':_get_campo('nombre','Cliente'),
        'numero':_get_campo('numero','Cliente')
    }
    return cliente

def eliminarCliente(clave):
    global clientes
    for cliente in clientes:
        if cliente['numero'] == cliente:
            clientes.remove(cliente)


def agregar_Tarjeta_A_Cuenta(tarjeta,cuenta):
    if tarjeta not in cuenta ['tarjetas']:
        cuenta['tarjetas'].append(tarjeta)
    else:
        print('La tarjeta {} ya esta en la cuenta '.format(tarjeta['numero']))

def agregar_cliente_a_cuenta(cliente,cuenta):
    if cliente not in cuenta ['clientes']:
        cuenta['clientes'].append(cliente)
    else:
        print('El cliente {} ya esta en la cuenta '.format(cliente['numero']))


def mod_numero_Cliente(numeroCliente):
    global clientes
    for cliente in clientes:
        if cliente['numero'] == numeroCliente:
            return cliente
    return None


def modificarCliente():
    global clientes
    clienteNumero = input ('Numero de cliente: ').lower()
    cliente = mod_numero_Cliente(clienteNumero)
    if cliente:
        print('¿Que quiere modificar?')
        print('[1] Nombre')
        print('[2] Numero')
        print('[3] Todo')
        campoModificar = input().lower()
        if campoModificar == '1':
            cliente['nombre'] = _get_campo('nombre', 'Cliente')
        elif campoModificar == '2':
            cliente['numero'] = _get_campo('numero', 'Cliente')
        elif campoModificar == '3':
            cliente['nombre'] = _get_campo('nombre', 'Cliente')
            cliente['numero'] = _get_campo('numero', 'Cliente')
        else:
            print('Opcion invalida')
    else:
        print('Cliente no existe')


def mod_numero_tarjeta(numeroTarjeta):
    global tarjetas 
    for tarjeta in tarjetas:
        if tarjeta['numero'] == numeroTarjeta:
            return tarjeta
    return None


def modificarTarjeta():
    global tarjetas
    tarjetaNumero = input ('Numero de tarjeta: ').lower()
    tarjeta = mod_numero_tarjeta(tarjetaNumero)
    if tarjeta:
        print('¿Que quiere modificar?')
        print('[1] Numero')
        print('[2] PIN')
        print('[3] Saldo')
        print('[4] Todo')
        campoModificar = input().lower()
        if campoModificar == '1':
            tarjeta['numero'] = _get_campo('numero', 'Cliente')
        elif campoModificar == '2':
            tarjeta['PIN'] = _get_campo('PIN', 'Cliente')
        elif campoModificar == '3':
            tarjeta['saldo'] = _get_campo('saldo', 'Cliente')
        elif campoModificar == '4':
            tarjeta['numero'] = _get_campo('numero', 'Cliente')
            tarjeta['PIN'] = _get_campo('PIN', 'Cliente')
            tarjeta['saldo'] = _get_campo('saldo', 'Cliente')
        else:
            print('Opcion invalida')
    else:
        print('Tarjeta no existe')


def mod_numero_cuenta(numeroCuenta):
    global cuentas 
    for cuenta in cuentas:
        if cuenta['numero'] == numeroCuenta:
            return cuenta
    return None


def modificarCuenta():
    global cuentas
    cuentaNumero = input ('Numero de cuenta: ').lower()
    cuenta = modificarCuenta(cuentaNumero)
    if cuenta:
        print('¿Que quiere modificar?')
        print('[1] Todo')
        campoModificar = input().lower()
        if campoModificar == '1':
            tarjeta['numero'] = _get_campo('numero', 'Cliente')
        else:
            print('Opcion invalida')
    else:
        print('Cuenta no existe')

def listarClientes():
    global clientes
    print(' Nombre | Clave ')
    for cliente in clientes:
        print (' {nombre} | {clave} '.format(
            nombre = cliente['nombre'],
            clave = cliente['numero']
        ))

def listarCuentas():
    global cuentas
    print(' Numero ')
    for cuenta in cuentas:
        print (' {numero}'.format(
            numero = cuenta['numero']
        ))

def listarTarjetas():
    global tarjetas
    print (' Numero | PIN | Saldo ')
    for tarjeta in tarjetas:
        print (' {numero} | {PIN} | {saldo}'.format(
        numero = tarjeta['numero'],
        PIN = tarjeta['PIN'],
    ))

def obtenerCliente(numero):
    global clientes
    for cliente in clientes:
        if cliente['numero'] == int (numero):
            return cliente
    print('El cliente no existe')
    return None

def obtenerCuenta(numero):
    global cuentas
    for cuenta in cuentas:
        if cuenta['numero'] == numero:
            return cuenta

def obtenerTarjetas(numero):
    global tarjetas
    for tarjeta in tarjetas:
        if tarjeta['numero'] == numero:
            return tarjeta
    return None

def _inicio_sesion():
    numero = input('Ingrese el numero de tarjeta: ')
    pin = input('Ingrese su PIN: ')
    for aux in tarjetas:
        if numero == tarjetas['numero']:
            if pin == tarjetas['PIN']:
                print('Bienvenido al Banco UPSRJ')
            else:
                print('PIN invalido')
        else:
            print('Tarjeta invalida')

def depositar():
    global tarjetas
    cantidad = int (input('Cantidad a depositar:$ '))
    numeroT = input ('Numero de tarjeta: ')
    obtenerTarjetas(numeroT)
    antes = tarjeta['saldo']
    tarjeta['saldo'] = antes + cantidad
    print ('saldo: {}'.format(tarjeta['saldo']))

def retirar():
    global tarjetas
    cantidad = int (input('Cantidad a retirar:$ '))
    numeroT = input ('Numero de tarjeta: ')
    obtenerTarjetas(numeroT)
    if tarjeta['saldo'] >= cantidad:
        tarjeta['saldo'] -= cantidad
        print('Tu saldo disponible es de: {}'.format(tarjeta['saldo']) )
    else:
        print('No hay suficiente cash')

def transferencia():
    global tarjetas
    cantidad = int(input('Cantidad a transferir:$ '))
    numeroT1 = input('Numero de tarjeta emisor: ')
    numeroT2 = input('Numero de tarjeta receptor: ')
    obtenerTarjetas(numeroT1)
    if tarjeta['saldo'] >= cantidad:
        tarjeta['saldo'] -= cantidad
        print('Tu saldo disponible es de: {}'.format(tarjeta['saldo']) )
        if numeroT2 == tarjeta['numero']:
            obtenerTarjetas(numeroT2)
            antes = tarjeta['saldo']
            tarjeta['saldo'] = antes + cantidad
            print ('Operacion Exitosa')
        else:
            print('Operacion no exitosa')
    else:
        print('No hay suficiente cash')

def consultaSaldo():
    global tarjetas
    numeroT = input('Numero de tarjeta: ')
    obtenerTarjetas(numeroT)
    print('saldo: {}'.format(tarjeta['saldo']))

def ultimosMovimientos(movimiento):
    pass

def _welcome_():
    print('Banco UPSRJ')
    print('[1] Iniciar sesion')
    print('[2] Registarse')
    print('[3] Salir')

def _welcome1_():
    print('*' * 50)
    print('Banco UPSRJ')
    print('[1] Cliente')
    print('[2] Tarjeta')
    print('[3] Cuenta')
    print('[4] Transacciones')
    print('[5] Salir')


def _transacciones_():
    print('TRANSACCIONES\n¿Que desea hacer?')
    print('*'*50)
    print('[1] Retiro')
    print('[2] Deposito')
    print('[3] Transferencia')
    print('[4] Movimientos')
    print('[5] Consulta de saldo')
    print('[6] Salir')

def _cuentas_():
    print('CUENTAS\n¿Que desea hacer?')
    print('*'*50)
    print('[1] Crear cuenta')
    print('[2] Eliminar cuenta')
    print('[3] Modificar cuenta')
    print('[4] Agregar cliente a cuenta')
    print('[5] Agregar tarjeta a cuenta')
    print('[6] Listar cuentas')
    print('[7] Salir')

def _tarjetas_():
    print('TARJETAS\n¿Que desea hacer?')
    print('*'*50)
    print('[1] Crear tarjeta')
    print('[2] Eliminar tarjeta')
    print('[3] Modificar tarjeta')
    print('[4] Listar tarjetas')
    print('[5] Salir')

def _clientes_():
    print('CLIENTES\n¿Que desea hacer?')
    print('*'*50)
    print('[1] Crear cliente')
    print('[2] Eliminar cliente')
    print('[3] Modificar cliente')
    print('[4] Listar clientes')
    print('[5] Salir')

if __name__ == "__main__":
    while True:
        _welcome_()
        command = input()
        if command == '1':
            _inicio_sesion()
        elif command == '2':
            while True:
                _welcome1_()
                opcion = input()
                if opcion == '1':
                    while True:
                        _clientes_()
                        opcionCliente = input()
                        if opcionCliente == '1':
                            cliente = _crear_cliente()
                            agregarCliente(cliente)
                        elif opcionCliente == '2':
                            numero = input ('Numero de cliente: '.lower())
                            eliminarCliente(numero)
                        elif opcionCliente == '3':
                            modificarCliente()
                        elif opcionCliente == '4':
                            listarClientes()
                        elif opcionCliente == '5':
                            break
                        else:
                            print ('Comando Invalido')
                elif opcion == '2':
                    while True:
                        _tarjetas_()
                        opcionTarjetas = input()
                        if opcionTarjetas == '1':
                            tarjeta = _crear_tarjeta()
                            agregarTarjeta(tarjeta)
                        elif opcionTarjetas == '2':
                            numero = input ('Numero de tarjeta: '.lower())
                            eliminarTarjeta(numero)
                        elif opcionTarjetas == '3':
                            modificarTarjeta()
                        elif opcionTarjetas == '4':
                            listarTarjetas()
                        elif opcionTarjetas == '5':
                            break
                        else:
                            print ('Comand invalido')
                elif opcion == '3':
                    while True:
                        _cuentas_()
                        opcionCuentas = input ()
                        if opcionCuentas == '1':
                            cuenta = _crear_cuenta()
                            agregarCuenta(cuenta)
                        elif opcionCuentas == '2':
                            numero = input ('Numero de cuenta: '.lower())
                            eliminarCuenta(numero)
                        elif opcionCuentas == '3':
                            modificarCuenta()
                        elif opcionCuentas == '4':
                            numeroCl = input ('Numero de cliente: ')
                            cliente = obtenerCliente(numeroCl)
                            if cliente: 
                                numeroC = input ('Numero de Cuenta: ')
                                cuenta = obtenerCuenta(numeroC)
                                if cuenta:
                                    agregar_cliente_a_cuenta(cliente,cuenta)
                                else:
                                    print('El numero de cuenta no existe')
                            else:
                                print ('El numero de cliente no existe')
                        elif opcionCuentas == '5':
                            numeroT = input ('Numero de tarjeta: '.lower())
                            tarjeta = obtenerTarjetas(numeroT)
                            if tarjeta: 
                                numeroC = input ('Numero de cuenta: '.lower())
                                cuenta = obtenerCuenta(numeroC)
                                if cuenta:
                                    agregar_Tarjeta_A_Cuenta(tarjeta,cuenta)
                                else:
                                    print('Numro de cuenta no existe')
                            else:
                                print('Numero de tarjeta no existe')
                        elif opcionCuentas == '6':
                            listarCuentas()
                        elif opcionCuentas == '7':
                            break
                elif opcion == '4':
                    while True:
                        _transacciones_()
                        opcionTrans = input()
                        if opcionTrans == '1':
                            retirar()
                        elif opcionTrans == '2':
                            depositar()
                        elif opcionTrans == '3':
                            transferencia()
                        elif opcionTrans == '4':
                            pass
                        elif opcionTrans == '5':
                            consultaSaldo()
                        elif opcionTrans == '6':
                            break
                        else:
                            print('Comando invalido')
                elif opcion == '5':
                    break
                else:
                    print('Comando invalido')