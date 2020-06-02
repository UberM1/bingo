import random
import math


def IntentoCarton():
    contador = 0
    carton = (
        (0,0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,0,0)
    )
    numerosCarton = 0

    while numerosCarton < 15 :
        contador+=1
        
        if contador == 50 : 
            return IntentoCarton()
        
        numero = random.randint(1, 90)
        columna = math.floor(numero / 10);
        
        if columna == 9 :
            columna = 8
        
        huecos = 0
        
        for i in range(0, 2) :
            if carton[i][columna] == numero :
                huecos = 0
                break
        
        if  huecos < 2 : 
            continue
        
        fila = 0

        for j in range(0, 2) :
            huecos = 0
            
            for i in range(0, 8) :
                if carton[fila][i] == 0 :
                    huecos+=1
            
            if huecos < 5 or carton[fila][columna] != 0 :
                fila+=1;
            else:
                break
        
        if fila == 3: 
            continue

        carton[fila][columna] = numero
        numerosCarton+=1
        contador = 0
    
    for x in range(0, 8):
        huecos = 0
        
        for y in range(0, 2):
            if carton[y][x] == 0 :
                huecos+=1
            if huecos == 3 :
                return IntentoCarton()
    
    return carton

def imprimirCarton(carton) :
    print("\n")
    for columna in range(0, 2):
        for fila in range(0, 8):
            print(carton[fila][columna], sep=" ") 
        print("\n")
    print("\n")

imprimirCarton(IntentoCarton())




