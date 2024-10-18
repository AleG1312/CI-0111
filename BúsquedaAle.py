'''
Funcion que busca un elemento en la lista
Debe terminar la implementación del algoritmo busqueda

Se desarrolló el código tomando en cuenta las siguientes indicaciones hechas en clase:
    1. Puede modificar el código a conveniencia e incluso cambiarlo todo.
    2. No hay solo una manera de resolver un problema.
    3. No se evaluará el código por eficiencia o buenas prácticas, sino porque logra resolver el problema.
'''
def busqueda(lista, valor, por_pasos):
    if (por_pasos == True):
        print(f"Estamos analizando la lista: {lista}, en búsqueda del valor: {valor}")

    indice_mitad = (len(lista)-1) // 2
    if lista[indice_mitad] == valor:
        return "True"
    elif len(lista) == 1:
        return "False"
    elif valor <= lista[indice_mitad]:
        return busqueda(lista[:indice_mitad+1], valor, por_pasos)
    elif valor > lista[indice_mitad]:
        return busqueda(lista[indice_mitad+1:], valor, por_pasos)

def main():
    #Creo la lista
    lista = [0, 6, 5, 23, 38, 49, 20, 15]
    #La ordeno en caso de no estar ordenada
    lista.sort()
    #Pregunto por el número a buscar
    numero = int(input("Ingrese el número que desea buscar: "))
    #Pregunto si desea la solución por pasos
    decision = int(input("¿Desea mostrar la solución por pasos? (1: Sí / 2: No)"))
    por_pasos = True if decision == 1 else False
    #Llamo a la función:
    resultado = busqueda(lista, numero, por_pasos)
    #Imprimo el resultado
    print(resultado)
main()