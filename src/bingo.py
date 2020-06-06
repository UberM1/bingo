import random
import math


# Cuenta la cantidad de celdas ocupadas
def contar_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda > 0:
                contador += 1
    return contador

# Retorna True si no hay columnas vacias, False en caso contrario
def sin_colums_vacias(mi_carton):
    for columna in range(9):
        if not(mi_carton[0][columna] or mi_carton[1][columna] or mi_carton[2][columna]):
            return False
    return True

# Retorna True si no hay filas vacias, False en caso contrario
def sin_filas_vacias(mi_carton):
    for fila in mi_carton:
        sum = 0
        for celda in fila:
            sum += celda
        if sum == 0:
            return False
    return True

# Retorna True si las celdas ocupadas se encuentran entre 1 y 90, False en caso contrario
def celdas_ocupadas_1_a_90(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if not(celda >= 0 and celda <= 90):
                return False
    return True

# Retorna True si todos los numeros van de menor a mayor horizontalmente, False en caso contrario
def mayores_a_la_derecha(mi_carton):
    for fila in range(3):
        for columna in range(9):
            if mi_carton[fila][columna] != 0:
                for i in range(columna + 1, 9):
                    if mi_carton[0][i] != 0:
                        if mi_carton[0][i] < mi_carton[fila][columna]:
                            return False
                    if mi_carton[1][i] != 0:
                        if mi_carton[1][i] < mi_carton[fila][columna]:
                            return False
                    if mi_carton[2][i] != 0:
                        if mi_carton[2][i] < mi_carton[fila][columna]:
                            return False
    return True

# Retorna True si todos los numeros van de menor a mayor verticalmente en una columna, False en caso contrario
def mayores_abajo(mi_carton):
    for columna in range(9):
        if mi_carton[0][columna] != 0:
            if mi_carton[1][columna] != 0:
                if mi_carton[0][columna] > mi_carton[1][columna]:
                    return False
            if mi_carton[2][columna] != 0:
                if mi_carton[0][columna] > mi_carton[2][columna]:
                    return False

        if mi_carton[1][columna] != 0:
            if mi_carton[2][columna] != 0:
                if mi_carton[1][columna] > mi_carton[2][columna]:
                    return False
    return True

# Retorna True si no hay numeros repetido, False en caso contrario
def sin_numeros_repeditos(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                aux = 0
                for fila2 in mi_carton:
                    for celda2 in fila2:
                        if celda == celda2:
                            aux += 1
                if aux > 1:
                    return False
    return True
# Retorna True si no hay mas de 2 vacios seguidos 
def vacios_segui2(mi_carton):
    count = 0
    for fila in mi_carton:
        count = 0
        for celda in fila:
            if(celda == 0):
                count+=1
            if(celda != 0):
                count = 0
            if(count > 2):
                return False
    if count > 2:
        return False
    else: 
        return True
# Retorna True si no hay mas de 2 rellenos seguidos
def completos_segui2(mi_carton):
    count = 0
    for fila in mi_carton:
        count = 0
        for celda in fila:
            if(celda != 0):
                count += 1
            if(celda == 0):
                count = 0
            if(count > 2):
                return False
    if count > 2:
        return False
    else: 
        return True
#genera un carton valido
def Generar(): 
    bandera = False
    i=0
    while bandera == False:
        CARTON = IntentoCarton()
        if((contar_celdas_ocupadas(CARTON)==15) and (sin_colums_vacias(CARTON)) and (sin_filas_vacias(CARTON)) and (celdas_ocupadas_1_a_90(CARTON)) and (mayores_a_la_derecha(CARTON)) and (mayores_abajo(CARTON)) and (sin_numeros_repeditos(CARTON)) and (vacios_segui2(CARTON)) and (completos_segui2(CARTON))):
            bandera = True
            break
    return CARTON
#genera un intento de carton 
def IntentoCarton():
    contador = 0
    carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while (numerosCarton < 15):
        contador+=1
        
        if (contador == 50): 
            return IntentoCarton()
        
        numero = random.randint(1, 90)
        columna = math.floor(numero / 10);
        
        if(columna == 9):
            columna = 8
        
        huecos = 0
        
        for i in range(0, 3):
            if (carton[i][columna] == 0):
                huecos += 1
            if (carton[i][columna] == numero):
                huecos = 0
                break
        
        if  (huecos < 2): 
            continue
        
        fila = 0

        for j in range(0, 3):
            huecos = 0
            
            for i in range(0, 9):
                if(carton[fila][i] == 0):
                    huecos+=1
            
            if(huecos < 5 or carton[fila][columna] != 0):
                fila+=1;
            else:
                break
        
        if(fila == 3): 
            continue

        carton[fila][columna] = numero
        numerosCarton+=1
        contador = 0
    
    for x in range(0, 9):
        huecos = 0
        
        for y in range(0, 3):
            if carton[y][x] == 0 :
                huecos+=1
            if huecos == 3 :
                return IntentoCarton()
    
    return carton
