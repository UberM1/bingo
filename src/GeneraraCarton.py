import bingo
import carton
def Generar(): 
    bandera = False
    i=0
    while bandera == False:
        i+=1
        print(i,end=' ')
        CARTON = carton.IntentoCarton()
        if((bingo.contar_celdas_ocupadas(CARTON)==15) and (bingo.sin_colums_vacias(CARTON)) and (bingo.sin_filas_vacias(CARTON)) and (bingo.celdas_ocupadas_1_a_90(CARTON)) and (bingo.mayores_a_la_derecha(CARTON)) and (bingo.mayores_abajo(CARTON)) and (bingo.sin_numeros_repeditos(CARTON)) and (bingo.vacios_segui2(CARTON)) and (bingo.completos_segui2(CARTON))):
            bandera = True
            break
    if bandera == True : 
        print("El carton Generado Es:\n")
        carton.imprimirCarton(CARTON)
    else:
        print("no se encontro carton valido")
    return CARTON