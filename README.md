# LAB1_202373504-3
Nombres:
    Lucas Ansieta M. Rol: 202373504-3. Paralelo 200.
    Benjamín Palacios T. Rol: 202373532-9. Paralelo 200.

Entornos de desarrollo: Visual Studio Code (macOS).

Instrucciones de ejecución:
    Desde la consola, usando el siguiente comando: python3 t1.py

Consideraciones:
    Decidimos hacer la implementación de la matriz (tablero) a través de listas, pues el acceso a los datos del tablero es mucho más cómodo de esta forma. Esta implementación nos llevó a que la interfaz del tablero pueda ser distanta a la mostrada en el ejemplo, la vista al imprimir el tablero como listas resulta mucho más agradable si hablamos de un largo pequeño. Sin embargo, quizás este formato de impresión no sea del todo óptimo si el largo ingresado es muy grande... Por esta razón, implementamos un tercer input al momento de empezar el juego, siendo "1" la vista del tablero como listas y "2" la vista del tablero como carácteres (tal como se ve en los ejemplos).
    
Especificación de los algoritmos:
    - generarTablero(largo): Crea una lista llamada 'tablero', a la cual se le agregan 11 listas que representan las 11 filas del pasillo... En cuanto a las columnas, éstas simplemente están representadas por cada uno de los elementos de cada una de las 11 listas, la función toma como parámetro el largo 'largo' del tablero para saber cuantos elementos va a tener cada una de las 11 listas de 'tablero'. De este modo, se puede acceder a un elemento en particular de la siguiente forma: tablero[coordY][coordX].
    - imprimirTablero(seleccion, tablero, largo): En base a la selección del usuario, imprime el tablero de una forma más cómoda a la vista pero adaptada a menores tamaños de tablero, o bien, de una forma menos cómoda a la vista pero adaptada a mayores tamaños de tablero.
    - binario_decimal(binario): La función toma como parámetro un número binario 'binario' en formato string, el cuál mediante el algoritmo visto en clases es transformado y retornado a su valor decimal. El algoritmo consiste en:
        1. Dar vuelta el binario (ej: si era 1010, que pase a ser 0101)
        2. Para cada número por separado dentro del binario dado vuelta se repite el siguiente ciclo: El número se multiplica por 2^i, donde i es un iterador inicializado en 0 que va sumando 1 a su valor cada vez que una iteración culmina... Luego, el resultado de esta multiplicación se suma a numeroFinal: una variable originalmente inicializada en 0 (Notar que el motivo de hacer el swap al binario en el paso 1 es para emular de manera fideidigna el algoritmo visto en clases).
        3. La función retorna la variable numeroFinal, que corresponde al valor en decimal del binario 'binario'.
        4. En caso de que 'binario' no corresponda a un número binario, la función es capaz de detectarlo y retornar un error. De este modo no habrá retorno de un resultado equívoco.
    - octal_decimal(octal): Sigue prácticamente el mismo algoritmo que binario_decimal(binario), con la única diferencia que en el paso 2 del algoritmo, en vez de que cada número por separado se multiplique por 2^i, se multiplica por 8^i. La función es igualmente capaz de detectar si 'octal' no corresponde a un número en formato octal.
    - hexadecimal_decimal(hexadecimal): Sigue prácticamente el mismo algoritmo que binario_decimal(binario), con las siguientes diferencias:
        1. En el paso 2 del algoritmo, en vez de que el valor decimal de cada caracter por separado se multiplique por 2^i, se multiplica por 16^i. La función es igualmente capaz de detectar si 'hexadecimal' no corresponde a un número en formato hexadecimal.
        2. Dada la naturaleza de los números hexadecimales, la función contiene un diccionario cuyas claves representan a cada caracter en hexadecimal (0, 1, ..., E, F), y sus valores a sus valores (valga la redundancia) en decimal. De este modo, lo que se va sumando a la variable numeroFinal no es hexadecimal[i], sino dict[hexadecimal[i]] (en el código, la iteracion es mediante un ciclo for y el iterador 'caracter', pero la idea de la implementación es la misma).
    - decimal_binario(decimal): La función toma como parámetro un número decimal 'decimal' en formato int, el cuál mediante el algoritmo visto en clases es transformado y retornado a su valor binario. El algoritmo consiste en:
        1. Inicializo dos variables: 'resultado' y 'resto'... 'resultado' siendo la división entera entre 'decimal' y 2, y 'resto' siendo el resto de dicha división.
        2. Inicializo una variable llamada 'strResultado', la cual irá correspondiendo a la concatenación de los restos que vayan dejando las divisiones enteras.
        3. Se vuelven a repetir los pasos anteriores, con la sutileza de que ahora la variable 'resultado' corresponderá a la división entera entre el valor de 'resultado' de la iteración anterior y 2 (en código: resultado = resultado//2). Este bucle terminará cuando resultado eventualmente sea igual a 0.
        4. Dado que 'strResultado' será la concatenación de todos los restos, pero el algoritmo visto en clases sugiere que el binario resultante debe verse desde el resto de la división más reciente hasta llegar al resto de la primera que se hizo, solo queda invertir 'strResultado' para llegar al número binario que estamos buscando.
    - decimal_octal(decimal): Sigue prácticamente el mismo algoritmo que decimal_binario(decimal), con la única diferencia que en el paso 1 del algoritmo, 'resultado' corresponderá a la división entera entre 'decimal' y 8. Lo mismo ocurriendo al redefinir 'resultado' en el paso 3 (en código: resultado = resultado//8).
    - decimal_hexadecimal(decimal): Sigue prácticamente el mismo algoritmo que decimal_binario(decimal), con las siguientes diferencias:
        1. En el paso 1 del algoritmo, 'resultado' corresponderá a la división entera entre 'decimal' y 16. Lo mismo ocurriendo al redefinir 'resultado' en el paso 3 (en código: resultado = resultado//16).
        2. Dada la naturaleza de los números hexadecimales, la función contiene un diccionario cuyas claves representan a los valores decimales desde el 0 hasta el 15, y sus valores a sus valores (valga la redundancia) en hexadecimal (0, 1, ..., E, F). De este modo, lo que se va concatenando a strResultado no es directamente la variable 'resto' (pues, por ejemplo, si el resto termina siendo 15, a 'strResultado' no se le debería concatenar directamente un 15), sino mas bien dict[resto] (de este modo, si el resto es 15, a 'strResultado' se le concatena correctamente 'F').
    Tal como se puede apreciar, intentamos que los algoritmos fuesen lo más similares posibles a lo visto en clases.
