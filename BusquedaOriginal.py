'''
Funcion que busca un elemento en la lista
Debe terminar la implementación del algoritmo busqueda
'''


def busqueda(lista, limite_inferior, limite_superior, valor):
    mitad = 0
    if limite_inferior > limite_superior:
        return -1
    else:
        mitad = (limite_inferior + limite_superior) // 2


lista = [0, 6, 5, 23, 38, 49, 20, 15]

resultado = busqueda(lista, 0, len(lista), 23)
print(resultado)
