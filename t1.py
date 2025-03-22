import random, math, re

def generarTablero(largo): # Genera un tablero de 11 filas y 'largo' columnas
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

def generarGuardias(tablero, largo, cantidad): # En base a un tablero y su largo, se generan 'cantidad' guardias en posiciones aleatorias
    i=0
    while i<cantidad:
        randFila = random.randint(0,10)
        randColumna = random.randint(0, largo-1)

        while tablero[randFila][randColumna] == "!" or tablero[randFila][randColumna] == "S" or tablero[randFila][randColumna] == "*":
            randFila = random.randint(0,10)
            randColumna = random.randint(0, largo-1)
        
        tablero[randFila][randColumna] = "!"
        i+=1

def imprimirTablero(seleccion, tablero, largo): # Función encargada de imprimir el tablero, puede ser impreso como listas (más cómodo a la vista pero menos práctico con largos grandes) o como carácteres (menos cómodo a la vista pero más práctico con largos grandes)
    if seleccion == 1:
        for elemento in tablero:
            print(str(elemento)+"\n")
    elif seleccion == 2:
        for elemento in tablero:
            aImprimir = ""
            i=0
            for element in elemento:
                aImprimir += element
                i+=1
                if i == largo:
                    print(aImprimir)
                    i=0
                    break

def binario_decimal(binario): # Convierte a número decimal el número binario 'binario'.
    numeroFinal = 0
    binarioString = str(binario)
    binarioString = binarioString[::-1]
    i=0
    for caracter in binarioString:
        caracter = int(caracter)
        if caracter==2 or caracter==3 or caracter==4 or caracter==5 or caracter==6 or caracter==7 or caracter==8 or caracter==9:
            return("Error: El número ingresado no corresponde a un número binario.")
        numeroFinal += (math.pow(2, i))*caracter
        i+=1
    return numeroFinal

def octal_decimal(octal): # Convierte a número decimal el número octal 'octal'.
    numeroFinal = 0
    octalString = str(octal)
    octalString = octalString[::-1]
    i=0
    for caracter in octalString:
        caracter = int(caracter)
        if caracter==8 or caracter==9:
            return("Error: El número ingresado no corresponde a un número octal.")
        numeroFinal += (math.pow(8, i))*caracter
        i+=1
    return numeroFinal

def hexadecimal_decimal(hexadecimal): # Convierte a número decimal el número hexadecimal 'hexadecimal'.
    if re.fullmatch(r'[0x]*[0-9A-Fa-f]+', hexadecimal) == None:
        return("Error: El número ingresado no corresponde a un número hexadecimal.")
    dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
        }
    numeroFinal = 0
    invertido = hexadecimal[::-1]
    i=0
    for caracter in invertido:
        if caracter == "x":
            break
        numeroFinal += (math.pow(16, i))*dict[caracter]
        i+=1
    return numeroFinal

print("¡SI SEÑORES... VUELTA AL RUEDO :VVV! Esto es:")
print(r"""___  ___     _        _   _____                   _____       _ _     _   __  _____  __  _____   
|  \/  |    | |      | | |  __ \                 /  ___|     | (_)   | | /  ||  _  |/  ||  _  |_ 
| .  . | ___| |_ __ _| | | |  \/ ___  __ _ _ __  \ `--.  ___ | |_  __| | `| || |/' |`| || |/' (_)
| |\/| |/ _ \ __/ _` | | | | __ / _ \/ _` | '__|  `--. \/ _ \| | |/ _` |  | ||  /| | | ||  /| |  
| |  | |  __/ || (_| | | | |_\ \  __/ (_| | |    /\__/ / (_) | | | (_| | _| |\ |_/ /_| |\ |_/ /_ 
\_|  |_/\___|\__\__,_|_|  \____/\___|\__,_|_|    \____/ \___/|_|_|\__,_| \___/\___/ \___/\___/(_)
______ _                          _____             _                                            
| ___ (_)                        /  ___|           | |                                           
| |_/ /_ _ __   __ _ _ __ _   _  \ `--. _ __   __ _| | _____                                     
| ___ \ | '_ \ / _` | '__| | | |  `--. \ '_ \ / _` | |/ / _ \                                    
| |_/ / | | | | (_| | |  | |_| | /\__/ / | | | (_| |   <  __/                                    
\____/|_|_| |_|\__,_|_|   \__, | \____/|_| |_|\__,_|_|\_\___|                                    
                           __/ |                                                                 
                          |___/                                                                  
""")

boardLarge = int(input("Ingresa el largo del tablero: "))
guardias = int(input("Ingresa la cantidad de guardias a generar: "))
boardPrinting = int(input("""Ingresa el modo de impresión del tablero:
    - 1: Tablero como listas (óptimo para largos pequeños).
    - 2: Tablero como caracteres (óptimo para largos grandes).
Selecciona una opción: """))
while boardPrinting != 1 and boardPrinting != 2:
    boardPrinting = int(input("Selección inválida, inténtalo de nuevo (1 o 2): "))
board = generarTablero(boardLarge)
generarGuardias(board, boardLarge, guardias)

imprimirTablero(boardPrinting, board, boardLarge)