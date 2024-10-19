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

#Función para visualizar el tablero
def mostrarTablero(tablero):
    for i in tablero:
        print(i)

#Dada una casilla,revisa si hay un jaque en esa fila.
def jaque_fila(fila,columna,tablero):
    jaque = 0
    for j in range(len(tablero[fila])):
        if (j != columna):      #Para no revisar la casilla de mi reina
            if(tablero[fila][j] == 1):
                jaque = 1
                break
    return jaque

#Dada una casilla,revisa si hay un jaque en esa columna.
def jaque_columna(fila,columna,tablero):
    jaque = 0
    for i in range(len(tablero)):
        if (i != fila):     #Para no revisar la casilla de mi reina
            if(tablero[i][columna] == 1):
                jaque = 1
                break
    return jaque

#Me ubica el elemento inicial para empezar la revisión de la diagonal descendente que pasa por la casilla inicial.
def casilla_inicial_diagonal_descendente(fila, columna):
    if (fila > 0 and columna > 0):
        return casilla_inicial_diagonal_descendente(fila-1, columna-1)
    else:
        return fila, columna
    
#Dada una casilla, revisa si hay un jaque en la diagonal descendente que pasa por la casilla.
def jaque_diagonal_descendente(fila, columna, tablero):
    jaque = 0
    #Establezco la casilla inicial para mi revision
    fila_revision , columna_revision = casilla_inicial_diagonal_descendente(fila,columna)
    #Hago la revisión
    while(fila_revision < len(tablero) and columna_revision < len(tablero)):
        if (fila_revision != fila):  #Para no revisar la casilla de mi reina
            if(tablero[fila_revision][columna_revision] == 1):
                jaque = 1
                return jaque
        fila_revision += 1
        columna_revision += 1
    return jaque

#Me ubica el elemento inicial para empezar la revisión de la diagonal ascendente que pasa por la casilla inicial.
def casilla_inicial_diagonal_ascendente(fila, columna, tablero):
    if (fila < len(tablero)-1 and columna > 0):
        return casilla_inicial_diagonal_ascendente(fila+1, columna-1, tablero)
    else:
        return fila, columna
    
#Dada una casilla, revisa si hay un jaque en la diagonal descendente que pasa por la casilla.
def jaque_diagonal_ascendente(fila,columna,tablero):
    jaque = 0
    #Establezco la casilla inicial para mi revisión
    fila_revision , columna_revision = casilla_inicial_diagonal_ascendente(fila,columna, tablero)
    #Hago la revisión
    while(fila_revision >= 0 and columna_revision < len(tablero)):
        if (fila_revision != fila):  #Para no revisar la casilla de mi reina
            if(tablero[fila_revision][columna_revision] == 1):
                jaque = 1
                return jaque
        fila_revision -= 1
        columna_revision += 1
    return jaque

#Dada una casila, revisa si hay un jaque
def recibe_jaque(fila, columna, tablero):
    jaque = 0
    # Crear lista de funciones sin ejecutarlas, usando referencias
    jaques = [
            lambda: jaque_fila(fila,columna,tablero),
            lambda: jaque_columna(fila,columna,tablero),
            lambda: jaque_diagonal_descendente(fila,columna,tablero),
            lambda: jaque_diagonal_ascendente(fila,columna,tablero)
            ]
    for function in jaques:
        if (function() == 1):
            jaque = 1
            return jaque
    return jaque

def asignar_reina(fila, columna, tablero):
    tablero[fila][columna] = 1

def eliminar_reina(fila, columna, tablero):
    tablero[fila][columna] = 0

def colocar_reina(columna,tablero):
    fila = 0
    posicion = 0

    if columna > 7:
        posicion = 1
        return posicion
    else:
        while (fila <= 7):
            if recibe_jaque(fila, columna, tablero):
                fila += 1
            else:
                asignar_reina(fila, columna, tablero)
                posicion = colocar_reina(columna + 1, tablero)
                if not posicion:
                    eliminar_reina(fila, columna, tablero)
                fila += 1
    return posicion

def pruebas_metodos():
    tablero =  [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    jaque = 0
    while (jaque != 1):
        #Realizo el primer movimiento
        movimiento = str(input("Ingrese el par ordenado de (fila, columna) para establecer la casilla inicial: "))
        #Proceso la entrada
        fila = int(movimiento.split(",")[0])
        columna = int(movimiento.split(",")[1])
        #Lo agrego en el tablero
        asignar_reina(fila,columna,tablero)
        #Muestro el tablero en pantalla
        mostrarTablero(tablero)
        #Verifico  un jaque
        jaque = recibe_jaque(fila,columna,tablero)

def main():
    tablero =  [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
    colocar_reina(0, tablero)
    mostrarTablero(tablero)
#pruebas_metodos()   
main()