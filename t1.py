import random, math, re, sys, time

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

def binario_decimal(binario): # Convierte a número decimal el número binario 'binario'. Se asume que el número llegará como string, pues es input del usuario.
    numeroFinal = 0
    binario = binario[::-1]
    i=0
    for caracter in binario:
        caracter = int(caracter)
        if caracter==2 or caracter==3 or caracter==4 or caracter==5 or caracter==6 or caracter==7 or caracter==8 or caracter==9:
            return("Error: El número ingresado no corresponde a un número binario.")
        numeroFinal += (math.pow(2, i))*caracter
        i+=1
    return int(numeroFinal)

def octal_decimal(octal): # Convierte a número decimal el número octal 'octal'. Se asume que el número llegará como string, pues es input del usuario.
    numeroFinal = 0
    octal = octal[::-1]
    i=0
    for caracter in octal:
        caracter = int(caracter)
        if caracter==8 or caracter==9:
            return("Error: El número ingresado no corresponde a un número octal.")
        numeroFinal += (math.pow(8, i))*caracter
        i+=1
    return int(numeroFinal)

def hexadecimal_decimal(hexadecimal): # Convierte a número decimal el número hexadecimal 'hexadecimal'. Se asume que el número llegará como string, pues es input del usuario.
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
    return int(numeroFinal)

def decimal_binario(decimal): # Convierte a número binario el número decimal 'decimal'. Se debe castear el parámetro a int.
    strResultado = ""
    resultado = decimal//2
    resto = decimal%2
    strResultado += str(resto)
    while resultado != 0:
        resto = resultado%2
        resultado = resultado//2
        strResultado += str(resto)
    strResultado = strResultado[::-1]
    return int(strResultado)

def decimal_octal(decimal): # Convierte a número octal el número decimal 'decimal'. Se debe castear el parámetro a int.
    strResultado = ""
    resultado = decimal//8
    resto = decimal%8
    strResultado += str(resto)
    while resultado != 0:
        resto = resultado%8
        resultado = resultado//8
        strResultado += str(resto)
    strResultado = strResultado[::-1]
    return int(strResultado)

def decimal_hexadecimal(decimal): # Convierte a número hexadecimal el número decimal 'decimal'. Se debe castear el parámetro a int.
    dict = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
        }
    strResultado = ""
    resultado = decimal//16
    resto = decimal%16
    strResultado += str(dict[resto])
    while resultado != 0:
        resto = resultado%16
        resultado = resultado//16
        strResultado += str(dict[resto])
    strResultado = strResultado[::-1]
    return strResultado

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

SnakeX = 0
SnakeY = 5
boardLarge = int(input("Ingresa el largo del tablero: "))
if boardLarge <= 20:
    boardSize = "pequeño"
    formato = "binario"
elif boardLarge <= 100:
    boardSize = "mediano"
    formato = "octal"
else:
    boardSize = "grande"
    formato = "hexadecimal"
guardias = int(input("Ingresa la cantidad de guardias a generar: "))
boardPrinting = int(input("""Ingresa el modo de impresión del tablero:
    - 1: Tablero como listas (óptimo para largos pequeños).
    - 2: Tablero como caracteres (óptimo para largos grandes).
Selecciona una opción: """))
while boardPrinting != 1 and boardPrinting != 2:
    boardPrinting = int(input("Selección inválida, inténtalo nuevamente (1 o 2): "))
board = generarTablero(boardLarge)
generarGuardias(board, boardLarge, guardias)

while True: #Ciclo de juego, termina cuando Snake llega al objetivo
    print()
    if boardSize == "pequeño":
        print("MODO DE JUEGO: PASILLO PEQUEÑO.")
    elif boardSize == "mediano":
        print("MODO DE JUEGO: PASILLO MEDIANO.")
    else:
        print("MODO DE JUEGO: PASILLO GRANDE.")
    imprimirTablero(boardPrinting, board, boardLarge)
    action = input("""Ingresa una acción:
    - w: Moverse hacia arriba.
    - a: Moverse hacia la izquierda.
    - s: Moverse hacia abajo.
    - d: Moverse hacia la derecha.
Selecciona una opción: """)
    action = action.lower()
    while action != "w" and action != "a" and action != "s" and action != "d":
        action = input("Selección inválida, inténtalo nuevamente (w/a/s/d): ")
    if action == "w":
        numsysSteps = input("Ingresa la cantidad de pasos que quieres moverte hacia arriba en formato {}: ".format(formato))
        if formato == "binario":
            steps = binario_decimal(numsysSteps)
        elif formato == "octal":
            steps = octal_decimal(numsysSteps)
        else:
            steps = hexadecimal_decimal(numsysSteps)
        while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
            numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
        board[SnakeY][SnakeX] = "X"
        SnakeY-=steps
        while SnakeY<0:
            SnakeY+=steps
            numsysSteps = input("Error: El número de pasos ingresado sobrepasa los límites del pasillo. Reingresa la cantidad de pasos que quieres moverte hacia arriba en formato {}: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
            while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
                numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
                if formato == "binario":
                    steps = binario_decimal(numsysSteps)
                elif formato == "octal":
                    steps = octal_decimal(numsysSteps)
                else:
                    steps = hexadecimal_decimal(numsysSteps)
            SnakeY-=steps
        if board[SnakeY][SnakeX] == "X":
            board[SnakeY][SnakeX] = "S"
        elif board[SnakeY][SnakeX] == "*":
            break
        else:
            print("-----------------------------------------------------------")
            print("        GAME OVER: FUISTE ATRAPADO POR LOS GUARDIAS        ")
            print("-----------------------------------------------------------")
            exit()
    elif action == "a":
        numsysSteps = input("Ingresa la cantidad de pasos que quieres moverte hacia la izquierda en formato {}: ".format(formato))
        if formato == "binario":
            steps = binario_decimal(numsysSteps)
        elif formato == "octal":
            steps = octal_decimal(numsysSteps)
        else:
            steps = hexadecimal_decimal(numsysSteps)
        while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
            numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
        board[SnakeY][SnakeX] = "X"
        SnakeX-=steps
        while SnakeX<0:
            SnakeX+=steps
            numsysSteps = input("Error: El número de pasos ingresado sobrepasa los límites del pasillo. Reingresa la cantidad de pasos que quieres moverte hacia la izquierda en formato {}: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
            while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
                numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
                if formato == "binario":
                    steps = binario_decimal(numsysSteps)
                elif formato == "octal":
                    steps = octal_decimal(numsysSteps)
                else:
                    steps = hexadecimal_decimal(numsysSteps)
            SnakeX-=steps
        if board[SnakeY][SnakeX] == "X":
            board[SnakeY][SnakeX] = "S"
        elif board[SnakeY][SnakeX] == "*":
            break
        else:
            print("-----------------------------------------------------------")
            print("        GAME OVER: FUISTE ATRAPADO POR LOS GUARDIAS        ")
            print("-----------------------------------------------------------")
            exit()
    elif action == "s":
        numsysSteps = input("Ingresa la cantidad de pasos que quieres moverte hacia abajo en formato {}: ".format(formato))
        if formato == "binario":
            steps = binario_decimal(numsysSteps)
        elif formato == "octal":
            steps = octal_decimal(numsysSteps)
        else:
            steps = hexadecimal_decimal(numsysSteps)
        while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
            numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
        board[SnakeY][SnakeX] = "X"
        SnakeY+=steps
        while SnakeY>10:
            SnakeY-=steps
            numsysSteps = input("Error: El número de pasos ingresado sobrepasa los límites del pasillo. Reingresa la cantidad de pasos que quieres moverte hacia arriba en formato {}: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
            while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
                numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
                if formato == "binario":
                    steps = binario_decimal(numsysSteps)
                elif formato == "octal":
                    steps = octal_decimal(numsysSteps)
                else:
                    steps = hexadecimal_decimal(numsysSteps)
            SnakeY+=steps
        if board[SnakeY][SnakeX] == "X":
            board[SnakeY][SnakeX] = "S"
        elif board[SnakeY][SnakeX] == "*":
            break
        else:
            print("-----------------------------------------------------------")
            print("        GAME OVER: FUISTE ATRAPADO POR LOS GUARDIAS        ")
            print("-----------------------------------------------------------")
            exit()
    elif action == "d":
        numsysSteps = input("Ingresa la cantidad de pasos que quieres moverte hacia la derecha en formato {}: ".format(formato))
        if formato == "binario":
            steps = binario_decimal(numsysSteps)
        elif formato == "octal":
            steps = octal_decimal(numsysSteps)
        else:
            steps = hexadecimal_decimal(numsysSteps)
        while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
            numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
        board[SnakeY][SnakeX] = "X"
        SnakeX+=steps
        while SnakeX>boardLarge-1:
            SnakeX-=steps
            numsysSteps = input("Error: El número de pasos ingresado sobrepasa los límites del pasillo. Reingresa la cantidad de pasos que quieres moverte hacia la derecha en formato {}: ".format(formato))
            if formato == "binario":
                steps = binario_decimal(numsysSteps)
            elif formato == "octal":
                steps = octal_decimal(numsysSteps)
            else:
                steps = hexadecimal_decimal(numsysSteps)
            while steps == "Error: El número ingresado no corresponde a un número {}.".format(formato):
                numsysSteps = input("Error: El número ingresado no corresponde a un número {}... Inténtalo nuevamente: ".format(formato))
                if formato == "binario":
                    steps = binario_decimal(numsysSteps)
                elif formato == "octal":
                    steps = octal_decimal(numsysSteps)
                else:
                    steps = hexadecimal_decimal(numsysSteps)
            SnakeX+=steps
        if board[SnakeY][SnakeX] == "X":
            board[SnakeY][SnakeX] = "S"
        elif board[SnakeY][SnakeX] == "*":
            break
        else:
            print("-----------------------------------------------------------")
            print("        GAME OVER: FUISTE ATRAPADO POR LOS GUARDIAS        ")
            print("-----------------------------------------------------------")
            exit()

# ----- DESAFÍO FINAL: HACKEO ----- #
if boardSize == "pequeño":
    winnerInt = random.randint(0,20)
elif boardSize == "mediano":
    winnerInt = random.randint(0,100)
else:
    winnerInt = random.randint(0,500)
if formato == "binario":
    encryptedWinnerInt = decimal_binario(winnerInt)
elif formato == "octal":
    encryptedWinnerInt = decimal_octal(winnerInt)
else:
    encryptedWinnerInt = decimal_hexadecimal(winnerInt)
    encryptedWinnerInt = "0x"+encryptedWinnerInt

print()
print(r"""______                 __ _         _____                       _      _            _       _         
|  _  \               / _(_)       /  __ \                     | |    | |          | |     | |        
| | | |___  ___  __ _| |_ _  ___   | /  \/ ___  _ __ ___  _ __ | | ___| |_ __ _  __| | ___ | |        
| | | / _ \/ __|/ _` |  _| |/ _ \  | |    / _ \| '_ ` _ \| '_ \| |/ _ \ __/ _` |/ _` |/ _ \| |        
| |/ /  __/\__ \ (_| | | | | (_) | | \__/\ (_) | | | | | | |_) | |  __/ || (_| | (_| | (_) |_|        
|___/ \___||___/\__,_|_| |_|\___/   \____/\___/|_| |_| |_| .__/|_|\___|\__\__,_|\__,_|\___/(_)        
 _   _             _ _                      _            | |_         _     _      _   _            _ 
| | | |           | | |                    | |           |_| |       | |   (_)    | | (_)          | |
| |_| | __ _ ___  | | | ___  __ _  __ _  __| | ___     __ _| |   ___ | |__  _  ___| |_ ___   _____ | |
|  _  |/ _` / __| | | |/ _ \/ _` |/ _` |/ _` |/ _ \   / _` | |  / _ \| '_ \| |/ _ \ __| \ \ / / _ \| |
| | | | (_| \__ \ | | |  __/ (_| | (_| | (_| | (_) | | (_| | | | (_) | |_) | |  __/ |_| |\ V / (_) |_|
\_| |_/\__,_|___/ |_|_|\___|\__, |\__,_|\__,_|\___/   \__,_|_|  \___/|_.__/| |\___|\__|_| \_/ \___/(_)
                             __/ |                                        _/ |                        
                            |___/                                        |__/                         """)
print()
print("¡Eso ha estado genial! Has conseguido llegar hasta el objetivo.")
for i in range(3):
    time.sleep(2.5)
    sys.stdout.write(".")
    sys.stdout.flush()
print()
print("¡¿QUÉ?! ¿Está encriptado?")
print()
print("¡No puede ser! Está encriptado en código {}... SOLO TÚ PUEDES AYUDARNOS A DESENCRIPTAR A DECIMAL.".format(formato))
print("El número en cuestión dice {}... ¿Se te ocurre alguna solución?".format(encryptedWinnerInt))
usersSolve = int(input("Ingresa la solución al acertijo final: "))
print("Desencriptando...")
for i in range(3):
    time.sleep(1.5)
    sys.stdout.write(".")
    sys.stdout.flush()
if formato == "binario":
    if decimal_binario(usersSolve) != encryptedWinnerInt:
            print("\nOh, no... Parece que ese número no era el correcto.")
            print("-----------------------------------------------------------")
            print("       LA RESPUESTA CORRECTA ERA: {}. GAME OVER :'V.       ".format(winnerInt))
            print("-----------------------------------------------------------")
            exit()
    print("\n-----------------------------------------------------------")
    print("Desencriptación exitosa. ¡Felicidades! Has ganado el juego.")
    print("-----------------------------------------------------------")
elif formato == "octal":
    if decimal_octal(usersSolve) != encryptedWinnerInt:
            print("\nOh, no... Parece que ese número no era el correcto.")
            print("-----------------------------------------------------------")
            print("       LA RESPUESTA CORRECTA ERA: {}. GAME OVER :'V.       ".format(winnerInt))
            print("-----------------------------------------------------------")
            exit()
    print("\n-----------------------------------------------------------")
    print("Desencriptación exitosa. ¡Felicidades! Has ganado el juego.")
    print("-----------------------------------------------------------")
else:
    if decimal_hexadecimal(usersSolve) != encryptedWinnerInt[2:]:
        print("\nOh, no... Parece que ese número no era el correcto.")
        print("-----------------------------------------------------------")
        print("       LA RESPUESTA CORRECTA ERA: {}. GAME OVER :'V.       ".format(winnerInt))
        print("-----------------------------------------------------------")
        exit()
    print("\n-----------------------------------------------------------")
    print("Desencriptación exitosa. ¡Felicidades! Has ganado el juego.")
    print("-----------------------------------------------------------")