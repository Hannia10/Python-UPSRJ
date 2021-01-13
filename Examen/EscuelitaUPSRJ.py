import sys

asignaturas = []

def agregar_asignatura(nombre_asig,clave_asig,maximo_alumnos):
    global asignaturas
    if clave_asig not in asignaturas:
        asignaturas.append({'nombre':nombre_asig, 'clave':clave_asig, 'maximo_alumnos':maximo_alumnos})

def eliminar_asignatura(clave_asig):
    global asignaturas
    for i in range(len(asignaturas)):
        if asignaturas[i]['clave'] == clave_asig:
            print(item for item in asignaturas if item['clave']== clave_asig)
            del asignaturas [i]
            break

def serch_asignatura(clave_asig):
    global asignaturas
    for i in range(len(asignaturas)):
        if asignaturas[i]['clave'] == clave_asig:
            print([i for i in asignaturas if i['clave'] == clave_asig][0])
            break
    else:
        print("\Asignatura no existe\n")

def _get_modificar_asignatura(asignatura_update_field,nombre_asig):
    asignatura = serch_asignatura(nombre_asig)
    if asignatura:
        if asignatura_update_field == 'nombre':
            asignatura['nombre'] = _get_modificar_asignatura('nombre')
            return asignatura
        elif asignatura_update_field == 'clave':
            asignatura['clave'] = _get_modificar_asignatura('clave')
            return asignatura
        elif asignatura_update_field == 'maximo_alumnos':
            asignatura['maximo_alumnos'] = _get_modificar_asignatura('maximo_alumnos')
            return asignatura
        elif asignatura_update_field == 'all':
            asignatura['nombre'] = _get_modificar_asignatura('nombre')
            asignatura['clave'] = _get_modificar_asignatura('clave')
            asignatura['maximo_alumnos'] = _get_modificar_asignatura('maximo_alumnos')
            return asignatura

def modificar_asignatura(nombre_asig,clave_asig,nombre_asig_update,clave_asig_update):
    global asignaturas
    for asignatura in asignaturas:
        if nombre_asig in asignatura['nombre']:
            index = asignaturas.index(asignatura)
            asignaturas[index]=asignatura_update
            asignatura_up =asignatura
    if not asignatura_up:
        print ('La asignatura no está en la lista')

def listar_asignatura():
    global asignaturas
    for idx, asignatura in enumerate (asignaturas):
        print('{idx} | {nombre} | {clave} | {maximo_alumnos}'.format(
            idx = idx,
            nombre = asignatura['nombre'],
            clave = asignatura['clave'],
            maximo_alumnos = asignatura ['maximo_alumnos']
        ))

def _print_welcome():
    print ("WELCOME TO UPSRJ")
    print ("*" * 50)
    print ("[1]Asignaturas")
    print ("[2]Alumnos")
    print ("[3]Agregar alumno a asignatura")

def _print_welcome_asignatura():
    print ("[A]gregar asignatura")
    print ("[M]odificar asignatura")
    print ("[E]liminar asignatura")

def _print_welcome_alumnos():
    print ("[A]gregar alumnos")
    print ("[M]odificar alumnos")
    print ("[E]liminar alumnos")

if __name__ == "_main_":
    _print_welcome()
    command = input()

    if command == 1:
        _print_welcome_asignatura()
        command = input()
        command = command.upper()

        if command == 'A':
            nombre_asig = input ('Ingresar el nombre de la asignatura ')
            clave_asig = input ('Ingresar la clave de la asignatura ')
            maximo_alumnos = input ('Ingresar el numero maximo de alumnos ')
            agregar_asignatura(nombre_asig,clave_asig,maximo_alumnos)

            print (asignaturas)
        
        elif command == 'E':
            clave_asig = input ('¿Qué asignatura quieres eliminar?')
            eliminar_asignatura(clave_asig)
            print (asignaturas)

        elif command == 'M':
            pass