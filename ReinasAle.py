'''

Consideraciones:
- Meter la primera reina.
- Meter la segunda en una casilla que no esté atacada por
la primera reina.
- Meter la tercera en una casilla no atacada por la
primera o la segunda.
- Meter sucesivamente el resto de reinas. Si en algún
momento no puede colocarse una reina, ir deshaciendo
movimientos de las reinas ya colocadas y a partir de esa
reorganización continuar la colocación del resto de
reinas.
Funciones auxiliares:

Funciones a implementar:
- asignar_reina(fila, columa) => Sitúa un 1
en la casilla (Fila, Columna) indicando que está
ocupada por una reina.
- eliminar_reina(fila, columna) => Sitúa un
0 en la casilla (Fila, Columna) indicando que esa casilla
está libre (antes estaba ocupada por una reina y ahora
deja de estarlo).
- recibe_jaque(fila, columna) => Devuelve 1
si la casilla (Fila, Columna) recibe jaque de alguna
reina y 0 en caso contrario.
'''

tablero = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]


def recibe_jaque(fila, columna):
    jaque = jaque_fila(fila,columna)
    if (jaque == 0):
        jaque = jaque_columna(fila,columna)
        if (jaque == 0):
            jaque = jaque_diagonal(fila,columna)
    print("Hay jaque: " + str(jaque))
    return jaque
    pass

def jaque_fila(fila,columna):
    jaque = 0
    for j in range(len(tablero[fila])):
        if (j == columna):
            pass
        else:
            if(tablero[fila][j] == 1):
                jaque = 1
                break
    return jaque

def jaque_columna(fila,columna):
    jaque = 0
    for i in range(len(tablero)):
        if (i == fila):
            pass
        else:
            if(tablero[i][columna] == 1):
                jaque = 1
                break
    return jaque

def jaque_diagonal(fila,columna):
    jaque = 0
    menor = min(fila,columna)

    fila_revision = fila - menor
    columna_revision = columna - menor

    while(fila_revision < len(tablero) and columna_revision < len(tablero)):
        if (fila_revision == fila):
            #En caso de estar revisando la casilla de mi reina, ingorarla
            pass
        elif(tablero[fila_revision][columna_revision] == 1):
            jaque = 1
            return jaque
        fila_revision += 1
        columna_revision += 1
    return jaque

def asignar_reina(fila, columna):
    tablero[fila][columna] = 1
    pass


def eliminar_reina(fila, columna):
    tablero[fila][columna] = 0


def colocar_reina(columna):
    fila = 0
    posicion = 0

    if columna > 7:
        posicion = 1
        return posicion
    else:
        posicion = 0
        fila = 1
        while not posicion and (fila <= 7):
            if recibe_jaque(fila, columna):
                ++fila
            else:
                asignar_reina(fila, columna)
                posicion = colocar_reina(columna + 1)
                if not posicion:
                    eliminar_reina(fila, columna)
                    ++fila
    return posicion


def main():
    jaque = 0
    while (jaque != 1):
        #Realizo el primer movimiento
        movimiento = str(input("Ingrese (fila,columna):"))
        #Proceso la entrada
        fila = int(movimiento.split(",")[0])
        columna = int(movimiento.split(",")[1])
        #Lo agrego en el tablero
        asignar_reina(fila,columna)
        #Muestro el tablero en pantalla
        for i in range(len(tablero)):
            print(tablero[i])
        #Verifico  un jaque
        jaque = recibe_jaque(fila,columna)


jaque_diagonal(4,5)
main()
