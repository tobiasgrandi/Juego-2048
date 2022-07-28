import random

nuevo_numero = [2, 4] #Lista de los nuevos posibles numeros
grilla = []
filas_columnas = 3 #cantidad de filas y columnas
valor_llegada = 2048
tecla_arriba = "w"
tecla_izquierda = "a"
tecla_abajo = "s"
tecla_derecha = "d"


def inicializar_juego():
    """Crea una matriz que se usará como grilla para jugar con la cantidad de filas y columnas que se indiquen."""
    
    for i in range(filas_columnas):
        grilla.append([])
        for j in range(filas_columnas):
            grilla[i].append(0)
    insertar_nuevo_random(grilla)
    return grilla


def convertir_grilla_blanco(grilla):
    """Convierte los 0 de la grilla en espacios en blanco"""

    for i in range(filas_columnas):
        for j in range(filas_columnas):
            if grilla[i][j] == 0:
                grilla[i][j] = " "
    return grilla


def convertir_grilla_cero(grilla):
    """Convierte los espacios en blanco de la grilla en 0"""

    for i in range(filas_columnas):
        for j in range(filas_columnas):
            if grilla[i][j] == " ":
                grilla[i][j] = 0
    return grilla


def copia_grilla(grilla):
    """Realiza una copia de la grilla"""
    
    grilla_2 = []
    for i in range(filas_columnas):
        grilla_2.append([])
        for j in range(filas_columnas):
            grilla_2[i].append(grilla[i][j])
    return grilla_2


def insertar_nuevo_random(grilla):
    """Inserta un nuevo valor en una posicion random"""

    convertir_grilla_cero(grilla)
    
    grilla_prueba = []
    for i in range(filas_columnas):
        for j in range(filas_columnas):
            grilla_prueba.append(grilla[i][j])
    if 0 in grilla_prueba:
        if max(grilla_prueba) == 0:
            grilla[random.choice(range(filas_columnas))][random.choice(range(filas_columnas))] = random.choice(nuevo_numero)
        else:
           while True:
                fila_random =  random.choice(range(filas_columnas))
                columna_random = random.choice(range(filas_columnas))
                if grilla[fila_random][columna_random] == 0:
                    grilla[fila_random][columna_random] = random.choice(nuevo_numero)
                    return grilla


def mostrar_juego(grilla):
    """Crea la parte gráfica del juego"""

    convertir_grilla_blanco(grilla) 
    
    for i in range(filas_columnas):
        if i >= 1:
            print("")
            print("-"*(len(grilla)*13))
        for j in range(filas_columnas):
            print(grilla[i][j], end="      |     ")
    print()
    return grilla


def trasponer(grilla):
    """Traspone la matriz grilla para facilitar su manipulación"""

    for i in range(filas_columnas):
        for j in range(len(grilla[0])):
            if i < j:
                grilla[i][j], grilla[j][i] = grilla[j][i], grilla[i][j]
    return grilla


def movimientos_restantes(grilla):
    """Comprueba si, antes de perder, quedan movimientos a realizar"""
    
    grilla_mov = []
    grilla_comp = [False]*(filas_columnas**2)
    for h in range(filas_columnas):
        for i in range(filas_columnas):
            for j in range(1, filas_columnas-1):
                if grilla[i][j] == grilla[i][j+1] or grilla[i][j] == grilla[i][j-1]:
                    grilla_mov.append(True)
                elif grilla[i][j] != grilla[i][j+1] and grilla[i][j] != grilla[i][j-1]:
                    grilla_mov.append(False)
    if grilla_mov == grilla_comp:
        return True
    elif grilla_mov != grilla_comp:
        return False


def juego_ganado(grilla):
    """Comprueba  si se llegó al valor final"""
    
    for i in grilla:
        for j in range(filas_columnas):
            if i[j] == valor_llegada:
                print("")
                return True


def juego_perdido(grilla):
    """Comprueba si ya no hay movimientos a realizar"""
    
    convertir_grilla_cero(grilla)

    grilla_comprobar = []
    for i in grilla:
        grilla_comprobar += i
    if 0 not in grilla_comprobar:
        if movimientos_restantes(grilla) == True and movimientos_restantes(trasponer(grilla)) == True:
            return True
 
                
def pedir_direccion(grilla):
    """Pide la dirección de movimiento al usuario"""

    while True:
        direccion = input(f"Ingrese una tecla de dirección {tecla_arriba, tecla_izquierda, tecla_abajo, tecla_derecha}: ")
        if direccion == tecla_arriba:
            print()
            return tecla_arriba
        elif direccion == tecla_izquierda:
            print()
            return tecla_izquierda
        elif direccion == tecla_abajo:
            print()
            return tecla_abajo
        elif direccion == tecla_derecha:
            print()
            return tecla_derecha
        else:
            print("Ingrese una tecla válida")


def suma_derecha(grilla):
    """Suma los valores hacia la derecha"""

    resultados = []

    for h in range(filas_columnas):
        for i in range(filas_columnas):
            for j in range(filas_columnas-1):
                
                if grilla[i][filas_columnas-1] == grilla[i][filas_columnas-2] and grilla[i][filas_columnas-2] not in resultados:
                    grilla[i][filas_columnas-1] *= 2
                    grilla[i][filas_columnas-2] = 0
                    resultados.append(grilla[i][filas_columnas-1])
                
                elif grilla[i][j+1] == grilla[i][j]  and grilla[i][j+1] not in resultados:
                    grilla[i][j+1] *= 2
                    grilla[i][j] = 0
                    resultados.append(grilla[i][j+1])
                
                elif grilla[i][j+1] == 0 and j != filas_columnas:
                    grilla[i][j+1] = grilla[i][j]
                    grilla[i][j] = 0         
    return grilla


def suma_izquierda(grilla):
    """Suma los valores hacia la izquierda"""

    resultados = []

    for h in range(filas_columnas):
        for i in range(filas_columnas):
            for j in range(-1, -filas_columnas, -1):
                
                if grilla[i][0] == grilla[i][1] and grilla[i][0] not in resultados:
                    grilla[i][0] *= 2
                    grilla[i][1] = 0
                    resultados.append(grilla[i][0])
                
                elif grilla[i][j] == grilla[i][j-1] and j-1 != 0 and grilla[i][j-1] not in resultados:
                    grilla[i][j-1] *= 2
                    grilla[i][j] = 0
                    resultados.append(grilla[i][j-1])
                
                elif grilla[i][j-1] == 0:
                    grilla[i][j-1] = grilla[i][j]
                    grilla[i][j] = 0
                

def actualizar_juego(grilla, dir):
    """Actualiza el juego dependiendo del movimiento"""

    grilla_2 = copia_grilla(grilla)
    
    if dir == tecla_arriba or dir == tecla_abajo:
        if dir == tecla_arriba:
            trasponer(grilla_2)
            suma_izquierda(grilla_2)
            trasponer(grilla_2)
        elif dir == tecla_abajo:
            trasponer(grilla_2)
            suma_derecha(grilla_2)
            trasponer(grilla_2)
    elif dir == tecla_izquierda:
        suma_izquierda(grilla_2)
    elif dir == tecla_derecha:
        suma_derecha(grilla_2)
    return grilla_2