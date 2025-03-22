import random

def generarTablero(largo):
    tablero = []
    randInt = random.randint(0,10)
    i=0
    while i<11:
        tablero.append([])
        i+=1
    for elemento in tablero:
        j=0
        while j<largo:
            elemento.append("X")
            j+=1

    tablero[5][0] = "S"
    tablero[randInt][largo-1] = "*"

    return tablero

def generarGuardias(tablero, largo, cantidad):
    i=0
    while i<cantidad:
        randFila = random.randint(0,10)
        randColumna = random.randint(0, largo-1)

        while tablero[randFila][randColumna] == "!" or tablero[randFila][randColumna] == "S" or tablero[randFila][randColumna] == "*":
            randFila = random.randint(0,10)
            randColumna = random.randint(0, largo-1)
        
        tablero[randFila][randColumna] = "!"
        i+=1

boardLarge = int(input("Ingresa el largo del tablero: "))
guardias = int(input("Ingresa la cantidad de guardias a generar: "))
board = generarTablero(boardLarge)
generarGuardias(board, boardLarge, guardias)

for elemento in board:
    print(str(elemento)+"\n")