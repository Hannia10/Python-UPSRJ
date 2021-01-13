#Se importa el archivo lista y el programa lo conoce como List
import lista as List 

if __name__ == "__main__":
    lista = List.Lista()
    lista.insertarAlInicio('Hannia')
    lista.insertarAlInicio('Vianney')
    lista.insertarAlFinal('Santiago')
    lista.listar()
    print('*' * 15)
    lista.eliminarFinal()
    lista.listar()