'''
Funcion que busca un elemento en la lista
Debe terminar la implementación del algoritmo busqueda
'''
# def busqueda(lista, limite_inferior, limite_superior, valor):    
#     mitad = 0
#     if limite_inferior > limite_superior:
#         return -1
#     else:
#         mitad = (limite_inferior + limite_superior) // 2

# lista = [0, 6, 5, 23, 38, 49, 20, 15]

# resultado = busqueda(lista, 0, len(lista), 23)
# print(resultado)

def busqueda(lista, limite_inferior, limite_superior, valor):
    print("\n--------------------------------------------------")
    print(lista)
    mitad = (limite_inferior + limite_superior) // 2
    print(f"Estamos comparando el valor {valor} con el de la lista: {lista[mitad-1]}")
    if lista[mitad-1] == valor:
        return "True"
    elif len(lista) == 1:
        return "False"
    elif valor <= lista[mitad-1]:
        return busqueda(lista[:mitad], 0, mitad, valor)
    elif valor > lista[mitad-1]:
        return busqueda(lista[mitad:],mitad, len(lista), valor)


lista = [0, 6, 5, 23, 38, 49, 20, 15]

resultado = busqueda(lista, 0, len(lista), 1)
print(resultado)